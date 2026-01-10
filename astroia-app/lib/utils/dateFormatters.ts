/**
 * Utilitaires de formatage de dates pour LUNA
 */

/**
 * Formate une date au format "Novembre 2025"
 * @param date - Date à formater
 * @returns String formatée (ex: "Novembre 2025")
 */
export function formatMonthYear(date: Date): string {
  const monthNames = [
    'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
    'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'
  ];
  
  const month = monthNames[date.getMonth()];
  const year = date.getFullYear();
  
  return `${month} ${year}`;
}

/**
 * Formate une date au format "15 janvier 2025"
 * @param date - Date à formater
 * @returns String formatée (ex: "15 janvier 2025")
 */
export function formatFullDate(date: Date): string {
  const monthNames = [
    'janvier', 'février', 'mars', 'avril', 'mai', 'juin',
    'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'
  ];
  
  const day = date.getDate();
  const month = monthNames[date.getMonth()];
  const year = date.getFullYear();
  
  return `${day} ${month} ${year}`;
}

