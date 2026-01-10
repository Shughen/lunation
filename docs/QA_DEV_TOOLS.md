# QA Dev Tools - Notifications & Deep Links Testing

**Status**: DEV ONLY (automatically disabled in production builds)

## 🎯 Purpose

Quick testing helper for QA validation of:
- Notification scheduling (VoC start, VoC end, New cycle)
- i18n interpolation in notification content
- Deep link navigation from notifications

## 📍 Location

The QA tools are visible in **Settings screen** (bottom section), **only in DEV mode** (`__DEV__`).

## 🔧 How to Use (2 minutes test)

### 1. Access DEV QA Section

```bash
# Run app in dev mode
cd apps/mobile
npm start
```

1. Navigate to **Settings** screen (⚙️)
2. Scroll to bottom
3. You should see a section with dashed red border: **"🔧 DEV QA Tools"**

### 2. Trigger QA Notifications

1. Tap **"🔔 Trigger QA Notifications"** button
2. If permission not granted, allow notifications in device settings
3. Alert will confirm: "3 test notifications scheduled"

**Scheduled notifications**:
- **T+15s**: VoC Start → Deep link to `/lunar/voc`
- **T+30s**: VoC End → Deep link to `/lunar/voc`
- **T+45s**: New Cycle → Deep link to `/lunar/report`

### 3. Test Deep Links

1. Wait for notifications to appear (15s, 30s, 45s)
2. **Tap each notification** to test deep link navigation
3. Verify app opens to correct screen:
   - VoC notifications → Void of Course screen
   - New Cycle notification → Lunar Report screen

### 4. Verify i18n Interpolation

Check notification content has **no unresolved placeholders**:
- ❌ BAD: "La Lune entre en VoC jusqu'à {endTime}"
- ✅ GOOD: "La Lune entre en VoC jusqu'à 18:30"

**Test data used**:
- `endTime`: "18:30"
- `month`: "Janvier"
- `sign`: "Taureau"
- `ascendant`: "Balance"

### 5. Cancel All Notifications

Tap **"🚫 Cancel All Notifications"** to clean up scheduled notifications.

## 🚨 Important Notes

### DEV ONLY Enforcement

The component is **completely removed in production**:

```typescript
// Export null in production, component in dev
export default __DEV__ ? DevQASection : null;
```

**Verification**:
- In production builds, the DEV QA section will **not appear** in Settings
- No performance impact, no bundle size increase
- Import statement returns `null` in production

### Permissions

If notification permissions are not granted:
- Alert will show: "Permission Required"
- Button to open device Settings
- No crash, graceful degradation

### Console Logs

All QA actions are logged to console with `[DEV QA]` prefix:
```
[DEV QA] Canceled existing notifications
[DEV QA] Scheduled VoC Start notification (T+15s)
[DEV QA] Scheduled VoC End notification (T+30s)
[DEV QA] Scheduled New Cycle notification (T+45s)
```

## 📦 Implementation Details

### Files Modified

- `apps/mobile/components/DevQASection.tsx` - NEW: QA component (DEV only)
- `apps/mobile/app/settings.tsx` - Added conditional import + render

### Dependencies Reused

- `services/notificationScheduler.ts`:
  - `requestNotificationPermissions()`
  - `cancelAllNotifications()`
- `i18n/index.ts`:
  - `i18n.t()` for all notification strings
- `expo-notifications`:
  - `scheduleNotificationAsync()`
  - `SchedulableTriggerInputTypes.TIME_INTERVAL`

### No Duplication

All notification logic reuses existing scheduler functions and i18n keys. No hardcoded strings.

## ✅ QA Checklist

- [ ] DEV QA section visible in Settings (DEV mode only)
- [ ] "Trigger QA Notifications" button functional
- [ ] 3 notifications scheduled with correct timing (15s, 30s, 45s)
- [ ] Notification titles use i18n (no hardcoded strings)
- [ ] Notification bodies have interpolated values (no "{endTime}" placeholders)
- [ ] Deep link to `/lunar/voc` works (VoC notifications)
- [ ] Deep link to `/lunar/report` works (New Cycle notification)
- [ ] "Cancel All Notifications" button functional
- [ ] Permission handling graceful (no crash if denied)
- [ ] Console logs present with `[DEV QA]` prefix
- [ ] **CRITICAL**: DEV QA section invisible in production builds

---

**Last Updated**: 2025-12-31
**Version**: MVP 1.4 + DEV Tools
