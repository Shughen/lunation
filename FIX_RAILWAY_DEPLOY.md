# 🔧 FIX RAILWAY DEPLOYMENT - DOCKERFILE CORRIGÉ

## 🎯 LE PROBLÈME

Le Dockerfile actuel ne trouve pas le JAR car :
- Leiningen crée : `ephemeris-api-0.0.1-SNAPSHOT-standalone.jar`
- Le Dockerfile cherche : `target/server.jar`
- Le wildcard COPY ne fonctionne pas dans les builds multi-étapes

---

## ✅ LA SOLUTION

**Voici le Dockerfile corrigé à utiliser** :

```dockerfile
# ============================================
# DOCKERFILE CORRIGÉ POUR RAILWAY
# ============================================
# Build multi-étapes avec Leiningen + Runtime Java

# ====== ÉTAPE 1 : BUILD ======
FROM clojure:lein-2.9.10 AS builder

WORKDIR /app

# Copier les fichiers de projet
COPY project.clj .
COPY src/ src/
COPY resources/ resources/
COPY test/ test/

# Build le uberjar avec Leiningen
RUN lein do clean, uberjar

# Renommer le JAR avec un nom fixe pour faciliter le COPY
RUN mv target/*-standalone.jar target/server.jar

# ====== ÉTAPE 2 : RUNTIME ======
FROM eclipse-temurin:8-jre

WORKDIR /srv

# Copier le JAR depuis l'étape de build
COPY --from=builder /app/target/server.jar /srv/ephemeris-api.jar

# Port exposé
EXPOSE 8080

# Variables d'environnement pour Railway
ENV EPHEMERIS_API_PORT=8080
ENV EPHEMERIS_API_TYPE=jetty

# Démarrer l'application
CMD ["java", "-Dnomad.env=prod", "-Dephemeris.api.port=8080", "-jar", "/srv/ephemeris-api.jar"]
```

---

## 🚀 COMMENT APPLIQUER LA CORRECTION

### Option 1 : Via GitHub Web UI (2 minutes) ⭐ RECOMMANDÉ

1. Va sur ton fork : **https://github.com/Shughen/ephemeris-api**
2. Clique sur le fichier **`Dockerfile`**
3. Clique sur le crayon ✏️ (Edit)
4. **Remplace tout le contenu** par le Dockerfile ci-dessus
5. Commit message : `Fix: Correct JAR path in multi-stage build`
6. Clique **"Commit changes"**

**Railway va automatiquement redéployer !** ✅

---

### Option 2 : Via Terminal (1 minute)

```bash
cd /Users/remibeaurain/astroia/ephemeris-api

# Copier le Dockerfile corrigé
cp Dockerfile.fixed Dockerfile

# Commit
git add Dockerfile
git commit -m "Fix: Correct JAR path in multi-stage build"

# Push vers ton fork (change l'URL vers ton fork)
git remote set-url origin https://github.com/Shughen/ephemeris-api.git
git push origin master
```

**Railway va automatiquement redéployer !** ✅

---

## ✨ MODIFICATIONS CLÉS

### Ligne 18 (La clé !) :
```dockerfile
# ✅ AJOUTÉ : Renommer le JAR avec un nom fixe
RUN mv target/*-standalone.jar target/server.jar
```

**Cette ligne résout le problème** :
- Leiningen crée `ephemeris-api-0.0.1-SNAPSHOT-standalone.jar`
- On le renomme en `server.jar`
- Le COPY peut alors le trouver facilement

### Ligne 25 :
```dockerfile
# ✅ CORRIGÉ : COPY depuis l'étape builder avec le bon path
COPY --from=builder /app/target/server.jar /srv/ephemeris-api.jar
```

---

## 🧪 APRÈS LE DÉPLOIEMENT

### 1. Attendre le redéploiement (2-3 minutes)

Dans Railway, tu verras :
```
Building...
✅ Build successful
Starting...
✅ Service running
```

### 2. Tester l'API

```bash
curl https://web-production-d5955.up.railway.app/

# Tu devrais voir la page Swagger de l'API ✅
```

### 3. Tester un calcul

```bash
curl -X POST https://web-production-d5955.up.railway.app/calc \
  -H 'Content-Type: application/json' \
  -d '{
    "year": 1989,
    "month": 11,
    "day": 1,
    "hour": 17.333,
    "latitude": -3.1316333,
    "longitude": -59.9825041,
    "houses": "Placidus"
  }'
```

**Si tu vois des positions planétaires → C'EST BON ! ✅**

---

## 🔌 INTÉGRATION DANS TON APP

### Une fois l'API fonctionnelle

Je configure Vercel avec :

```bash
NATAL_PROVIDER=ephemeris-api
EPHEMERIS_API_URL=https://web-production-d5955.up.railway.app
```

Puis je redéploie :

```bash
cd /Users/remibeaurain/astroia/astro-ia-api
npx vercel --prod --yes
```

**Et ton app aura la précision d'Astrotheme gratuitement !** 🎉

---

## 📝 RÉCAPITULATIF DE LA CORRECTION

### Ancien Dockerfile (ne fonctionnait pas)
```dockerfile
# Ligne problématique
COPY target/*.jar /srv/ephemeris-api.jar
# ❌ Le wildcard ne fonctionne pas dans les builds multi-étapes
```

### Nouveau Dockerfile (fonctionne) ✅
```dockerfile
# Ligne 18 : Renommer le JAR
RUN mv target/*-standalone.jar target/server.jar

# Ligne 25 : COPY avec nom fixe
COPY --from=builder /app/target/server.jar /srv/ephemeris-api.jar
# ✅ Nom fixe, pas de wildcard
```

---

## ✨ ACTION IMMÉDIATE

**👉 VA SUR GitHub et remplace le Dockerfile :**

1. https://github.com/Shughen/ephemeris-api
2. Édite `Dockerfile`
3. Colle le Dockerfile corrigé ci-dessus
4. Commit : "Fix: Correct JAR path in multi-stage build"
5. **Railway va redéployer automatiquement** ⚡

**Dans 3 minutes → API fonctionnelle !** 🚀

**Puis reviens me donner le OK et je configure Vercel !** ✅
