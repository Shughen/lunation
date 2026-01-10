# 🎨 Astro.IA Frontend - React + TypeScript

**Application web React moderne avec Vite, TypeScript, et Tailwind CSS**

---

## 📦 Technologies

- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool ultrarapide
- **Tailwind CSS** - Styling utility-first
- **Zustand** - State management
- **React Query** - Data fetching & caching
- **React Router** - Routing
- **Axios** - HTTP client
- **Lucide React** - Icons

---

## 🚀 Démarrage Rapide

```bash
# Installation
npm install

# Développement
npm run dev

# Build production
npm run build

# Preview production
npm run preview
```

---

## 📁 Structure

```
frontend/
├── src/
│   ├── components/     # Composants réutilisables
│   │   ├── ui/         # Composants UI de base
│   │   └── features/   # Composants métier
│   ├── pages/          # Pages/routes
│   ├── hooks/          # Custom hooks
│   ├── stores/         # Zustand stores
│   ├── services/       # API calls
│   ├── utils/          # Utilitaires
│   ├── types/          # Types TypeScript
│   ├── styles/         # CSS globaux
│   ├── App.tsx         # Composant racine
│   └── main.tsx        # Point d'entrée
├── public/             # Assets statiques
└── package.json
```

---

## 🔧 Scripts Disponibles

```bash
npm run dev          # Lance le serveur de développement
npm run build        # Build pour production
npm run preview      # Preview du build
npm run lint         # Linting avec ESLint
npm run format       # Formatage avec Prettier
npm run test         # Tests avec Vitest
npm run test:ui      # Tests avec UI
npm run test:coverage # Coverage des tests
```

---

## 🎨 Conventions de Code

### Composants

```tsx
// components/Button.tsx
interface ButtonProps {
  label: string;
  onClick: () => void;
  variant?: 'primary' | 'secondary';
}

export function Button({ label, onClick, variant = 'primary' }: ButtonProps) {
  return (
    <button
      onClick={onClick}
      className={`btn btn-${variant}`}
    >
      {label}
    </button>
  );
}
```

### Hooks Personnalisés

```tsx
// hooks/useUser.ts
import { useQuery } from '@tanstack/react-query';
import { userService } from '@/services/user';

export function useUser(userId: string) {
  return useQuery({
    queryKey: ['user', userId],
    queryFn: () => userService.getUser(userId),
  });
}
```

### Services API

```tsx
// services/user.ts
import { apiClient } from '@/lib/api';
import type { User } from '@shared/types';

export const userService = {
  async getUser(id: string): Promise<User> {
    const { data } = await apiClient.get(`/users/${id}`);
    return data;
  },
};
```

---

## 🌐 Variables d'Environnement

Créer `.env.local` :

```bash
VITE_API_URL=http://localhost:8000
VITE_ENABLE_ML=true
```

Usage :

```tsx
const apiUrl = import.meta.env.VITE_API_URL;
```

---

## 🎯 Bonnes Pratiques

1. **Typage strict** - Pas de `any`, utiliser `unknown` si nécessaire
2. **Composants purs** - Props immutables, pas de side-effects
3. **Custom hooks** - Logique réutilisable
4. **Error boundaries** - Gérer les erreurs gracieusement
5. **Lazy loading** - Code splitting pour les routes
6. **Memoization** - `useMemo`, `useCallback` quand nécessaire

---

## 🧪 Tests

```tsx
// Button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from './Button';

test('calls onClick when clicked', () => {
  const handleClick = vi.fn();
  render(<Button label="Click me" onClick={handleClick} />);
  
  fireEvent.click(screen.getByText('Click me'));
  expect(handleClick).toHaveBeenCalledTimes(1);
});
```

---

## 📚 Ressources

- [React Docs](https://react.dev)
- [Vite Docs](https://vitejs.dev)
- [Tailwind CSS](https://tailwindcss.com)
- [React Query](https://tanstack.com/query)
- [Zustand](https://zustand-demo.pmnd.rs/)

