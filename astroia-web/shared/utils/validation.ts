/**
 * Utilitaires de validation
 */

/**
 * Valide un email
 */
export function isValidEmail(email: string): boolean {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

/**
 * Valide un mot de passe (minimum 8 caractères)
 */
export function isValidPassword(password: string): boolean {
  return password.length >= 8;
}

/**
 * Valide une date de naissance (pas dans le futur, après 1900)
 */
export function isValidBirthDate(date: Date): boolean {
  const now = new Date();
  const minDate = new Date('1900-01-01');

  return date <= now && date >= minDate;
}

/**
 * Valide une heure (format HH:MM)
 */
export function isValidTime(time: string): boolean {
  const timeRegex = /^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$/;
  return timeRegex.test(time);
}

/**
 * Valide un nom (2-50 caractères, lettres et espaces)
 */
export function isValidName(name: string): boolean {
  return name.length >= 2 && name.length <= 50 && /^[a-zA-ZÀ-ÿ\s'-]+$/.test(name);
}

