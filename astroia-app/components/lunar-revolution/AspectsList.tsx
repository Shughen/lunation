import React, { useMemo } from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import { color, space, radius, type as typography } from '@/theme/tokens';
import { LunarAspect } from '@/lib/services/lunarRevolutionService';
import { translatePlanet, translateAspect, translateStrength } from '@/lib/utils/astrologyTranslations';
import { getAspectEmoji, getStrengthColor, sortAspects } from '@/lib/utils/aspectInterpretations';

interface AspectsListProps {
  aspects: LunarAspect[];
  title?: string;
}

export default React.memo(function AspectsList({ aspects, title = 'Aspects principaux' }: AspectsListProps) {
  // Trier les aspects selon la hiérarchie astrologique
  const sortedAspects = useMemo(() => {
    if (!aspects || aspects.length === 0) return [];
    
    // Convertir LunarAspect en format compatible avec sortAspects
    const formattedAspects = aspects.map(asp => ({
      from: asp.from,
      to: asp.to,
      aspect_type: asp.aspect_type,
      strength: asp.strength,
      orb: asp.orb,
      interpretation: asp.interpretation,
    }));
    
    return sortAspects(formattedAspects);
  }, [aspects]);

  if (!sortedAspects || sortedAspects.length === 0) {
    return (
      <View style={styles.container}>
        <Text style={styles.label}>{title.toUpperCase()}</Text>
        <Text style={styles.emptyText}>
          Aucun aspect significatif pour cette révolution lunaire.
        </Text>
      </View>
    );
  }

  // Grouper par intensité pour l'affichage
  const strongAspects = sortedAspects.filter(a => a.strength === 'strong');
  const mediumAspects = sortedAspects.filter(a => a.strength === 'medium');
  const weakAspects = sortedAspects.filter(a => a.strength === 'weak');

  return (
    <View style={styles.container}>
      <Text style={styles.label}>{title.toUpperCase()}</Text>
      
      {strongAspects.length > 0 && (
        <View style={styles.aspectsGroup}>
          <Text style={styles.groupLabel}>Aspects forts</Text>
          <View style={styles.aspectsList}>
            {strongAspects.map((aspect, index) => (
              <AspectItem key={`strong-${index}`} aspect={aspect} />
            ))}
          </View>
        </View>
      )}
      
      {mediumAspects.length > 0 && (
        <View style={styles.aspectsGroup}>
          <Text style={styles.groupLabel}>Aspects moyens</Text>
          <View style={styles.aspectsList}>
            {mediumAspects.map((aspect, index) => (
              <AspectItem key={`medium-${index}`} aspect={aspect} />
            ))}
          </View>
        </View>
      )}
      
      {weakAspects.length > 0 && (
        <View style={styles.aspectsGroup}>
          <Text style={styles.groupLabel}>Aspects faibles</Text>
          <View style={styles.aspectsList}>
            {weakAspects.map((aspect, index) => (
              <AspectItem key={`weak-${index}`} aspect={aspect} />
            ))}
          </View>
        </View>
      )}
    </View>
  );
});

function AspectItem({ aspect }: { aspect: LunarAspect }) {
  const planetFrom = translatePlanet(aspect.from);
  const planetTo = translatePlanet(aspect.to);
  const aspectType = translateAspect(aspect.aspect_type);
  const strength = translateStrength(aspect.strength);
  const emoji = getAspectEmoji(aspect.aspect_type);
  const strengthColor = getStrengthColor(aspect.strength);
  const orb = Math.abs(aspect.orb).toFixed(2);

  return (
    <View style={styles.aspectItem}>
      <View style={styles.aspectHeader}>
        <Text style={styles.aspectEmoji}>{emoji}</Text>
        <View style={styles.aspectInfo}>
          <Text style={styles.aspectPlanets}>
            {planetFrom} {aspectType} {planetTo}
          </Text>
          <View style={styles.aspectMeta}>
            <View style={[styles.strengthBadge, { backgroundColor: strengthColor + '22' }]}>
              <Text style={[styles.strengthText, { color: strengthColor }]}>
                {strength}
              </Text>
            </View>
            <Text style={styles.orbText}>Orbe {orb}°</Text>
          </View>
        </View>
      </View>
      
      {aspect.interpretation && (
        <Text style={styles.aspectInterpretation}>
          {aspect.interpretation}
        </Text>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginBottom: space.lg,
  },
  label: {
    ...typography.label,
    color: color.brand,
    letterSpacing: 1.2,
    marginBottom: space.md,
  },
  emptyText: {
    ...typography.body,
    color: color.textMuted,
    fontStyle: 'italic',
    textAlign: 'center',
    paddingVertical: space.lg,
  },
  aspectsGroup: {
    marginBottom: space.lg,
  },
  groupLabel: {
    ...typography.label,
    color: color.textMuted,
    fontSize: 12,
    marginBottom: space.sm,
    textTransform: 'uppercase',
    letterSpacing: 0.5,
  },
  aspectsList: {
    gap: space.md,
  },
  aspectItem: {
    backgroundColor: color.surface,
    borderRadius: radius.md,
    padding: space.md,
    borderWidth: 1,
    borderColor: color.border,
  },
  aspectHeader: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginBottom: space.xs,
  },
  aspectEmoji: {
    fontSize: 24,
    marginRight: space.sm,
  },
  aspectInfo: {
    flex: 1,
  },
  aspectPlanets: {
    ...typography.h4,
    color: color.text,
    fontWeight: '700',
    marginBottom: space.xs,
  },
  aspectMeta: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: space.sm,
  },
  strengthBadge: {
    paddingHorizontal: space.sm,
    paddingVertical: 2,
    borderRadius: 4,
  },
  strengthText: {
    ...typography.bodySm,
    fontWeight: '700',
  },
  orbText: {
    ...typography.bodySm,
    color: color.textMuted,
  },
  aspectInterpretation: {
    ...typography.body,
    color: color.textSecondary,
    marginTop: space.xs,
    lineHeight: 20,
  },
});

