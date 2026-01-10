// Thème visuel Astro.IA - Mystique et moderne

// Palette de couleurs - Optimisée pour contraste (WCAG AA)
export const colors = {
  // Couleurs principales
  primary: '#8B7CFF',     // Violet cosmique (ajusté pour contraste)
  secondary: '#6B7CFF',   // Bleu indigo
  accent: '#FFB347',      // Doré lumineux
  
  // Dégradés
  darkBg: ['#050816', '#1E1B4B', '#4C1D95'], // Bleu nuit → Violet (plus foncé)
  gradientDark: ['#050816', '#1E1B4B', '#4C1D95'], // Alias pour darkBg
  cardBg: 'rgba(23, 27, 42, 0.8)', // Fond semi-transparent ajusté
  ctaGradient: ['#FFB347', '#FF9F1C'], // Dégradé CTA optimisé
  
  // Texte - Contraste optimal
  text: '#F7F4FF',        // Presque blanc (contraste 15:1)
  textSecondary: '#C3BEDD', // Gris-violet clair (contraste 7:1)
  textMuted: '#9B95B3',   // Labels (contraste 4.5:1)
  
  // États & Badges
  success: '#2ECC71',     // Vert (badge Fort)
  successText: '#0B1A10', // Texte sur badge vert
  warning: '#FF9F1C',     // Orange (badge Moyen)
  warningText: '#1E1E26', // Texte sur badge orange
  weak: '#8E8E98',        // Gris (badge Faible)
  weakText: '#1E1E26',    // Texte sur badge gris
  error: '#EF4444',
};

// Typographie
export const fonts = {
  family: {
    regular: 'System',
    medium: 'System',
    bold: 'System',
  },
  sizes: {
    xs: 12,
    sm: 14,
    md: 16,
    lg: 20,
    xl: 24,
    xxl: 32,
    xxxl: 40,
  },
  weights: {
    regular: '400',
    medium: '600',
    bold: 'bold',
  },
};

// Espacements
export const spacing = {
  xs: 4,
  sm: 8,
  md: 16,
  lg: 24,
  xl: 32,
  xxl: 48,
};

// Rayons de bordure
export const borderRadius = {
  sm: 8,
  md: 12,
  lg: 16,
  xl: 20, // Optimisé pour le CTA
  xxl: 24,
  full: 9999,
};

// Ombres
export const shadows = {
  sm: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  md: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 4.65,
    elevation: 8,
  },
  lg: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.37,
    shadowRadius: 7.49,
    elevation: 12,
  },
};

// Animations
export const animations = {
  duration: {
    fast: 200,
    normal: 300,
    slow: 500,
  },
  easing: {
    easeIn: 'ease-in',
    easeOut: 'ease-out',
    easeInOut: 'ease-in-out',
  },
};

// Export par défaut pour faciliter l'import
export default {
  colors,
  fonts,
  spacing,
  borderRadius,
  shadows,
  animations,
};

// Pour la compatibilité avec l'ancien code (majuscules)
export const COLORS = colors;
export const FONTS = fonts;
export const SPACING = spacing;
export const BORDER_RADIUS = borderRadius;
export const SHADOWS = shadows;
