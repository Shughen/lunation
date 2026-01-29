/**
 * Rituals Tab Screen
 * Daily rituals and journal prompts based on lunar phase
 */

import React, { useState, useMemo } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';
import { useLunar } from '../../contexts/LunarProvider';
import { JournalEntryModal } from '../../components/JournalEntryModal';
import { MoonPhaseIcon } from '../../components/icons/MoonPhaseIcon';
import { Skeleton } from '../../components/Skeleton';
import { haptics } from '../../services/haptics';
import { getMoonPhaseFrench } from '../../utils/horoscopeCalculations';

// Fallback si LinearGradient n'est pas disponible
const LinearGradientComponent = LinearGradient || (({ colors: bgColors, style, children, ...props }: any) => {
  return <View style={[{ backgroundColor: bgColors?.[0] || '#1a0b2e' }, style]} {...props}>{children}</View>;
});

// Rituals by moon phase
const PHASE_RITUALS: Record<string, Array<{ title: string; description: string; icon: string }>> = {
  new_moon: [
    { title: 'Meditation d\'intention', description: 'Prenez 10 minutes pour visualiser vos objectifs du cycle', icon: '' },
    { title: 'Liste de souhaits', description: 'Ecrivez 3 intentions claires pour ce nouveau cycle', icon: '' },
    { title: 'Nettoyage energetique', description: 'Brulez de la sauge ou ouvrez les fenetres pour renouveler l\'energie', icon: '' },
  ],
  waxing_crescent: [
    { title: 'Premier pas', description: 'Identifiez une action concrete vers votre objectif', icon: '' },
    { title: 'Affirmations positives', description: 'Repetez 3 affirmations liees a vos intentions', icon: '' },
    { title: 'Planification', description: 'Organisez votre semaine en accord avec vos intentions', icon: '' },
  ],
  first_quarter: [
    { title: 'Bilan intermediaire', description: 'Evaluez vos progres et ajustez si necessaire', icon: '' },
    { title: 'Action decisive', description: 'Prenez une decision que vous avez repoussee', icon: '' },
    { title: 'Perseverance', description: 'Surmontez un obstacle avec determination', icon: '' },
  ],
  waxing_gibbous: [
    { title: 'Perfectionnement', description: 'Affinez les details de vos projets en cours', icon: '' },
    { title: 'Gratitude anticipee', description: 'Remerciez pour ce qui est en train de se manifester', icon: '' },
    { title: 'Preparation', description: 'Preparez-vous pour la culmination de vos efforts', icon: '' },
  ],
  full_moon: [
    { title: 'Celebration', description: 'Reconnaissez et celebrez vos accomplissements', icon: '' },
    { title: 'Liberation', description: 'Laissez partir ce qui ne vous sert plus', icon: '' },
    { title: 'Bain de lune', description: 'Rechargez vos cristaux ou meditez sous la lune', icon: '' },
  ],
  waning_gibbous: [
    { title: 'Partage', description: 'Transmettez ce que vous avez appris a d\'autres', icon: '' },
    { title: 'Gratitude', description: 'Listez 5 choses pour lesquelles vous etes reconnaissant', icon: '' },
    { title: 'Reflexion', description: 'Analysez ce qui a fonctionne et ce qui peut s\'ameliorer', icon: '' },
  ],
  last_quarter: [
    { title: 'Lacher-prise', description: 'Abandonnez une habitude qui vous limite', icon: '' },
    { title: 'Tri et rangement', description: 'Desencombrez un espace physique ou mental', icon: '' },
    { title: 'Pardon', description: 'Pardonnez-vous ou pardonnez quelqu\'un', icon: '' },
  ],
  waning_crescent: [
    { title: 'Repos', description: 'Accordez-vous du temps pour recuperer', icon: '' },
    { title: 'Introspection', description: 'Meditez sur les lecons du cycle qui s\'acheve', icon: '' },
    { title: 'Reve lucide', description: 'Notez vos reves au reveil pour recevoir des messages', icon: '' },
  ],
};

// Journal prompts by phase
const PHASE_PROMPTS: Record<string, string> = {
  new_moon: 'Quelles nouvelles graines voulez-vous planter ce cycle?',
  waxing_crescent: 'Quel premier pas pouvez-vous faire aujourd\'hui?',
  first_quarter: 'Quel obstacle devez-vous surmonter? Comment allez-vous le faire?',
  waxing_gibbous: 'Qu\'est-ce qui necessite votre attention pour etre parfait?',
  full_moon: 'Qu\'avez-vous accompli dont vous etes fier? Que devez-vous laisser partir?',
  waning_gibbous: 'Quelle sagesse souhaitez-vous partager avec les autres?',
  last_quarter: 'Quelle vieille croyance etes-vous pret a abandonner?',
  waning_crescent: 'De quoi avez-vous besoin pour vous regenerer avant le prochain cycle?',
};

function normalizePhase(phase: string | undefined): string {
  if (!phase) return 'new_moon';
  return phase.toLowerCase().replace(/\s+/g, '_');
}

interface RitualCardProps {
  title: string;
  description: string;
  icon: string;
  completed: boolean;
  onToggle: () => void;
}

function RitualCard({ title, description, icon, completed, onToggle }: RitualCardProps) {
  return (
    <TouchableOpacity
      style={[styles.ritualCard, completed && styles.ritualCardCompleted]}
      onPress={onToggle}
    >
      <View style={styles.ritualIcon}>
        <Text style={styles.ritualIconText}>{icon}</Text>
      </View>
      <View style={styles.ritualContent}>
        <Text style={[styles.ritualTitle, completed && styles.ritualTitleCompleted]}>
          {title}
        </Text>
        <Text style={styles.ritualDescription}>{description}</Text>
      </View>
      <View style={[styles.checkbox, completed && styles.checkboxCompleted]}>
        {completed && <Text style={styles.checkmark}>OK</Text>}
      </View>
    </TouchableOpacity>
  );
}

export default function RitualsScreen() {
  const { current: lunarData, status } = useLunar();
  const [completedRituals, setCompletedRituals] = useState<Set<string>>(new Set());
  const [journalModalVisible, setJournalModalVisible] = useState(false);

  const moonPhase = lunarData?.moon?.phase || 'waxing_crescent';
  const normalizedPhase = normalizePhase(moonPhase);
  const phaseFrench = getMoonPhaseFrench(moonPhase);

  const rituals = useMemo(
    () => PHASE_RITUALS[normalizedPhase] || PHASE_RITUALS.new_moon,
    [normalizedPhase]
  );

  const journalPrompt = PHASE_PROMPTS[normalizedPhase] || PHASE_PROMPTS.new_moon;

  const toggleRitual = (title: string) => {
    haptics.light();
    setCompletedRituals((prev) => {
      const newSet = new Set(prev);
      if (newSet.has(title)) {
        newSet.delete(title);
      } else {
        newSet.add(title);
      }
      return newSet;
    });
  };

  const completedCount = completedRituals.size;
  const totalCount = rituals.length;
  const progressPercent = (completedCount / totalCount) * 100;

  // Loading state
  if (status.isLoading && !lunarData) {
    return (
      <LinearGradientComponent colors={colors.darkBg} style={styles.container}>
        <ScrollView contentContainerStyle={styles.scrollContent}>
          <View style={styles.header}>
            <Text style={styles.title}>Rituels du Jour</Text>
          </View>
          <Skeleton width="100%" height={100} style={{ marginBottom: spacing.md }} />
          <Skeleton width="100%" height={80} style={{ marginBottom: spacing.sm }} />
          <Skeleton width="100%" height={80} style={{ marginBottom: spacing.sm }} />
          <Skeleton width="100%" height={80} />
        </ScrollView>
      </LinearGradientComponent>
    );
  }

  return (
    <LinearGradientComponent colors={colors.darkBg} style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.title}>Rituels du Jour</Text>
        </View>

        {/* Phase Info */}
        <View style={styles.phaseCard}>
          <MoonPhaseIcon phase={moonPhase} size={40} />
          <View style={styles.phaseInfo}>
            <Text style={styles.phaseName}>{phaseFrench}</Text>
            <Text style={styles.phaseSubtitle}>
              {completedCount}/{totalCount} rituels accomplis
            </Text>
          </View>
          <View style={styles.progressCircle}>
            <Text style={styles.progressText}>{Math.round(progressPercent)}%</Text>
          </View>
        </View>

        {/* Rituals List */}
        <View style={styles.ritualsSection}>
          <Text style={styles.sectionTitle}>Rituels suggeres</Text>
          {rituals.map((ritual, index) => (
            <RitualCard
              key={index}
              title={ritual.title}
              description={ritual.description}
              icon={ritual.icon}
              completed={completedRituals.has(ritual.title)}
              onToggle={() => toggleRitual(ritual.title)}
            />
          ))}
        </View>

        {/* Journal Section */}
        <View style={styles.journalSection}>
          <Text style={styles.sectionTitle}>Reflexion du jour</Text>
          <View style={styles.journalCard}>
            <Text style={styles.journalPrompt}>{journalPrompt}</Text>
            <TouchableOpacity
              style={styles.journalButton}
              onPress={() => {
                haptics.light();
                setJournalModalVisible(true);
              }}
            >
              <Text style={styles.journalButtonText}>Ecrire dans mon journal</Text>
            </TouchableOpacity>
          </View>
        </View>

        {/* Tip Card */}
        <View style={styles.tipCard}>
          <Text style={styles.tipIcon}>*</Text>
          <Text style={styles.tipText}>
            Les rituels sont des suggestions pour vous connecter a l'energie lunaire.
            Adaptez-les selon votre ressenti et vos besoins du moment.
          </Text>
        </View>
      </ScrollView>

      {/* Journal Modal */}
      {lunarData && (
        <JournalEntryModal
          visible={journalModalVisible}
          onClose={() => setJournalModalVisible(false)}
          moonContext={lunarData.moon}
        />
      )}
    </LinearGradientComponent>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollContent: {
    paddingTop: 60,
    paddingHorizontal: spacing.lg,
    paddingBottom: 100,
  },
  header: {
    alignItems: 'center',
    marginBottom: spacing.xl,
  },
  title: {
    ...fonts.h2,
    color: colors.text,
  },
  phaseCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  phaseInfo: {
    flex: 1,
    marginLeft: spacing.md,
  },
  phaseName: {
    ...fonts.h3,
    color: colors.text,
    marginBottom: spacing.xs,
  },
  phaseSubtitle: {
    ...fonts.bodySmall,
    color: colors.textMuted,
  },
  progressCircle: {
    width: 50,
    height: 50,
    borderRadius: 25,
    backgroundColor: 'rgba(183, 148, 246, 0.2)',
    borderWidth: 2,
    borderColor: colors.accent,
    alignItems: 'center',
    justifyContent: 'center',
  },
  progressText: {
    ...fonts.bodySmall,
    color: colors.accent,
    fontWeight: '700',
  },
  ritualsSection: {
    marginBottom: spacing.lg,
  },
  sectionTitle: {
    ...fonts.body,
    color: colors.gold,
    fontWeight: '600',
    marginBottom: spacing.md,
  },
  ritualCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.md,
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: spacing.sm,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  ritualCardCompleted: {
    backgroundColor: 'rgba(74, 222, 128, 0.1)',
    borderColor: 'rgba(74, 222, 128, 0.3)',
  },
  ritualIcon: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: 'rgba(183, 148, 246, 0.1)',
    alignItems: 'center',
    justifyContent: 'center',
  },
  ritualIconText: {
    fontSize: 20,
  },
  ritualContent: {
    flex: 1,
    marginLeft: spacing.md,
  },
  ritualTitle: {
    ...fonts.body,
    color: colors.text,
    fontWeight: '600',
    marginBottom: spacing.xs,
  },
  ritualTitleCompleted: {
    textDecorationLine: 'line-through',
    color: colors.success,
  },
  ritualDescription: {
    ...fonts.caption,
    color: colors.textMuted,
    lineHeight: 16,
  },
  checkbox: {
    width: 28,
    height: 28,
    borderRadius: 14,
    borderWidth: 2,
    borderColor: colors.textMuted,
    alignItems: 'center',
    justifyContent: 'center',
  },
  checkboxCompleted: {
    backgroundColor: colors.success,
    borderColor: colors.success,
  },
  checkmark: {
    ...fonts.caption,
    color: colors.text,
    fontWeight: '700',
  },
  journalSection: {
    marginBottom: spacing.lg,
  },
  journalCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    borderWidth: 1,
    borderColor: colors.accent,
  },
  journalPrompt: {
    ...fonts.body,
    color: colors.text,
    fontStyle: 'italic',
    lineHeight: 24,
    marginBottom: spacing.lg,
  },
  journalButton: {
    backgroundColor: colors.accent,
    borderRadius: borderRadius.md,
    paddingVertical: spacing.md,
    alignItems: 'center',
  },
  journalButtonText: {
    ...fonts.button,
    color: '#000000',
  },
  tipCard: {
    backgroundColor: 'rgba(255, 215, 0, 0.1)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    flexDirection: 'row',
    alignItems: 'flex-start',
    borderWidth: 1,
    borderColor: 'rgba(255, 215, 0, 0.3)',
  },
  tipIcon: {
    fontSize: 20,
    marginRight: spacing.sm,
  },
  tipText: {
    ...fonts.caption,
    color: colors.text,
    flex: 1,
    lineHeight: 18,
  },
});
