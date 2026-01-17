# Astroia Lunar - Documentation API MVP

**Version:** 1.0.0
**Base URL:** `http://localhost:8000` (développement) | `https://api.astroia-lunar.com` (production)
**Date de création:** 2026-01-17

Cette documentation technique décrit tous les endpoints de l'API MVP d'Astroia Lunar. L'API est construite avec FastAPI et utilise PostgreSQL comme base de données.

---

## Table des matières

1. [Authentification](#1-authentification)
2. [Thème Natal](#2-thème-natal)
3. [Révolutions Lunaires](#3-révolutions-lunaires)
4. [VoC (Void of Course)](#4-voc-void-of-course)
5. [Transits](#5-transits)
6. [Journal](#6-journal)
7. [Codes de statut HTTP](#7-codes-de-statut-http)
8. [Mode développement](#8-mode-développement)

---

## 1. Authentification

L'API utilise l'authentification JWT (JSON Web Tokens) avec OAuth2. En mode développement, un système de bypass est disponible pour faciliter les tests.

### 1.1 POST /api/auth/login

Authentifie un utilisateur et retourne un token JWT.

**Headers:**
```
Content-Type: application/x-www-form-urlencoded
```

**Request Body (form-urlencoded):**
```
username=user@example.com&password=mypassword
```

**Response (200 OK):**
```json
{
  "access_token": "YOUR_JWT_TOKEN_HERE",
  "token_type": "bearer"
}
```

**Codes de statut:**
- `200` : Login réussi
- `401` : Email ou mot de passe incorrect

**Exemple curl:**
```bash
curl -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=mypassword"
```

---

### 1.2 GET /api/auth/me

Récupère les informations du profil de l'utilisateur authentifié.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
{
  "id": 1,
  "email": "user@example.com",
  "birth_date": "1990-05-15",
  "birth_time": "14:30",
  "birth_place_name": "Paris, France",
  "is_premium": false,
  "created_at": "2025-01-01T10:00:00Z"
}
```

**Codes de statut:**
- `200` : Profil récupéré
- `401` : Non authentifié

**Exemple curl:**
```bash
curl -X GET "http://localhost:8000/api/auth/me" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

### 1.3 POST /api/auth/logout

Déconnecte l'utilisateur (endpoint placeholder pour compatibilité future).

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
{
  "message": "Logged out successfully"
}
```

**Note:** En JWT stateless, la déconnexion est gérée côté client en supprimant le token. Cet endpoint est prévu pour les futures fonctionnalités (blacklist de tokens, etc.).

---

## 2. Thème Natal

Le thème natal est la carte astrologique calculée pour la date, l'heure et le lieu de naissance de l'utilisateur.

### 2.1 POST /api/natal-chart

Calcule et sauvegarde le thème natal de l'utilisateur. Si un thème existe déjà, il est écrasé.

**Headers:**
```
Authorization: Bearer <access_token>
Content-Type: application/json
```

**Request Body:**
```json
{
  "date": "1990-05-15",
  "time": "14:30",
  "latitude": 48.8566,
  "longitude": 2.3522,
  "place_name": "Paris, France",
  "timezone": "Europe/Paris"
}
```

**Champs:**
- `date` (string, requis) : Date de naissance au format YYYY-MM-DD
- `time` (string, optionnel) : Heure de naissance au format HH:MM (défaut: "12:00")
- `latitude` (float, requis) : Latitude du lieu de naissance
- `longitude` (float, requis) : Longitude du lieu de naissance
- `place_name` (string, requis) : Nom du lieu de naissance
- `timezone` (string, optionnel) : Fuseau horaire (défaut: auto-détecté)

**Response (201 Created):**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "sun_sign": "Taurus",
  "moon_sign": "Gemini",
  "ascendant": "Virgo",
  "planets": {
    "sun": {
      "sign": "Taurus",
      "degree": 24.5,
      "house": 9
    },
    "moon": {
      "sign": "Gemini",
      "degree": 12.3,
      "house": 10
    },
    "mercury": {
      "sign": "Taurus",
      "degree": 18.7,
      "house": 9
    }
  },
  "houses": {
    "1": {
      "sign": "Virgo",
      "degree": 15.2
    },
    "2": {
      "sign": "Libra",
      "degree": 10.8
    }
  },
  "aspects": [
    {
      "planet1": "sun",
      "planet2": "moon",
      "type": "sextile",
      "orb": 1.8
    }
  ]
}
```

**Codes de statut:**
- `201` : Thème créé avec succès
- `401` : Non authentifié
- `422` : Format de date/heure invalide
- `500` : Erreur serveur
- `502` : Erreur du provider RapidAPI
- `503` : Service RapidAPI indisponible

**Exemple curl:**
```bash
curl -X POST "http://localhost:8000/api/natal-chart" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "1990-05-15",
    "time": "14:30",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "place_name": "Paris, France",
    "timezone": "Europe/Paris"
  }'
```

---

### 2.2 GET /api/natal-chart

Récupère le thème natal de l'utilisateur authentifié.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "sun_sign": "Taurus",
  "moon_sign": "Gemini",
  "ascendant": "Virgo",
  "planets": { },
  "houses": { },
  "aspects": [ ]
}
```

**Codes de statut:**
- `200` : Thème récupéré
- `401` : Non authentifié
- `404` : Thème natal non calculé
- `500` : Erreur serveur

**Exemple curl:**
```bash
curl -X GET "http://localhost:8000/api/natal-chart" \
  -H "Authorization: Bearer <token>"
```

---

## 3. Révolutions Lunaires

Les révolutions lunaires représentent le retour de la Lune à sa position natale chaque mois (~27-28 jours).

### 3.1 POST /api/lunar-returns/generate

Génère 12 révolutions lunaires glissantes (rolling) à partir de maintenant. Nécessite un thème natal préalablement calculé.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (201 Created):**
```json
{
  "message": "12 révolution(s) lunaire(s) générée(s)",
  "mode": "rolling",
  "start_date": "2026-01-01T00:00:00+00:00",
  "end_date": "2027-01-01T00:00:00+00:00",
  "months_count": 12,
  "generated_count": 12,
  "correlation_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
}
```

**Codes de statut:**
- `201` : Révolutions générées avec succès
- `401` : Non authentifié
- `404` : Thème natal manquant
- `422` : Coordonnées de naissance manquantes
- `500` : Erreur serveur
- `503` : Clé API Ephemeris manquante

**Exemple curl:**
```bash
curl -X POST "http://localhost:8000/api/lunar-returns/generate" \
  -H "Authorization: Bearer <token>"
```

---

### 3.2 GET /api/lunar-returns/current

Récupère la révolution lunaire en cours (ou la prochaine si aucune n'est active).

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
{
  "id": 42,
  "month": "2026-01",
  "return_date": "2026-01-15T12:00:00+00:00",
  "lunar_ascendant": "Capricorn",
  "moon_house": 2,
  "moon_sign": "Taurus",
  "aspects": [
    {
      "planet1": "moon",
      "planet2": "venus",
      "type": "trine",
      "orb": 2.1
    }
  ],
  "interpretation": "Ce mois met l'accent sur la sécurité matérielle..."
}
```

**Codes de statut:**
- `200` : Révolution lunaire trouvée
- `401` : Non authentifié
- `404` : Aucune révolution lunaire disponible (ou retourne `null` en mode graceful)
- `500` : Erreur serveur

**Note:** Si aucune révolution lunaire n'existe, le endpoint peut déclencher une génération automatique (lazy loading) avec advisory lock PostgreSQL pour éviter les générations concurrentes.

**Exemple curl:**
```bash
curl -X GET "http://localhost:8000/api/lunar-returns/current" \
  -H "Authorization: Bearer <token>"
```

---

### 3.3 GET /api/lunar-returns/{id}

Récupère une révolution lunaire spécifique par son ID.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Path Parameters:**
- `id` (integer) : ID de la révolution lunaire

**Response (200 OK):** (même structure que `/current`)

**Codes de statut:**
- `200` : Révolution trouvée
- `401` : Non authentifié
- `404` : Révolution lunaire introuvable
- `500` : Erreur serveur

**Exemple curl:**
```bash
curl -X GET "http://localhost:8000/api/lunar-returns/42" \
  -H "Authorization: Bearer <token>"
```

---

### 3.4 POST /api/lunar/return/report

Génère un rapport mensuel de révolution lunaire (Luna Pack P1).

**Headers:**
```
Authorization: Bearer <access_token>
Content-Type: application/json
```

**Request Body:**
```json
{
  "month": "2026-01",
  "date": "2026-01-15",
  "time": "14:30",
  "latitude": 48.8566,
  "longitude": 2.3522,
  "timezone": "Europe/Paris",
  "birth_date": "1990-05-15",
  "birth_time": "14:30"
}
```

**Response (200 OK):**
```json
{
  "provider": "rapidapi",
  "kind": "lunar_return_report",
  "data": {
    "moon": {
      "sign": "Taurus",
      "house": 2,
      "degree": 12.3
    },
    "ascendant": {
      "sign": "Capricorn",
      "degree": 5.7
    },
    "interpretation": "Ce mois met l'accent sur la sécurité matérielle et les finances personnelles. La Lune en Taurus en Maison 2 suggère une période favorable pour consolider vos ressources..."
  },
  "cached": false
}
```

**Codes de statut:**
- `200` : Rapport généré
- `401` : Non authentifié
- `422` : Payload invalide
- `500` : Erreur serveur
- `502` : Erreur provider RapidAPI

**Exemple curl:**
```bash
curl -X POST "http://localhost:8000/api/lunar/return/report" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "month": "2026-01",
    "date": "2026-01-15",
    "time": "14:30",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris",
    "birth_date": "1990-05-15",
    "birth_time": "14:30"
  }'
```

---

### 3.5 GET /api/lunar-returns/current/report

Récupère le rapport mensuel de la révolution lunaire en cours (format v4 avec climat général, axes dominants, aspects majeurs).

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
{
  "month": "2026-01",
  "return_date": "2026-01-15T12:00:00+00:00",
  "general_climate": "Ce mois met l'accent sur la sécurité matérielle et les finances personnelles. La Lune en Taurus en Maison 2 suggère une période favorable pour consolider vos ressources.",
  "dominant_axes": [
    {
      "axis": "Finances et valeurs",
      "interpretation": "Focus sur la stabilité financière et matérielle."
    }
  ],
  "major_aspects": [
    {
      "aspect": "Lune trigone Vénus",
      "interpretation": "Harmonie dans les relations affectives et financières.",
      "orb": 2.1
    }
  ]
}
```

**Codes de statut:**
- `200` : Rapport généré
- `401` : Non authentifié
- `404` : Aucune révolution lunaire pour le mois en cours
- `500` : Erreur serveur

**Exemple curl:**
```bash
curl -X GET "http://localhost:8000/api/lunar-returns/current/report" \
  -H "Authorization: Bearer <token>"
```

---

## 4. VoC (Void of Course)

Le Void of Course (VoC) représente la période où la Lune ne fait plus d'aspects majeurs avant de changer de signe. Considérée comme peu propice aux initiatives importantes.

### 4.1 GET /api/lunar/voc/current

Vérifie s'il y a une fenêtre VoC active actuellement. Utilise un cache en mémoire (TTL: 1 minute) pour optimiser les performances.

**Response (200 OK):**
```json
{
  "is_voc": true,
  "current_window": {
    "start_at": "2026-01-17T10:30:00+00:00",
    "end_at": "2026-01-17T14:45:00+00:00",
    "moon_sign": "Gemini",
    "duration_hours": 4.25
  }
}
```

**Si aucune fenêtre active:**
```json
{
  "is_voc": false,
  "current_window": null
}
```

**Codes de statut:**
- `200` : Statut VoC récupéré
- `500` : Erreur serveur

**Exemple curl:**
```bash
curl -X GET "http://localhost:8000/api/lunar/voc/current"
```

---

### 4.2 GET /api/lunar/voc/status

Endpoint unifié pour l'écran VoC MVP (Phase 1.3). Retourne le statut complet : fenêtre active, prochaine fenêtre et fenêtres à venir.

**Response (200 OK):**
```json
{
  "now": {
    "start_at": "2026-01-17T10:30:00+00:00",
    "end_at": "2026-01-17T14:45:00+00:00",
    "moon_sign": "Gemini",
    "duration_hours": 4.25
  },
  "next": {
    "start_at": "2026-01-19T08:15:00+00:00",
    "end_at": "2026-01-19T11:30:00+00:00",
    "moon_sign": "Cancer",
    "duration_hours": 3.25
  },
  "upcoming": [
    {
      "start_at": "2026-01-21T15:00:00+00:00",
      "end_at": "2026-01-21T18:45:00+00:00",
      "moon_sign": "Leo",
      "duration_hours": 3.75
    }
  ]
}
```

**Champs:**
- `now` : Fenêtre VoC active maintenant (ou `null` si aucune)
- `next` : Prochaine fenêtre VoC à venir (ou `null`)
- `upcoming` : Liste des 2-3 prochaines fenêtres (24-48h)

**Codes de statut:**
- `200` : Statut récupéré
- `500` : Erreur serveur

**Note:** Cache en mémoire (TTL: 2 minutes), retry logic (3 retries avec exponential backoff), requêtes DB parallélisées.

**Exemple curl:**
```bash
curl -X GET "http://localhost:8000/api/lunar/voc/status"
```

---

### 4.3 POST /api/lunar/voc

Calcule le statut Void of Course pour une date/heure/lieu donnés. Sauvegarde automatiquement les fenêtres VoC en DB.

**Headers:**
```
Content-Type: application/json
```

**Request Body:**
```json
{
  "date": "2026-01-17",
  "time": "12:00",
  "latitude": 48.8566,
  "longitude": 2.3522,
  "timezone": "Europe/Paris"
}
```

**Response (200 OK):**
```json
{
  "provider": "rapidapi",
  "kind": "void_of_course",
  "data": {
    "is_void": true,
    "void_of_course": {
      "start": "2026-01-17T10:30:00+00:00",
      "end": "2026-01-17T14:45:00+00:00"
    },
    "moon_sign": "Gemini",
    "last_aspect": {
      "planet": "Mars",
      "type": "square",
      "time": "2026-01-17T10:15:00+00:00"
    }
  },
  "cached": false
}
```

**Codes de statut:**
- `200` : Statut calculé
- `422` : Payload invalide
- `500` : Erreur serveur
- `502` : Erreur provider RapidAPI

**Exemple curl:**
```bash
curl -X POST "http://localhost:8000/api/lunar/voc" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2026-01-17",
    "time": "12:00",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris"
  }'
```

---

**Note:** Le endpoint `GET /voc/windows` mentionné dans la tâche n'existe pas dans le code actuel. Les fenêtres VoC sont accessibles via `/voc/status` qui retourne `now`, `next` et `upcoming`.

---

## 5. Transits

Les transits représentent les aspects formés par les planètes en transit avec les positions natales ou de révolution lunaire.

### 5.1 POST /api/transits/natal

Calcule les transits planétaires actuels croisés avec le thème natal.

**Headers:**
```
Content-Type: application/json
```

**Query Parameters:**
- `major_only` (boolean, optionnel) : Si `true`, ne retourne que les aspects majeurs (conjonction, opposition, carré, trigone). Défaut: `false`

**Request Body:**
```json
{
  "birth_date": "1990-05-15",
  "birth_time": "14:30",
  "birth_latitude": 48.8566,
  "birth_longitude": 2.3522,
  "birth_timezone": "Europe/Paris",
  "transit_date": "2026-01-17",
  "transit_time": "12:00",
  "orb": 5.0,
  "user_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

**Champs:**
- `birth_date` (string, requis) : Date de naissance (YYYY-MM-DD)
- `birth_time` (string, requis) : Heure de naissance (HH:MM)
- `birth_latitude` (float, requis) : Latitude de naissance
- `birth_longitude` (float, requis) : Longitude de naissance
- `birth_timezone` (string, optionnel) : Fuseau horaire (défaut: "Europe/Paris")
- `transit_date` (string, requis) : Date du transit (YYYY-MM-DD)
- `transit_time` (string, optionnel) : Heure du transit (HH:MM)
- `orb` (float, optionnel) : Orbe des aspects en degrés (défaut: 5.0)
- `user_id` (string UUID, optionnel) : ID utilisateur pour sauvegarde en DB

**Response (200 OK):**
```json
{
  "provider": "rapidapi",
  "kind": "natal_transits",
  "data": {
    "aspects": [
      {
        "transit_planet": "Jupiter",
        "natal_planet": "Sun",
        "aspect": "trine",
        "orb": 1.2,
        "exact_date": "2026-01-18T14:30:00+00:00"
      },
      {
        "transit_planet": "Saturn",
        "natal_planet": "Moon",
        "aspect": "square",
        "orb": 3.5,
        "exact_date": "2026-01-20T08:00:00+00:00"
      }
    ]
  },
  "insights": {
    "insights": [
      "Jupiter forme un trigone avec votre Soleil natal - période d'expansion et d'opportunités",
      "Saturne forme un carré avec votre Lune natale - période de restructuration émotionnelle"
    ],
    "major_aspects": [
      {
        "transit_planet": "Jupiter",
        "natal_planet": "Sun",
        "aspect": "trine",
        "orb": 1.2,
        "interpretation": "Période favorable pour les projets d'expansion"
      }
    ],
    "energy_level": "medium",
    "themes": ["expansion", "restructuration", "opportunités"]
  },
  "cached": false
}
```

**Codes de statut:**
- `200` : Transits calculés
- `422` : Payload invalide
- `500` : Erreur serveur
- `502` : Erreur provider RapidAPI

**Exemple curl:**
```bash
curl -X POST "http://localhost:8000/api/transits/natal?major_only=true" \
  -H "Content-Type: application/json" \
  -d '{
    "birth_date": "1990-05-15",
    "birth_time": "14:30",
    "birth_latitude": 48.8566,
    "birth_longitude": 2.3522,
    "transit_date": "2026-01-17"
  }'
```

---

### 5.2 POST /api/transits/lunar_return

Calcule les transits planétaires sur une révolution lunaire.

**Headers:**
```
Content-Type: application/json
```

**Query Parameters:**
- `major_only` (boolean, optionnel) : Si `true`, ne retourne que les aspects majeurs. Défaut: `false`

**Request Body:**
```json
{
  "birth_date": "1990-05-15",
  "birth_time": "14:30",
  "birth_latitude": 48.8566,
  "birth_longitude": 2.3522,
  "birth_timezone": "Europe/Paris",
  "lunar_return_date": "2026-01-15",
  "transit_date": "2026-01-17",
  "orb": 5.0,
  "user_id": "550e8400-e29b-41d4-a716-446655440000",
  "month": "2026-01"
}
```

**Response (200 OK):** (structure similaire à `/natal`)

**Codes de statut:**
- `200` : Transits calculés
- `422` : Payload invalide
- `500` : Erreur serveur
- `502` : Erreur provider RapidAPI

**Exemple curl:**
```bash
curl -X POST "http://localhost:8000/api/transits/lunar_return?major_only=true" \
  -H "Content-Type: application/json" \
  -d '{
    "birth_date": "1990-05-15",
    "birth_time": "14:30",
    "birth_latitude": 48.8566,
    "birth_longitude": 2.3522,
    "lunar_return_date": "2026-01-15",
    "transit_date": "2026-01-17",
    "month": "2026-01"
  }'
```

---

### 5.3 GET /api/transits/overview/{user_id}/{month}

Récupère la vue d'ensemble des transits pour un utilisateur et un mois donnés (données en cache).

**Headers:**
```
Authorization: Bearer <access_token>
X-Dev-User-Id: <uuid> (optionnel, mode DEV_AUTH_BYPASS uniquement)
```

**Path Parameters:**
- `user_id` (UUID) : ID de l'utilisateur
- `month` (string) : Mois au format YYYY-MM

**Query Parameters:**
- `major_only` (boolean, optionnel) : Si `true`, filtre uniquement les aspects majeurs. Défaut: `false`

**Response (200 OK):**
```json
{
  "id": 1,
  "user_id": "550e8400-e29b-41d4-a716-446655440000",
  "month": "2026-01",
  "overview": {
    "natal_transits": {
      "aspects": [ ]
    },
    "insights": {
      "insights": [ ],
      "major_aspects": [ ],
      "energy_level": "medium",
      "themes": [ ]
    },
    "last_updated": "2026-01-17T12:00:00Z"
  },
  "created_at": "2026-01-15T10:00:00Z"
}
```

**Codes de statut:**
- `200` : Overview récupéré
- `401` : Non authentifié
- `404` : Aucun transits overview trouvé
- `500` : Erreur serveur

**Note:** En mode `DEV_AUTH_BYPASS`, l'UUID du header `X-Dev-User-Id` est utilisé au lieu de celui de l'URL.

**Exemple curl:**
```bash
curl -X GET "http://localhost:8000/api/transits/overview/550e8400-e29b-41d4-a716-446655440000/2026-01?major_only=true" \
  -H "Authorization: Bearer <token>"
```

---

## 6. Journal

Le journal permet aux utilisateurs de noter quotidiennement leur humeur et leurs observations.

### 6.1 POST /api/journal/entry

Crée ou met à jour une entrée de journal. Une seule entrée par jour par utilisateur.

**Headers:**
```
Authorization: Bearer <access_token>
Content-Type: application/json
```

**Request Body:**
```json
{
  "date": "2026-01-17",
  "mood": "calm",
  "note": "Journée productive, sentiment de sérénité. Bonne concentration sur mes projets.",
  "month": "2026-01"
}
```

**Champs:**
- `date` (string, requis) : Date de l'entrée (YYYY-MM-DD)
- `mood` (string, optionnel) : Humeur parmi: `calm`, `excited`, `anxious`, `sad`, `neutral`, etc.
- `note` (string, optionnel) : Note libre de l'utilisateur
- `month` (string, optionnel) : Mois lunaire associé (format YYYY-MM)

**Response (201 Created):**
```json
{
  "id": 123,
  "user_id": 1,
  "date": "2026-01-17",
  "mood": "calm",
  "note": "Journée productive, sentiment de sérénité. Bonne concentration sur mes projets.",
  "month": "2026-01",
  "created_at": "2026-01-17T12:00:00Z",
  "updated_at": "2026-01-17T12:00:00Z"
}
```

**Codes de statut:**
- `201` : Entrée créée
- `200` : Entrée mise à jour (si elle existait déjà pour cette date)
- `401` : Non authentifié
- `500` : Erreur serveur

**Exemple curl:**
```bash
curl -X POST "http://localhost:8000/api/journal/entry" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2026-01-17",
    "mood": "calm",
    "note": "Journée productive.",
    "month": "2026-01"
  }'
```

---

### 6.2 GET /api/journal/entries

Récupère les entrées de journal de l'utilisateur avec filtrage et pagination.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `month` (string, optionnel) : Filtrer par mois lunaire (format YYYY-MM)
- `year` (integer, optionnel) : Filtrer par année
- `limit` (integer, optionnel) : Nombre d'entrées à retourner (défaut: 100)
- `offset` (integer, optionnel) : Offset pour pagination (défaut: 0)

**Response (200 OK):**
```json
{
  "entries": [
    {
      "id": 123,
      "user_id": 1,
      "date": "2026-01-17",
      "mood": "calm",
      "note": "Journée productive.",
      "month": "2026-01",
      "created_at": "2026-01-17T12:00:00Z",
      "updated_at": "2026-01-17T12:00:00Z"
    },
    {
      "id": 122,
      "user_id": 1,
      "date": "2026-01-16",
      "mood": "excited",
      "note": "Nouveau projet lancé!",
      "month": "2026-01",
      "created_at": "2026-01-16T10:00:00Z",
      "updated_at": null
    }
  ],
  "total": 2,
  "month": "2026-01"
}
```

**Codes de statut:**
- `200` : Entrées récupérées
- `401` : Non authentifié
- `500` : Erreur serveur

**Exemple curl:**
```bash
curl -X GET "http://localhost:8000/api/journal/entries?month=2026-01&limit=10" \
  -H "Authorization: Bearer <token>"
```

---

### 6.3 GET /api/journal/today

Récupère l'entrée de journal du jour (si elle existe).

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
{
  "id": 123,
  "user_id": 1,
  "date": "2026-01-17",
  "mood": "calm",
  "note": "Journée productive.",
  "month": "2026-01",
  "created_at": "2026-01-17T12:00:00Z",
  "updated_at": "2026-01-17T12:00:00Z"
}
```

**Si aucune entrée:**
```json
null
```

**Codes de statut:**
- `200` : Entrée trouvée (ou `null`)
- `401` : Non authentifié
- `500` : Erreur serveur

**Exemple curl:**
```bash
curl -X GET "http://localhost:8000/api/journal/today" \
  -H "Authorization: Bearer <token>"
```

---

### 6.4 DELETE /api/journal/entry/{entry_id}

Supprime une entrée de journal. Seul le propriétaire peut supprimer son entrée.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Path Parameters:**
- `entry_id` (integer) : ID de l'entrée à supprimer

**Response (204 No Content):**
(Pas de corps de réponse)

**Codes de statut:**
- `204` : Entrée supprimée
- `401` : Non authentifié
- `404` : Entrée non trouvée
- `500` : Erreur serveur

**Exemple curl:**
```bash
curl -X DELETE "http://localhost:8000/api/journal/entry/123" \
  -H "Authorization: Bearer <token>"
```

---

## 7. Codes de statut HTTP

Voici un récapitulatif des codes de statut utilisés par l'API :

| Code | Signification | Description |
|------|---------------|-------------|
| `200` | OK | Requête réussie |
| `201` | Created | Ressource créée avec succès |
| `204` | No Content | Suppression réussie (pas de corps de réponse) |
| `400` | Bad Request | Requête invalide (paramètres manquants ou invalides) |
| `401` | Unauthorized | Authentification manquante ou invalide |
| `404` | Not Found | Ressource non trouvée |
| `409` | Conflict | Conflit (ex: thème natal requis avant génération de révolutions lunaires) |
| `422` | Unprocessable Entity | Format de données invalide |
| `500` | Internal Server Error | Erreur serveur interne |
| `502` | Bad Gateway | Erreur du provider externe (RapidAPI) |
| `503` | Service Unavailable | Service externe indisponible (ex: clé API manquante) |

---

## 8. Mode développement

L'API offre un mode développement (`DEV_AUTH_BYPASS`) qui permet de contourner l'authentification JWT pour faciliter les tests.

### 8.1 Configuration

Pour activer le mode développement, configurer les variables d'environnement suivantes :

```bash
APP_ENV=development
DEV_AUTH_BYPASS=1
```

### 8.2 Headers DEV

En mode `DEV_AUTH_BYPASS`, deux headers sont disponibles :

**X-Dev-User-Id** : Spécifie l'ID utilisateur à utiliser (peut être un integer ou un UUID)
```bash
curl -X GET "http://localhost:8000/api/lunar-returns/current" \
  -H "X-Dev-User-Id: 1"
```

**X-Dev-External-Id** : Spécifie l'ID externe (UUID ou email) à utiliser
```bash
curl -X GET "http://localhost:8000/api/lunar-returns/current" \
  -H "X-Dev-External-Id: dev-remi"
```

### 8.3 Utilisateur par défaut

Si aucun header n'est fourni, l'API utilise automatiquement l'utilisateur `dev@local.dev` (créé automatiquement si inexistant).

### 8.4 Mocks et tests

Plusieurs variables d'environnement permettent de mocker les providers externes :

```bash
DEV_MOCK_NATAL=1           # Mock calculs de thème natal
DEV_MOCK_RAPIDAPI=1        # Mock RapidAPI
DEV_MOCK_EPHEMERIS=1       # Mock Swiss Ephemeris
```

**Note importante :** Le mode `DEV_AUTH_BYPASS` est **uniquement disponible en développement** (`APP_ENV=development`). En production, l'authentification JWT est obligatoire.

### 8.5 Routes DEV spéciales

**POST /api/lunar-returns/dev/purge** : Purge toutes les révolutions lunaires de l'utilisateur courant (nécessite `ALLOW_DEV_PURGE=1`).

```bash
export DEV_AUTH_BYPASS=1
export ALLOW_DEV_PURGE=1

curl -X POST "http://localhost:8000/api/lunar-returns/dev/purge" \
  -H "X-Dev-External-Id: dev-remi"
```

---

## Notes techniques

### Authentification

- L'API utilise JWT (JSON Web Tokens) avec OAuth2
- Les tokens expirent après `ACCESS_TOKEN_EXPIRE_MINUTES` (défini dans la config)
- En mode développement, `DEV_AUTH_BYPASS` permet de contourner l'authentification

### Base de données

- PostgreSQL avec SQLAlchemy async
- Migrations gérées par Alembic
- Schema sanity check au démarrage (fail-fast en dev)

### Providers externes

- **RapidAPI** : Calculs astrologiques (thème natal, révolutions lunaires, transits)
- **Swiss Ephemeris** : Positions planétaires complémentaires
- Les erreurs de provider sont loggées avec des `correlation_id` pour le debugging

### Cache et optimisations

- Cache en mémoire pour `/voc/current` (TTL: 1 min)
- Cache en mémoire pour `/voc/status` (TTL: 2 min)
- Retry logic pour requêtes DB (3 retries avec exponential backoff)
- Advisory locks PostgreSQL pour éviter les générations concurrentes

### Logs

Tous les endpoints loggent leurs opérations avec :
- `correlation_id` pour tracer les requêtes
- Logs INFO pour les opérations réussies
- Logs ERROR/WARNING pour les erreurs avec `exc_info=True`

---

**Fin de la documentation API MVP**

Pour toute question ou problème, consulter les logs du serveur avec le `correlation_id` fourni dans les réponses d'erreur.
