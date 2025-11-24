"""
Configuration SQLAlchemy (async)
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from config import settings

# Convertir postgresql:// en postgresql+asyncpg://
DATABASE_URL = settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

# Log pour debug (masquer le mot de passe)
import logging
from urllib.parse import urlparse
logger = logging.getLogger(__name__)
parsed = urlparse(settings.DATABASE_URL)
logger.info(f"🔗 Database URL: postgresql://{parsed.username}:***@{parsed.hostname}:{parsed.port}{parsed.path}")
logger.info(f"🔗 Database host: {parsed.hostname}")
logger.info(f"🔗 Database port: {parsed.port}")

# Engine async
engine = create_async_engine(
    DATABASE_URL,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_MAX_OVERFLOW,
    echo=True if settings.APP_ENV == "development" else False
)

# Session factory
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


class Base(DeclarativeBase):
    """Base pour tous les modèles SQLAlchemy"""
    pass


async def get_db():
    """Dependency pour récupérer une session DB"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

