/**
 * Types et clés AsyncStorage
 */

// Storage Keys
export const STORAGE_KEYS = {
  // Auth
  AUTH_TOKEN: 'auth_token',

  // Onboarding
  HAS_SEEN_WELCOME_SCREEN: 'hasSeenWelcomeScreen',
  ONBOARDING_COMPLETED: 'onboarding_completed',

  // Profile
  BIRTH_DATE: 'birth_date',
  BIRTH_TIME: 'birth_time',
  BIRTH_PLACE: 'birth_place',
  BIRTH_LATITUDE: 'birth_latitude',
  BIRTH_LONGITUDE: 'birth_longitude',

  // Cycle
  LAST_PERIOD_DATE: 'lastPeriodDate',
  AVERAGE_CYCLE_LENGTH: 'averageCycleLength',
} as const;

export type StorageKey = typeof STORAGE_KEYS[keyof typeof STORAGE_KEYS];
