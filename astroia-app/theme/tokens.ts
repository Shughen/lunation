/**
 * Design Tokens - LUNA App
 * Système de tokens unifié pour l'ensemble de l'application
 */

// ============================================
// RADIUS
// ============================================
export const radius = {
  sm: 12,
  md: 16,
  lg: 24,
  xl: 28,
} as const;

// ============================================
// SPACE
// ============================================
export const space = {
  xs: 8,
  sm: 12,
  md: 16,
  lg: 20,
  xl: 24,
  '2xl': 32,
  '3xl': 40,
  '4xl': 48,
} as const;

// ============================================
// SHADOWS
// ============================================
export const shadow = {
  sm: {
    shadowColor: '#000',
    shadowOpacity: 0.15,
    shadowRadius: 8,
    shadowOffset: { width: 0, height: 4 },
    elevation: 4,
  },
  md: {
    shadowColor: '#000',
    shadowOpacity: 0.25,
    shadowRadius: 16,
    shadowOffset: { width: 0, height: 8 },
    elevation: 8,
  },
  lg: {
    shadowColor: '#000',
    shadowOpacity: 0.35,
    shadowRadius: 24,
    shadowOffset: { width: 0, height: 12 },
    elevation: 12,
  },
} as const;

// ============================================
// COLORS - Palette optimisée pour contraste (WCAG AA)
// ============================================
export const color = {
  // Backgrounds
  bg: '#050816',              // Violet très foncé (arrière-plan principal)
  surface: '#171B2A',         // Violet/gris plus clair (cartes)
  surfaceElevated: '#1E2235', // Cartes élevées
  surfaceHover: '#252940',    // Hover sur cartes
  
  // Text - Contraste optimal
  text: '#F7F4FF',            // Presque blanc (contraste 15:1 sur bg)
  textSecondary: '#C3BEDD',   // Gris-violet clair (contraste 7:1)
  textMuted: '#9B95B3',       // Labels secondaires (contraste 4.5:1)
  textDisabled: '#6B6780',    // Texte désactivé
  
  // Brand
  brand: '#8B7CFF',           // Violet principal (ajusté pour contraste)
  brandSoft: '#8B7CFF22',
  brandHover: '#A396FF',
  
  // Semantic - Badges d'intensité
  success: '#2ECC71',         // Vert (Fort)
  successSoft: '#2ECC7122',
  successText: '#0B1A10',     // Texte sur vert
  warning: '#FF9F1C',         // Orange (Moyen)
  warningSoft: '#FF9F1C22',
  warningText: '#1E1E26',     // Texte sur orange
  weak: '#8E8E98',            // Gris (Faible)
  weakText: '#1E1E26',        // Texte sur gris
  danger: '#EF4444',
  dangerSoft: '#EF444422',
  info: '#3B82F6',
  infoSoft: '#3B82F622',
  
  // Borders
  border: '#2A2D42',
  borderFocus: '#8B7CFF',
  
  // Overlay
  overlay: 'rgba(5, 8, 22, 0.85)',
} as const;

// ============================================
// TYPOGRAPHY
// ============================================
export const type = {
  h1: {
    fontSize: 28,
    fontWeight: '700' as const,
    lineHeight: 34,
    letterSpacing: -0.5,
  },
  h2: {
    fontSize: 22,
    fontWeight: '700' as const,
    lineHeight: 28,
    letterSpacing: -0.3,
  },
  h3: {
    fontSize: 18,
    fontWeight: '700' as const,
    lineHeight: 24,
    letterSpacing: -0.2,
  },
  h4: {
    fontSize: 16,
    fontWeight: '600' as const,
    lineHeight: 22,
    letterSpacing: 0,
  },
  body: {
    fontSize: 16,
    fontWeight: '400' as const,
    lineHeight: 22,
    letterSpacing: 0,
  },
  bodySm: {
    fontSize: 14,
    fontWeight: '400' as const,
    lineHeight: 20,
    letterSpacing: 0,
  },
  caption: {
    fontSize: 12,
    fontWeight: '400' as const,
    lineHeight: 16,
    letterSpacing: 0,
  },
  label: {
    fontSize: 14,
    fontWeight: '600' as const,
    lineHeight: 18,
    letterSpacing: 0.1,
  },
} as const;

// ============================================
// ANIMATIONS
// ============================================
export const animation = {
  fast: 150,
  normal: 250,
  slow: 350,
  verySlow: 500,
} as const;

// ============================================
// LAYOUT
// ============================================
export const layout = {
  maxWidth: 480,
  containerPadding: 20,
  sectionGap: 24,
  cardGap: 16,
} as const;

// ============================================
// HIT SLOP (Accessibility)
// ============================================
export const hitSlop = {
  sm: { top: 8, bottom: 8, left: 8, right: 8 },
  md: { top: 12, bottom: 12, left: 12, right: 12 },
  lg: { top: 16, bottom: 16, left: 16, right: 16 },
} as const;

// ============================================
// HELPER TYPE
// ============================================
export type Color = keyof typeof color;
export type Space = keyof typeof space;
export type Radius = keyof typeof radius;
export type Shadow = keyof typeof shadow;
export type Type = keyof typeof type;

// ============================================
// EXPORTS
// ============================================
export default {
  color,
  space,
  radius,
  shadow,
  type,
  animation,
  layout,
  hitSlop,
};

