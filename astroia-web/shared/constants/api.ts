/**
 * Constantes API
 */

export const API_CODES = {
  // Success
  OK: 200,
  CREATED: 201,
  NO_CONTENT: 204,

  // Client Errors
  BAD_REQUEST: 400,
  UNAUTHORIZED: 401,
  FORBIDDEN: 403,
  NOT_FOUND: 404,
  CONFLICT: 409,
  UNPROCESSABLE_ENTITY: 422,
  TOO_MANY_REQUESTS: 429,

  // Server Errors
  INTERNAL_SERVER_ERROR: 500,
  NOT_IMPLEMENTED: 501,
  SERVICE_UNAVAILABLE: 503,
} as const;

export const ERROR_MESSAGES = {
  INVALID_EMAIL: 'Email invalide',
  INVALID_PASSWORD: 'Mot de passe invalide',
  INVALID_DATE: 'Date invalide',
  INVALID_TIME: 'Heure invalide',
  UNAUTHORIZED: 'Non autorisé',
  NOT_FOUND: 'Ressource non trouvée',
  SERVER_ERROR: 'Erreur serveur',
  NETWORK_ERROR: 'Erreur réseau',
} as const;

export const API_ENDPOINTS = {
  // Auth
  LOGIN: '/api/users/login',
  REGISTER: '/api/users/register',
  LOGOUT: '/api/users/logout',

  // Users
  ME: '/api/users/me',
  USERS: '/api/users',

  // Dashboard
  DASHBOARD: '/api/dashboard',

  // ML
  PARENT_CHILD_PREDICT: '/api/ml/parent-child/predict',
} as const;

