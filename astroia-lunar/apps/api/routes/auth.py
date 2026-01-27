"""Routes d'authentification"""

from fastapi import APIRouter, Depends, HTTPException, status, Request, Header
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload, selectinload
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional, Tuple, Literal
from uuid import UUID
from types import SimpleNamespace
import logging
import httpx

from database import get_db
from models.user import User
from config import settings

logger = logging.getLogger(__name__)

router = APIRouter()

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login", auto_error=False)


# === SCHEMAS ===
class UserRegister(BaseModel):
    email: EmailStr
    password: str
    birth_date: Optional[str] = None
    birth_time: Optional[str] = None
    birth_latitude: Optional[float] = None
    birth_longitude: Optional[float] = None
    birth_place_name: Optional[str] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):
    id: int
    email: str
    birth_date: Optional[str]
    birth_time: Optional[str]
    birth_place_name: Optional[str]
    is_premium: bool
    created_at: datetime


class OAuthUserInfo(BaseModel):
    """Info utilisateur optionnelle (Apple uniquement, premier login)"""
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class OAuthLoginRequest(BaseModel):
    """Requête de login OAuth (Google ou Apple)"""
    provider: Literal["google", "apple"]
    id_token: str
    user_info: Optional[OAuthUserInfo] = None  # Apple uniquement


class OAuthLoginResponse(BaseModel):
    """Réponse de login OAuth"""
    access_token: str
    token_type: str = "bearer"
    is_new_user: bool


# === HELPERS ===
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    # python-jose requires "sub" to be a string
    if "sub" in to_encode and isinstance(to_encode["sub"], int):
        to_encode["sub"] = str(to_encode["sub"])
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


# === OAUTH TOKEN VERIFICATION ===
async def verify_google_token(id_token: str) -> dict:
    """
    Vérifie un ID token Google et retourne les informations utilisateur.

    Returns:
        dict avec keys: sub (provider_id), email, email_verified, name, picture
    """
    try:
        # Utiliser l'endpoint tokeninfo de Google pour valider le token
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://oauth2.googleapis.com/tokeninfo?id_token={id_token}"
            )

            if response.status_code != 200:
                logger.warning(f"Google token validation failed: {response.status_code}")
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token Google invalide"
                )

            data = response.json()

            # Vérifier que l'email est vérifié
            if not data.get("email_verified", "false") == "true":
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Email Google non vérifié"
                )

            return {
                "sub": data["sub"],
                "email": data["email"],
                "name": data.get("name"),
                "picture": data.get("picture"),
            }
    except httpx.RequestError as e:
        logger.error(f"Google token verification network error: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Impossible de vérifier le token Google"
        )


async def verify_apple_token(id_token: str, user_info: Optional[OAuthUserInfo] = None) -> dict:
    """
    Vérifie un ID token Apple et retourne les informations utilisateur.

    Note: Apple ne fournit le nom qu'au premier login, d'où le paramètre user_info optionnel.

    Returns:
        dict avec keys: sub (provider_id), email
    """
    try:
        # Décoder le token JWT Apple (sans vérification de signature pour l'instant)
        # En production, il faudrait vérifier avec les clés publiques Apple
        # https://appleid.apple.com/auth/keys
        unverified_payload = jwt.decode(
            id_token,
            options={"verify_signature": False, "verify_aud": False}
        )

        email = unverified_payload.get("email")
        sub = unverified_payload.get("sub")

        if not email or not sub:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token Apple invalide: email ou sub manquant"
            )

        return {
            "sub": sub,
            "email": email,
            "name": f"{user_info.first_name or ''} {user_info.last_name or ''}".strip() if user_info else None,
        }
    except JWTError as e:
        logger.error(f"Apple token decode error: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token Apple invalide"
        )


async def resolve_dev_user(
    user_identifier: str,
    db: AsyncSession
) -> Tuple[User, str]:
    """
    Résolution déterministe d'un utilisateur en mode DEV_AUTH_BYPASS.

    Args:
        user_identifier: UUID string, integer string, ou email
        db: Session de base de données

    Returns:
        Tuple (User, method) où method décrit comment l'utilisateur a été résolu

    Raises:
        HTTPException: Si l'utilisateur ne peut pas être résolu
    """
    # Tentative 1: Traiter comme UUID et chercher par dev_external_id
    try:
        user_uuid = UUID(user_identifier)
        result = await db.execute(
            select(User)
            .where(User.dev_external_id == str(user_uuid))
            .options(joinedload(User.natal_chart))
        )
        user = result.scalar_one_or_none()

        if user:
            logger.info(f"✅ DEV_AUTH_BYPASS: user trouvé via dev_external_id={user_uuid}")
            return user, "header_uuid"

        # Créer un nouvel utilisateur dev avec cet UUID
        logger.info(f"🆕 DEV_AUTH_BYPASS: création user avec dev_external_id={user_uuid}")
        try:
            # Utiliser un hash pré-calculé pour éviter les problèmes avec bcrypt
            # Hash de "dev-password" pré-calculé avec bcrypt (généré avec bcrypt.gensalt())
            dev_password_hash = "$2b$12$A2rj/gsY/fAzI5GY9TCQFOByzS/J8TIL3ElOyFSAAxHzVdg.OluOq"
            
            new_user = User(
                email=f"dev+{str(user_uuid)[:8]}@local.dev",
                hashed_password=dev_password_hash,
                dev_external_id=str(user_uuid),
                is_active=True,
                is_premium=False
            )
            db.add(new_user)
            await db.commit()
            await db.refresh(new_user)
            logger.info(f"✅ DEV_AUTH_BYPASS: user créé - id={new_user.id}, email={new_user.email}")
            return new_user, "header_uuid_created"
        except IntegrityError as e:
            # L'utilisateur existe peut-être déjà (email ou dev_external_id en double)
            await db.rollback()
            logger.warning(f"⚠️ DEV_AUTH_BYPASS: échec création user avec dev_external_id={user_uuid}, erreur: {e}")
            # Réessayer de chercher par dev_external_id (peut-être créé entre temps)
            result = await db.execute(
                select(User)
                .where(User.dev_external_id == str(user_uuid))
                .options(joinedload(User.natal_chart))
            )
            user = result.scalar_one_or_none()
            if user:
                logger.info(f"✅ DEV_AUTH_BYPASS: user trouvé après rollback via dev_external_id={user_uuid}")
                return user, "header_uuid"
            # Si toujours pas trouvé, essayer par email généré
            email = f"dev+{str(user_uuid)[:8]}@local.dev"
            result = await db.execute(
                select(User)
                .where(User.email == email)
                .options(joinedload(User.natal_chart))
            )
            user = result.scalar_one_or_none()
            if user:
                logger.info(f"✅ DEV_AUTH_BYPASS: user trouvé via email={email} après échec création")
                return user, "header_uuid_email_fallback"
            # Si toujours pas trouvé, continuer vers les autres méthodes de résolution

    except (ValueError, TypeError):
        # Pas un UUID valide, continuer
        pass

    # Tentative 2: Traiter comme integer ID
    try:
        user_id = int(user_identifier)
        result = await db.execute(
            select(User)
            .where(User.id == user_id)
            .options(joinedload(User.natal_chart))
        )
        user = result.scalar_one_or_none()

        if user:
            logger.info(f"✅ DEV_AUTH_BYPASS: user trouvé via id={user_id}")
            return user, "header_int"

        logger.warning(f"⚠️ DEV_AUTH_BYPASS: user_id={user_id} introuvable")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"DEV_AUTH_BYPASS: user avec id={user_id} introuvable"
        )
    except (ValueError, TypeError):
        # Pas un integer valide
        pass

    # Tentative 3: Traiter comme email
    result = await db.execute(
        select(User)
        .where(User.email == user_identifier)
        .options(joinedload(User.natal_chart))
    )
    user = result.scalar_one_or_none()

    if user:
        logger.info(f"✅ DEV_AUTH_BYPASS: user trouvé via email={user_identifier}")
        return user, "header_email"

    # Tentative 4: Fallback vers dev@local.dev (utilisateur par défaut pour DEV)
    logger.info("📥 DEV_AUTH_BYPASS: pas de header/env, fallback vers dev@local.dev")
    result = await db.execute(
        select(User)
        .where(User.email == "dev@local.dev")
        .options(joinedload(User.natal_chart))
    )
    dev_user = result.scalar_one_or_none()

    if dev_user:
        logger.info(f"✅ DEV_AUTH_BYPASS resolved: user_id={dev_user.id}, method=dev_default")
        return dev_user, "dev_default"

    # Créer le user dev@local.dev si il n'existe pas
    logger.info("🆕 DEV_AUTH_BYPASS: création user dev@local.dev")
    try:
        # Utiliser un hash pré-calculé pour éviter les problèmes avec bcrypt
        # Hash de "dev-password" pré-calculé avec bcrypt (généré avec bcrypt.gensalt())
        dev_password_hash = "$2b$12$A2rj/gsY/fAzI5GY9TCQFOByzS/J8TIL3ElOyFSAAxHzVdg.OluOq"
        
        new_dev_user = User(
            email="dev@local.dev",
            hashed_password=dev_password_hash,
            is_active=True,
            is_premium=False
        )
        db.add(new_dev_user)
        await db.commit()
        await db.refresh(new_dev_user)
        logger.info(f"✅ DEV_AUTH_BYPASS: user dev@local.dev créé - id={new_dev_user.id}")
        return new_dev_user, "dev_default_created"
    except IntegrityError:
        # L'utilisateur a peut-être été créé entre temps
        await db.rollback()
        result = await db.execute(select(User).where(User.email == "dev@local.dev"))
        dev_user = result.scalar_one_or_none()
        if dev_user:
            logger.info(f"✅ DEV_AUTH_BYPASS: user dev@local.dev trouvé après rollback - id={dev_user.id}")
            return dev_user, "dev_default"
    except Exception as e:
        # Autres erreurs (comme bcrypt)
        await db.rollback()
        logger.warning(f"⚠️ DEV_AUTH_BYPASS: erreur lors de la création de dev@local.dev: {e}")
        # Réessayer de chercher l'utilisateur
        result = await db.execute(select(User).where(User.email == "dev@local.dev"))
        dev_user = result.scalar_one_or_none()
        if dev_user:
            logger.info(f"✅ DEV_AUTH_BYPASS: user dev@local.dev trouvé après erreur - id={dev_user.id}")
            return dev_user, "dev_default"

    # Échec: aucune résolution possible (ne devrait jamais arriver si dev@local.dev fonctionne)
    logger.error(f"❌ DEV_AUTH_BYPASS: impossible de résoudre user avec identifier={user_identifier}")
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"DEV_AUTH_BYPASS: impossible de résoudre user avec identifier={user_identifier}"
    )


async def get_current_user(
    x_dev_user_id: Optional[str] = Header(default=None, alias="X-Dev-User-Id"),
    x_dev_external_id: Optional[str] = Header(default=None, alias="X-Dev-External-Id"),
    token: Optional[str] = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
) -> User:
    """Dependency pour récupérer le user connecté"""
    from jose.exceptions import ExpiredSignatureError

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Impossible de valider les identifiants",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # ===== MODE DEV: bypass avec header X-Dev-User-Id OU X-Dev-External-Id (uniquement en development) =====
    if settings.APP_ENV == "development" and settings.DEV_AUTH_BYPASS:
        logger.info("🔧 DEV_AUTH_BYPASS enabled")

        # Priorité 1: Si header X-Dev-External-Id présent (UUID, email), résoudre via DB
        if x_dev_external_id:
            logger.info(f"📥 DEV_AUTH_BYPASS: X-Dev-External-Id header={x_dev_external_id}")
            user, method = await resolve_dev_user(x_dev_external_id, db)
            logger.info(f"✅ DEV_AUTH_BYPASS resolved: user_id={user.id}, method={method}")
            return user

        # Priorité 2: Si header X-Dev-User-Id présent, essayer de résoudre via DB d'abord (pour UUID)
        # Si c'est un int, créer un user lightweight avec email synthétique
        if x_dev_user_id:
            logger.info(f"📥 DEV_AUTH_BYPASS: X-Dev-User-Id header={x_dev_user_id}")

            # Tenter de parser comme integer (cas le plus courant)
            try:
                user_id = int(x_dev_user_id)
                logger.info(f"✅ DEV_AUTH_BYPASS: user lightweight créé avec id={user_id} (sans DB)")
                # Retourner un objet lightweight avec id ET email pour éviter crash ailleurs
                return SimpleNamespace(id=user_id, email=f"dev+{user_id}@local.dev")
            except (ValueError, TypeError):
                # Header présent mais non-int → essayer de résoudre via DB (peut être UUID/email)
                logger.info(f"📥 DEV_AUTH_BYPASS: X-Dev-User-Id n'est pas un int, résolution via DB: {x_dev_user_id}")
                try:
                    user, method = await resolve_dev_user(x_dev_user_id, db)
                    logger.info(f"✅ DEV_AUTH_BYPASS resolved: user_id={user.id}, method={method}")
                    return user
                except HTTPException:
                    # Si résolution échoue, erreur explicite
                    logger.warning(f"❌ DEV_AUTH_BYPASS: X-Dev-User-Id invalide ou introuvable: {x_dev_user_id}")
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail=f"DEV_AUTH_BYPASS: X-Dev-User-Id invalide ou introuvable: {x_dev_user_id}",
                        headers={"WWW-Authenticate": "Bearer"},
                    )
        
        # Priorité 3: Si pas de header mais DEV_USER_ID en env, utiliser celui-ci
        if settings.DEV_USER_ID:
            user_identifier = settings.DEV_USER_ID
            logger.info(f"📥 DEV_AUTH_BYPASS: DEV_USER_ID env={user_identifier}")
            
            # Tenter de parser comme integer
            try:
                user_id = int(user_identifier)
                logger.info(f"✅ DEV_AUTH_BYPASS: user lightweight créé avec id={user_id} depuis env (sans DB)")
                # Retourner un objet lightweight avec id ET email pour éviter crash ailleurs
                return SimpleNamespace(id=user_id, email=f"dev+{user_id}@local.dev")
            except (ValueError, TypeError):
                # DEV_USER_ID non-int → fallback vers resolve_dev_user (pour UUID/email)
                logger.info(f"📥 DEV_AUTH_BYPASS: DEV_USER_ID n'est pas un int, résolution via DB: {user_identifier}")
                user, method = await resolve_dev_user(user_identifier, db)
                logger.info(f"✅ DEV_AUTH_BYPASS resolved: user_id={user.id}, method={method}")
                return user
        
        # Fallback: chercher ou créer user avec email dev@local.dev
        logger.info("📥 DEV_AUTH_BYPASS: pas de header/env, fallback vers dev@local.dev")
        result = await db.execute(
            select(User)
            .where(User.email == "dev@local.dev")
            .options(joinedload(User.natal_chart))
        )
        dev_user = result.scalar_one_or_none()

        if dev_user:
            logger.info(f"✅ DEV_AUTH_BYPASS resolved: user_id={dev_user.id}, method=dev_default")
            return dev_user

        # Créer le user dev@local.dev
        logger.info("🆕 DEV_AUTH_BYPASS: création user dev@local.dev")
        try:
            # Utiliser un hash pré-calculé pour éviter les problèmes avec bcrypt
            # Hash de "dev-password" pré-calculé avec bcrypt (généré avec bcrypt.gensalt())
            dev_password_hash = "$2b$12$A2rj/gsY/fAzI5GY9TCQFOByzS/J8TIL3ElOyFSAAxHzVdg.OluOq"
            dev_user = User(
                email="dev@local.dev",
                hashed_password=dev_password_hash,
                is_active=True,
                is_premium=False
            )
            db.add(dev_user)
            await db.commit()
            await db.refresh(dev_user)
            logger.info(f"✅ DEV_AUTH_BYPASS created: user_id={dev_user.id}, method=dev_default")
            return dev_user
        except IntegrityError:
            # L'utilisateur a peut-être été créé entre temps
            await db.rollback()
            result = await db.execute(
                select(User)
                .where(User.email == "dev@local.dev")
                .options(joinedload(User.natal_chart))
            )
            dev_user = result.scalar_one_or_none()
            if dev_user:
                logger.info(f"✅ DEV_AUTH_BYPASS: user dev@local.dev trouvé après rollback - id={dev_user.id}")
                return dev_user
            raise

    # ===== MODE NORMAL: JWT =====
    if not token:
        logger.warning("❌ JWT: token manquant dans header Authorization")
        raise credentials_exception

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id_str: str = payload.get("sub")
        if user_id_str is None:
            logger.warning("❌ JWT decode: 'sub' claim manquant")
            raise credentials_exception
        # Convert string sub to int
        try:
            user_id: int = int(user_id_str)
        except (ValueError, TypeError):
            logger.warning(f"❌ JWT decode: 'sub' n'est pas un entier valide: {user_id_str}")
            raise credentials_exception
    except ExpiredSignatureError:
        logger.warning("❌ JWT decode: token expiré")
        raise credentials_exception
    except JWTError as e:
        logger.warning(f"❌ JWT decode: erreur de signature/format: {e}")
        raise credentials_exception

    # Eager loading pour optimiser les queries (évite N+1 queries dans les routes)
    # - natal_chart: chargé systématiquement (one-to-one, toujours petit, utilisé partout)
    # - lunar_reports, transits_overview: lazy load (one-to-many, chargés seulement si nécessaire)
    result = await db.execute(
        select(User)
        .where(User.id == user_id)
        .options(joinedload(User.natal_chart))
    )
    user = result.scalar_one_or_none()

    if user is None:
        logger.warning(f"❌ User non trouvé en DB: user_id={user_id}")
        raise credentials_exception

    return user


# === ROUTES ===
@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserRegister, db: AsyncSession = Depends(get_db)):
    """Inscription d'un nouvel utilisateur"""
    
    # Vérifier si l'email existe déjà
    result = await db.execute(select(User).where(User.email == user_data.email))
    existing_user = result.scalar_one_or_none()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cet email est déjà utilisé"
        )
    
    # Créer l'utilisateur
    user = User(
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
        birth_date=user_data.birth_date,
        birth_time=user_data.birth_time,
        birth_latitude=str(user_data.birth_latitude) if user_data.birth_latitude else None,
        birth_longitude=str(user_data.birth_longitude) if user_data.birth_longitude else None,
        birth_place_name=user_data.birth_place_name
    )
    
    db.add(user)
    await db.commit()
    await db.refresh(user)
    
    # Générer le token
    access_token = create_access_token(data={"sub": user.id})
    
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    """Connexion"""
    
    # Trouver l'utilisateur
    result = await db.execute(select(User).where(User.email == form_data.username))
    user = result.scalar_one_or_none()

    # Vérifier si l'utilisateur existe et a un mot de passe (pas un compte OAuth pur)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou mot de passe incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Si l'utilisateur est un compte OAuth sans mot de passe
    if user.hashed_password is None:
        provider = user.auth_provider or "social"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Ce compte utilise la connexion {provider.capitalize()}. Veuillez vous connecter via {provider.capitalize()}.",
        )

    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou mot de passe incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Générer le token
    access_token = create_access_token(data={"sub": user.id})
    
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/oauth", response_model=OAuthLoginResponse)
async def oauth_login(
    request: OAuthLoginRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Login/Register via OAuth provider (Google ou Apple).

    - Vérifie le id_token avec le provider
    - Crée l'utilisateur si nouveau
    - Retourne JWT + flag is_new_user
    """
    # Vérifier le token selon le provider
    if request.provider == "google":
        oauth_user = await verify_google_token(request.id_token)
    elif request.provider == "apple":
        oauth_user = await verify_apple_token(request.id_token, request.user_info)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Provider non supporté: {request.provider}"
        )

    provider_id = oauth_user["sub"]
    email = oauth_user["email"]

    # Chercher un utilisateur existant avec ce provider_id
    result = await db.execute(
        select(User).where(
            User.auth_provider == request.provider,
            User.provider_id == provider_id
        )
    )
    user = result.scalar_one_or_none()

    is_new_user = False

    if not user:
        # Vérifier si un compte existe déjà avec cet email
        result = await db.execute(
            select(User).where(User.email == email)
        )
        existing_user = result.scalar_one_or_none()

        if existing_user:
            # Lier le compte OAuth au compte existant
            existing_user.auth_provider = request.provider
            existing_user.provider_id = provider_id
            user = existing_user
            logger.info(f"OAuth: compte {email} lié à {request.provider}")
        else:
            # Créer un nouveau compte
            user = User(
                email=email,
                hashed_password=None,  # Pas de mot de passe pour OAuth
                auth_provider=request.provider,
                provider_id=provider_id,
            )
            db.add(user)
            is_new_user = True
            logger.info(f"OAuth: nouveau compte créé pour {email} via {request.provider}")

        await db.commit()
        await db.refresh(user)

    # Générer le JWT
    access_token = create_access_token(data={"sub": user.id})

    # is_new_user = True si le user vient d'être créé OU si son profil est incomplet
    is_new_user = is_new_user or user.birth_date is None

    return OAuthLoginResponse(
        access_token=access_token,
        token_type="bearer",
        is_new_user=is_new_user
    )


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    """Récupère le profil de l'utilisateur connecté"""
    return current_user

