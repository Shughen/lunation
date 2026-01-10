# 🔄 Shared - Utilitaires Communs

**Types, constantes et fonctions partagés entre Frontend et Backend**

---

## 📁 Structure

```
shared/
├── types/              # Types TypeScript/Python
│   ├── user.ts
│   ├── astro.ts
│   └── api.ts
├── constants/          # Constantes
│   ├── zodiac.ts
│   ├── api_codes.ts
│   └── config.ts
├── utils/              # Fonctions utilitaires
│   ├── date.ts
│   ├── validation.ts
│   └── astro.ts
└── README.md
```

---

## 🎯 Objectif

Ce dossier contient tout ce qui peut être partagé entre le frontend et le backend pour :

1. **Éviter la duplication de code**
2. **Garantir la cohérence** (types, constantes)
3. **Centraliser la logique métier** commune

---

## 📦 Utilisation

### Frontend (TypeScript)

```typescript
// Import depuis @shared (alias configuré dans vite.config.ts)
import { ZodiacSign } from '@shared/types/astro';
import { ZODIAC_SIGNS } from '@shared/constants/zodiac';
import { calculateAge } from '@shared/utils/date';
```

### Backend (Python)

```python
# Import Python (via dataclasses équivalentes)
from shared.types.astro import ZodiacSign
from shared.constants.zodiac import ZODIAC_SIGNS
from shared.utils.date import calculate_age
```

---

## ✅ Bonnes Pratiques

### 1. Types Partagés

Créer des types cohérents entre TS et Python :

**TypeScript (`types/user.ts`):**
```typescript
export interface User {
  id: number;
  email: string;
  fullName?: string;
  createdAt: Date;
}
```

**Python (`types/user.py`):**
```python
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class User:
    id: int
    email: str
    full_name: Optional[str] = None
    created_at: datetime = None
```

### 2. Constantes

```typescript
// constants/zodiac.ts
export const ZODIAC_SIGNS = [
  { id: 1, name: 'Bélier', emoji: '♈' },
  { id: 2, name: 'Taureau', emoji: '♉' },
  // ...
] as const;
```

### 3. Utilitaires

```typescript
// utils/date.ts
export function calculateAge(birthDate: Date): number {
  const today = new Date();
  const diff = today.getTime() - birthDate.getTime();
  return Math.floor(diff / (1000 * 60 * 60 * 24 * 365.25));
}
```

---

## 🔧 Configuration

### Frontend (Vite)

Déjà configuré dans `frontend/vite.config.ts` :

```typescript
resolve: {
  alias: {
    '@shared': path.resolve(__dirname, '../shared'),
  },
}
```

### Backend (Python)

Ajouter `../shared` au `PYTHONPATH` ou créer un symlink :

```bash
cd backend
ln -s ../shared shared
```

---

## 📚 Exemples

### Validation Email

**TypeScript :**
```typescript
// shared/utils/validation.ts
export function isValidEmail(email: string): boolean {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}
```

**Python :**
```python
# shared/utils/validation.py
import re

def is_valid_email(email: str) -> bool:
    return bool(re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email))
```

### Codes d'Erreur API

```typescript
// shared/constants/api_codes.ts
export const API_CODES = {
  SUCCESS: 200,
  CREATED: 201,
  BAD_REQUEST: 400,
  UNAUTHORIZED: 401,
  NOT_FOUND: 404,
  SERVER_ERROR: 500,
} as const;
```

---

## 🎯 À Faire

- [ ] Ajouter plus de types astrologiques
- [ ] Créer utils de calcul astrologique
- [ ] Documenter toutes les constantes
- [ ] Ajouter tests pour les utilitaires

---

**Code partagé = Code cohérent ! 🔄**

