# Copy Map — Astroia Lunar

**Objectif**: Référencer où vit chaque string de l'app (i18n key → screen → composant).

---

## 📍 Mapping i18n → Code

| Screen | Route | i18n Keys | Component | Status |
|--------|-------|-----------|-----------|--------|
| **Welcome** | `/onboarding/welcome` | `onboarding.welcome.*` | `WelcomeScreen.tsx` | ✅ Ready |
| **Profile Setup** | `/onboarding/profile` | `onboarding.profile.*` | `ProfileSetup.tsx` | ✅ Ready |
| **Consent RGPD** | `/onboarding/consent` | `onboarding.consent.*` | `ConsentScreen.tsx` | ✅ Ready |
| **Disclaimer** | `/onboarding/disclaimer` | `onboarding.disclaimer.*` | `DisclaimerScreen.tsx` | ✅ Ready |
| **Onboarding Slides** | `/onboarding/slides` | `onboarding.slides.*` | `SlidesCarousel.tsx` | ✅ Ready |
| **Home** | `/` | `emptyStates.noCycles.*` | `index.tsx` | ✅ Migrated |
| **Settings** | `/settings` | `settings.*` | `settings.tsx` | ✅ Migrated |
| **Lunar Report** | `/lunar/report` | `errors.notFound.*` | `report.tsx` | ✅ Ready |
| **Timeline** | `/lunar-returns/timeline` | `errors.generic.*` | `timeline.tsx` | ✅ Ready |
| **VoC Screen** | `/void-of-course` | `emptyStates.noVoC.*` | `VoCScreen.tsx` | ✅ Ready |
| **Journal** (Phase 2) | `/journal` | `journal.*`, `paywalls.journal.*` | `JournalScreen.tsx` | 🔜 Phase 2 |
| **Error Screens** | N/A | `errors.*` | Global error boundaries | ✅ Ready |
| **Notifications** | N/A | `notifications.*` | `notificationScheduler.ts` | ✅ Migrated |

---

## ✅ Hardcoded Strings Migration Complete (2025-12-31)

All 6 hardcoded strings have been successfully migrated to i18n.

### 1. `apps/mobile/services/notificationScheduler.ts` ✅

**Line 113:** ✅ Migrated
```typescript
title: i18n.t('notifications.vocStart.title')
```

**Line 133:** ✅ Migrated
```typescript
title: i18n.t('notifications.vocEnd.title')
```

**Line 183:** ✅ Migrated
```typescript
title: i18n.t('notifications.newCycle.title')
```

---

### 2. `apps/mobile/app/settings.tsx` ✅

**Line 55:** ✅ Migrated
```typescript
t('settings.notifications.permissionRequired')
```

**Line 73:** ✅ Migrated
```typescript
t('settings.notifications.enabledSuccess')
```

---

### 3. `apps/mobile/app/index.tsx` ✅

**Line 466:** ✅ Migrated
```typescript
{t('emptyStates.noCycles.title')}
```

**Line 479:** ✅ Migrated
```typescript
{t('emptyStates.noCycles.cta')}
```

---

## ✅ Strings Déjà i18n-Ready

| Key | Usage | Location |
|-----|-------|----------|
| `onboarding.welcome.title` | Welcome screen title | `WelcomeScreen.tsx:42` |
| `settings.profile.name` | Profile name label | `settings.tsx:89` |
| `errors.network.body` | Network error message | Global error handler |
| `paywalls.journal.cta` | Journal unlock CTA | `JournalPaywall.tsx:67` |
| `common.back` | Back button text | All screens with navigation |

---

## 🔧 Actions Requises

1. ✅ **Installer i18n library**: `npm install i18next react-i18next` - DONE
2. ✅ **Créer configuration i18n**: `apps/mobile/i18n/index.ts` - DONE
3. ✅ **Brancher au root layout**: `apps/mobile/app/_layout.tsx` - DONE
4. ✅ **Migrer les 6 hardcoded strings** - DONE (actually migrated 7 strings)
5. ✅ **TypeScript compilation clean**: `npm run lint` passes - DONE
6. ⚠️ **Tester toutes les routes** pour vérifier que les traductions s'affichent correctement - PENDING QA

## 📦 Files Modified (PR Summary)

- `apps/mobile/package.json` - Added i18next + react-i18next dependencies + check:i18n script
- `apps/mobile/i18n/index.ts` - NEW: i18n configuration
- `apps/mobile/scripts/check-i18n.js` - NEW: i18n key parity validator
- `apps/mobile/app/_layout.tsx` - Import i18n init (side effect)
- `apps/mobile/services/notificationScheduler.ts` - Migrated 3 notification titles
- `apps/mobile/app/settings.tsx` - Migrated 2 Alert titles
- `apps/mobile/app/index.tsx` - Migrated 2 empty state strings (title + CTA)
- `docs/copy/COPY_MAP.md` - Updated migration status

---

## 🔧 i18n Validation Checks

### Automated Key Parity Check

A validation script ensures FR and EN translation files have matching keys:

```bash
# Run i18n key parity check
npm run check:i18n
```

**What it checks**:
- ✅ All FR keys exist in EN
- ✅ No extra keys in EN
- ✅ Flattened dot notation comparison (e.g., `settings.notifications.title`)

**Current status**: ✅ 105 keys in FR, 105 keys in EN (100% parity)

**Integration**: Add to CI/CD pipeline before deployment:
```bash
npm run lint && npm run check:i18n && npm run test
```

---

**Status**: 100% i18n-ready. All hardcoded strings migrated. TypeScript compilation clean. i18n key parity validated. Ready for QA testing.
