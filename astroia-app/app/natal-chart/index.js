import { View, Text, StyleSheet, TouchableOpacity, ScrollView, Animated, Alert, ActivityIndicator, Switch } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { colors, fonts, spacing, borderRadius } from '@/constants/theme';
import { useEffect, useRef, useState } from 'react';
import { useRouter } from 'expo-router';
import { useProfileStore } from '@/stores/profileStore';
import { natalService } from '@/lib/api/natalService';
import { natalServiceRapidAPI } from '@/lib/api/natalServiceRapidAPI';

export default function NatalChartScreen() {
  const router = useRouter();
  const { profile, hasProfile, saveAstrologicalData } = useProfileStore();
  
  const [natalChart, setNatalChart] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [isComputing, setIsComputing] = useState(false);
  const [isSaving, setIsSaving] = useState(false);
  const [useRapidAPI, setUseRapidAPI] = useState(true); // Toggle RapidAPI vs ancien système
  
  const fadeAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    loadNatalChart();
    
    Animated.timing(fadeAnim, {
      toValue: 1,
      duration: 600,
      useNativeDriver: true,
    }).start();
  }, [useRapidAPI]);

  const loadNatalChart = async () => {
    setIsLoading(true);
    const service = useRapidAPI ? natalServiceRapidAPI : natalService;
    const chart = await service.getLatestNatalChart();
    console.log('[DEBUG Natal] natalChart:', {
      hasChart: !!chart,
      hasPositions: !!chart?.positions,
      sun: chart?.positions?.sun?.sign || chart?.chart?.sun?.sign,
      moon: chart?.positions?.moon?.sign || chart?.chart?.moon?.sign,
      ascendant: chart?.positions?.ascendant?.sign || chart?.chart?.ascendant?.sign,
    });
    setNatalChart(chart);
    setIsLoading(false);
  };

  const handleCompute = async () => {
    if (!hasProfile) {
      Alert.alert('Profil requis', 'Complétez d\'abord votre profil astral');
      router.push('/(tabs)/profile');
      return;
    }

    // Vérifier que le profil a les coordonnées
    if (!profile.latitude || !profile.longitude) {
      Alert.alert(
        'Géocodage requis',
        'Votre lieu de naissance doit être validé. Retournez dans Profil et validez votre lieu.',
        [{ text: 'OK', onPress: () => router.push('/(tabs)/profile') }]
      );
      return;
    }

    setIsComputing(true);

    try {
      // Choisir le service selon le toggle
      const service = useRapidAPI ? natalServiceRapidAPI : natalService;
      
      const result = await service.computeNatalChartForCurrentUser({
        birthDate: profile.birthDate,
        birthTime: profile.birthTime,
        birthPlace: profile.birthPlace,
        lat: profile.latitude,
        lon: profile.longitude,
        tz: profile.timezone || 'UTC',
      });

      setNatalChart(result);
      
      // Sauvegarder automatiquement dans le profil
      await autoSaveToProfile(result);
      
      // NOUVEAU : Synchroniser le profil avec le thème natal calculé
      try {
        const { syncFromNatalChart } = useProfileStore.getState();
        await syncFromNatalChart(null);
        console.log('[NatalChart] ✅ Profil synchronisé automatiquement après calcul');
      } catch (error) {
        console.error('[NatalChart] Erreur synchronisation automatique:', error);
        // Ne pas bloquer si la sync échoue
      }
      
      Alert.alert(
        '✨ Thème calculé !',
        `Votre carte du ciel a été calculée via ${useRapidAPI ? 'RapidAPI' : 'API V1'} et sauvegardée`,
        [{ text: 'Super !' }]
      );
    } catch (error) {
      console.error('[NatalChart] Erreur:', error);
      Alert.alert('Erreur', error.message || 'Impossible de calculer le thème natal');
    } finally {
      setIsComputing(false);
    }
  };

  // Sauvegarder automatiquement après calcul
  const autoSaveToProfile = async (chartResult) => {
    try {
      const chartPositions = chartResult?.positions || chartResult?.chart;
      
      console.log('[NatalChart] Chart positions reçues:', chartPositions);
      console.log('[NatalChart] Sun data:', chartPositions?.sun);
      console.log('[NatalChart] Moon data:', chartPositions?.moon);
      console.log('[NatalChart] Ascendant data:', chartPositions?.ascendant);
      
      if (!chartPositions || !chartPositions.sun || !chartPositions.moon || !chartPositions.ascendant) {
        console.log('[NatalChart] Données incomplètes, pas de sauvegarde auto');
        return;
      }

      // Mapper les signes aux IDs (FRANÇAIS car l'API retourne en français)
      const signMapping = {
        'Bélier': { id: 1, name: 'Bélier', emoji: '♈' },
        'Taureau': { id: 2, name: 'Taureau', emoji: '♉' },
        'Gémeaux': { id: 3, name: 'Gémeaux', emoji: '♊' },
        'Cancer': { id: 4, name: 'Cancer', emoji: '♋' },
        'Lion': { id: 5, name: 'Lion', emoji: '♌' },
        'Vierge': { id: 6, name: 'Vierge', emoji: '♍' },
        'Balance': { id: 7, name: 'Balance', emoji: '♎' },
        'Scorpion': { id: 8, name: 'Scorpion', emoji: '♏' },
        'Sagittaire': { id: 9, name: 'Sagittaire', emoji: '♐' },
        'Capricorne': { id: 10, name: 'Capricorne', emoji: '♑' },
        'Verseau': { id: 11, name: 'Verseau', emoji: '♒' },
        'Poissons': { id: 12, name: 'Poissons', emoji: '♓' },
      };

      // Debug: voir les signes bruts
      console.log('[NatalChart] Signes bruts:', {
        sun: chartPositions.sun?.sign,
        moon: chartPositions.moon?.sign,
        ascendant: chartPositions.ascendant?.sign,
      });

      const astroData = {
        sunSign: signMapping[chartPositions.sun?.sign] || signMapping[chartPositions.sun?.zodiacSign] || null,
        moonSign: signMapping[chartPositions.moon?.sign] || signMapping[chartPositions.moon?.zodiacSign] || null,
        ascendant: signMapping[chartPositions.ascendant?.sign] || signMapping[chartPositions.ascendant?.zodiacSign] || null,
      };

      console.log('[NatalChart] Sauvegarde auto des données astro:', astroData);

      const success = await saveAstrologicalData(astroData);

      if (success) {
        console.log('[NatalChart] ✅ Données astro sauvegardées automatiquement !');
      }
    } catch (error) {
      console.error('[NatalChart] Erreur sauvegarde auto:', error);
    }
  };

  const handleSaveToProfile = async () => {
    if (!positions || !positions.sun || !positions.moon || !positions.ascendant) {
      Alert.alert('Erreur', 'Calculez d\'abord votre thème natal');
      return;
    }

    setIsSaving(true);

    try {
      await autoSaveToProfile(natalChart);
      
      Alert.alert(
        '✅ Données sauvegardées !',
        'Vos signes (Soleil, Lune, Ascendant) sont maintenant enregistrés et seront utilisés automatiquement dans vos analyses.',
        [{ text: 'Super !' }]
      );
    } catch (error) {
      Alert.alert('Erreur', error.message);
    } finally {
      setIsSaving(false);
    }
  };

  const positions = natalChart?.positions || natalChart?.chart;

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
        {/* Header */}
        <View style={styles.header}>
          <TouchableOpacity onPress={() => router.back()} style={styles.backButton}>
            <Ionicons name="arrow-back" size={24} color={colors.text} />
          </TouchableOpacity>
          <Text style={styles.headerTitle}>🪐 Thème Natal</Text>
          <View style={styles.placeholder} />
        </View>

        {/* Toggle API Source */}
        <View style={styles.apiToggleContainer}>
          <Text style={styles.apiToggleLabel}>
            {useRapidAPI ? '🌟 RapidAPI (Précis)' : '📡 API V1 (Approx)'}
          </Text>
          <Switch
            value={useRapidAPI}
            onValueChange={(value) => {
              setUseRapidAPI(value);
              setNatalChart(null); // Reset chart quand on change d'API
            }}
            trackColor={{ false: '#767577', true: colors.accent }}
            thumbColor={useRapidAPI ? colors.primary : '#f4f3f4'}
          />
        </View>

        <Animated.ScrollView
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
          style={{ opacity: fadeAnim }}
        >
          {isLoading ? (
            <View style={styles.loadingContainer}>
              <ActivityIndicator size="large" color={colors.accent} />
              <Text style={styles.loadingText}>Chargement...</Text>
            </View>
          ) : !hasProfile ? (
            // Profil non complété
            <View style={styles.emptyState}>
              <View style={styles.emptyIcon}>
                <Ionicons name="planet-outline" size={80} color={colors.textMuted} />
              </View>
              <Text style={styles.emptyTitle}>Profil requis</Text>
              <Text style={styles.emptyText}>
                Complétez votre profil astral pour calculer votre thème natal
              </Text>
              <TouchableOpacity 
                style={styles.emptyButton}
                onPress={() => router.push('/(tabs)/profile')}
                activeOpacity={0.8}
              >
                <LinearGradient colors={colors.ctaGradient} style={styles.emptyButtonGradient}>
                  <Ionicons name="person-add" size={20} color="white" />
                  <Text style={styles.emptyButtonText}>Compléter mon profil</Text>
                </LinearGradient>
              </TouchableOpacity>
            </View>
          ) : (
            // Afficher le thème natal
            <>
              {/* Hero Card */}
              <View style={styles.heroCard}>
                <Text style={styles.heroEmoji}>{positions?.sun?.emoji || '⭐'}</Text>
                <Text style={styles.heroTitle}>{profile.name}</Text>
                <Text style={styles.heroSubtitle}>
                  {positions?.sun?.sign || 'Signe'} • {positions?.sun?.element || 'Élément'}
                </Text>
              </View>

              {/* Carte circulaire */}
              {positions && (
                <View style={styles.section}>
                  <Text style={styles.sectionTitle}>Carte du ciel</Text>
                  
                  <View style={styles.chartCard}>
                    <ZodiacWheel positions={positions} />
                  </View>
                </View>
              )}

              {/* Disclaimer V1 */}
              {positions && (
                <View style={styles.disclaimerCard}>
                  <Ionicons name="information-circle" size={20} color={colors.warning} />
                  <Text style={styles.disclaimerText}>
                    ⚠️ Version simplifiée (V1) : Soleil et Lune précis. Ascendant approximatif (±10°). 
                    Pour précision professionnelle, consultez Astrotheme.com
                  </Text>
                </View>
              )}

              {/* Positions planétaires */}
              {positions && (
                <View style={styles.section}>
                  <Text style={styles.sectionTitle}>Positions planétaires</Text>
                  
                  <PlanetCard
                    icon="sunny"
                    planet="Soleil"
                    position={positions.sun}
                    color={colors.accent}
                    precise
                  />
                  <PlanetCard
                    icon="moon"
                    planet="Lune"
                    position={positions.moon}
                    color={colors.primary}
                    precise
                  />
                  <PlanetCard
                    icon="arrow-up"
                    planet="Ascendant"
                    position={positions.ascendant}
                    color={colors.secondary}
                    approximate
                  />
                  {positions.mercury && (
                    <PlanetCard
                      icon="flash"
                      planet="Mercure"
                      position={positions.mercury}
                      color="#10B981"
                    />
                  )}
                  {positions.venus && (
                    <PlanetCard
                      icon="heart"
                      planet="Vénus"
                      position={positions.venus}
                      color="#EC4899"
                    />
                  )}
                  {positions.mars && (
                    <PlanetCard
                      icon="flame"
                      planet="Mars"
                      position={positions.mars}
                      color="#EF4444"
                    />
                  )}
                </View>
              )}

              {/* Bouton calculer */}
              <TouchableOpacity 
                style={styles.computeButton}
                onPress={handleCompute}
                disabled={isComputing}
                activeOpacity={0.8}
              >
                <LinearGradient colors={colors.ctaGradient} style={styles.computeButtonGradient}>
                  {isComputing ? (
                    <>
                      <ActivityIndicator color="white" />
                      <Text style={styles.computeButtonText}>Calcul en cours...</Text>
                    </>
                  ) : (
                    <>
                      <Ionicons name="refresh" size={24} color="white" />
                      <Text style={styles.computeButtonText}>
                        {natalChart ? 'Recalculer' : 'Calculer mon thème'}
                      </Text>
                    </>
                  )}
                </LinearGradient>
              </TouchableOpacity>

              {natalChart && (
                <Text style={styles.disclaimer}>
                  Dernière mise à jour : {new Date(natalChart.computed_at || natalChart.created_at).toLocaleDateString('fr-FR')}
                  {'\n'}Source : {natalChart.meta?.provider || natalChart.version || 'API V1'}
                  {!useRapidAPI && '\n⚠️ Limite : 1 calcul par 24h'}
                </Text>
              )}

              {/* Bouton sauvegarder dans le profil */}
              {positions && positions.sun && positions.moon && positions.ascendant && (
                <TouchableOpacity
                  style={styles.saveButton}
                  onPress={handleSaveToProfile}
                  disabled={isSaving}
                  activeOpacity={0.8}
                >
                  <View style={styles.saveButtonContent}>
                    <Ionicons 
                      name={isSaving ? "hourglass" : profile.ascendant ? "checkmark-circle" : "save"} 
                      size={20} 
                      color={profile.ascendant ? "#10B981" : "#8B5CF6"} 
                    />
                    <Text style={[styles.saveButtonText, profile.ascendant && styles.saveButtonTextSaved]}>
                      {isSaving ? 'Sauvegarde...' : profile.ascendant ? '✓ Sauvegardé dans le profil' : 'Sauvegarder dans mon profil'}
                    </Text>
                  </View>
                  {!profile.ascendant && (
                    <Text style={styles.saveButtonHint}>
                      Ces données seront utilisées pour pré-remplir vos analyses
                    </Text>
                  )}
                </TouchableOpacity>
              )}
            </>
          )}
        </Animated.ScrollView>
      </SafeAreaView>
    </LinearGradient>
  );
}

// Composant Roue du zodiaque
function ZodiacWheel({ positions }) {
  const signs = ['♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑', '♒', '♓'];
  const radius = 90; // Rayon du cercle de placement des planètes
  
  // Fonction pour convertir longitude en position x,y
  const getPlanetPosition = (longitude) => {
    // Convertir en radians (0° = haut, rotation horaire)
    const angle = (longitude - 90) * (Math.PI / 180);
    const x = radius * Math.cos(angle);
    const y = radius * Math.sin(angle);
    return { left: 110 + x, top: 110 + y }; // 110 = rayon du cercle / 2 + marge
  };
  
  return (
    <View style={styles.wheel}>
      <View style={styles.wheelInner}>
        {/* Cercle central */}
        <View style={styles.centerCircle}>
          <Text style={styles.centerText}>Carte{'\n'}du ciel</Text>
        </View>
        
        {/* Marqueurs planètes positionnés en cercle */}
        {positions.sun && (
          <View style={[styles.planetMarker, getPlanetPosition(positions.sun.longitude)]}>
            <Text style={styles.planetIcon}>☀️</Text>
          </View>
        )}
        {positions.moon && (
          <View style={[styles.planetMarker, getPlanetPosition(positions.moon.longitude)]}>
            <Text style={styles.planetIcon}>🌙</Text>
          </View>
        )}
        {positions.ascendant && (
          <View style={[styles.planetMarker, getPlanetPosition(positions.ascendant.longitude)]}>
            <Text style={styles.planetIcon}>⬆️</Text>
          </View>
        )}
      </View>
      
      {/* Signes du zodiaque autour */}
      <View style={styles.signsRing}>
        {signs.map((sign, i) => {
          const angle = (i * 30 - 90) * (Math.PI / 180); // 30° par signe, départ à 90°
          const signRadius = 120;
          const x = signRadius * Math.cos(angle);
          const y = signRadius * Math.sin(angle);
          return (
            <Text 
              key={i} 
              style={[
                styles.signLabel,
                { 
                  position: 'absolute',
                  left: 110 + x,
                  top: 110 + y,
                }
              ]}
            >
              {sign}
            </Text>
          );
        })}
      </View>
    </View>
  );
}

// Composant carte de planète
function PlanetCard({ icon, planet, position, color, precise, approximate }) {
  if (!position) return null;
  
  return (
    <View style={styles.planetCard}>
      <View style={[styles.planetIcon, { backgroundColor: `${color}33` }]}>
        <Ionicons name={icon} size={24} color={color} />
      </View>
      <View style={styles.planetContent}>
        <Text style={styles.planetName}>
          {planet}
          {precise && <Text style={styles.preciseTag}> ✓</Text>}
          {approximate && <Text style={styles.approximateTag}> ~</Text>}
        </Text>
        <Text style={styles.planetPosition}>
          {position.emoji} {position.sign} - {position.degree}°{position.minutes}'
        </Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1 },
  safeArea: { flex: 1 },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.md,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(139, 92, 246, 0.3)',
  },
  backButton: { width: 40, height: 40, alignItems: 'center', justifyContent: 'center' },
  headerTitle: { fontSize: fonts.sizes.xl, color: colors.text, fontWeight: 'bold' },
  placeholder: { width: 40 },
  apiToggleContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.sm,
    backgroundColor: 'rgba(139, 92, 246, 0.1)',
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(139, 92, 246, 0.2)',
  },
  apiToggleLabel: {
    fontSize: fonts.sizes.sm,
    color: colors.text,
    fontWeight: '600',
  },
  scrollContent: { padding: spacing.md },
  loadingContainer: { alignItems: 'center', paddingVertical: spacing.xxl * 2 },
  loadingText: { fontSize: fonts.sizes.md, color: colors.textMuted, marginTop: spacing.md },
  
  // Empty State
  emptyState: { alignItems: 'center', paddingVertical: spacing.xxl * 2 },
  emptyIcon: { marginBottom: spacing.lg },
  emptyTitle: { fontSize: fonts.sizes.xxl, color: colors.text, fontWeight: 'bold', marginBottom: spacing.sm },
  emptyText: { fontSize: fonts.sizes.md, color: colors.textMuted, textAlign: 'center', marginBottom: spacing.xl, paddingHorizontal: spacing.xl, lineHeight: 24 },
  emptyButton: { borderRadius: borderRadius.xl },
  emptyButtonGradient: { flexDirection: 'row', alignItems: 'center', paddingVertical: spacing.md, paddingHorizontal: spacing.lg, borderRadius: borderRadius.xl, gap: spacing.sm },
  emptyButtonText: { fontSize: fonts.sizes.md, color: 'white', fontWeight: 'bold' },
  
  // Hero
  heroCard: { alignItems: 'center', backgroundColor: colors.cardBg, padding: spacing.xl, borderRadius: borderRadius.lg, marginBottom: spacing.lg, borderWidth: 1, borderColor: 'rgba(139, 92, 246, 0.3)' },
  heroEmoji: { 
    fontSize: 64, 
    marginBottom: spacing.sm,
    // Halo doux autour du signe solaire
    textShadowColor: colors.accent || '#FFB347',
    textShadowOffset: { width: 0, height: 0 },
    textShadowRadius: 16,
  },
  heroTitle: { fontSize: fonts.sizes.xxl, color: colors.text, fontWeight: 'bold', marginBottom: spacing.xs },
  heroSubtitle: { fontSize: fonts.sizes.md, color: colors.textSecondary },
  
  // Section
  section: { marginBottom: spacing.lg },
  sectionTitle: { fontSize: fonts.sizes.lg, color: colors.text, fontWeight: 'bold', marginBottom: spacing.md + 8 }, // +8px pour aérer
  
  // Chart
  chartCard: { backgroundColor: colors.cardBg, borderRadius: borderRadius.lg, padding: spacing.lg, borderWidth: 1, borderColor: 'rgba(139, 92, 246, 0.3)', alignItems: 'center' },
  wheel: { width: 280, height: 280, position: 'relative', alignItems: 'center', justifyContent: 'center' },
  wheelInner: { width: 240, height: 240, borderRadius: 120, borderWidth: 2, borderColor: colors.primary, position: 'relative', alignItems: 'center', justifyContent: 'center' },
  centerCircle: { 
    width: 100, 
    height: 100, 
    borderRadius: 50, 
    backgroundColor: colors.cardBg, 
    alignItems: 'center', 
    justifyContent: 'center', 
    borderWidth: 1, 
    borderColor: colors.accent, 
    zIndex: 10,
    // Halo doux autour du cercle central
    shadowColor: colors.accent || '#FFB347',
    shadowOpacity: 0.6,
    shadowRadius: 16,
    shadowOffset: { width: 0, height: 0 },
    elevation: 8,
  },
  centerText: { fontSize: fonts.sizes.sm, color: colors.text, textAlign: 'center', fontWeight: '600' },
  planetMarker: { position: 'absolute', width: 30, height: 30, alignItems: 'center', justifyContent: 'center', zIndex: 5 },
  planetIcon: { fontSize: 24 },
  signsRing: { position: 'absolute', width: 280, height: 280 },
  signLabel: { fontSize: 20, color: colors.textMuted, fontWeight: 'bold', textShadowColor: 'rgba(0,0,0,0.5)', textShadowOffset: { width: 0, height: 1 }, textShadowRadius: 2 },
  
  // Planet Card
  planetCard: { flexDirection: 'row', backgroundColor: colors.cardBg, padding: spacing.md, borderRadius: borderRadius.lg, marginBottom: spacing.sm, borderWidth: 1, borderColor: 'rgba(139, 92, 246, 0.2)', gap: spacing.md },
  planetIcon: { width: 48, height: 48, borderRadius: borderRadius.md, alignItems: 'center', justifyContent: 'center' },
  planetContent: { flex: 1 },
  planetName: { fontSize: fonts.sizes.md, color: colors.text, fontWeight: 'bold', marginBottom: spacing.xs - 2 },
  planetPosition: { fontSize: fonts.sizes.sm, color: colors.textSecondary },
  
  // Compute Button
  computeButton: { borderRadius: borderRadius.xl, marginTop: spacing.md },
  computeButtonGradient: { flexDirection: 'row', alignItems: 'center', justifyContent: 'center', paddingVertical: spacing.md + 4, borderRadius: borderRadius.xl, gap: spacing.sm },
  computeButtonText: { fontSize: fonts.sizes.lg, color: 'white', fontWeight: 'bold' },
  disclaimer: { fontSize: fonts.sizes.xs, color: colors.textMuted, textAlign: 'center', marginTop: spacing.md },
  
  // Save Button
  saveButton: {
    backgroundColor: 'rgba(139, 92, 246, 0.15)',
    borderRadius: borderRadius.lg,
    padding: spacing.md,
    marginTop: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.3)',
  },
  saveButtonContent: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: spacing.sm,
  },
  saveButtonText: {
    fontSize: fonts.sizes.md,
    color: '#8B5CF6',
    fontWeight: '600',
  },
  saveButtonTextSaved: {
    color: '#10B981',
  },
  saveButtonHint: {
    fontSize: fonts.sizes.xs,
    color: 'rgba(139, 92, 246, 0.7)',
    textAlign: 'center',
    marginTop: spacing.xs,
    fontStyle: 'italic',
  },
  
  // Disclaimer
  disclaimerCard: {
    backgroundColor: 'rgba(245, 158, 11, 0.15)', // 0.1 → 0.15 pour fond plus opaque
    padding: spacing.sm,
    borderRadius: borderRadius.md,
    flexDirection: 'row',
    gap: spacing.sm,
    marginBottom: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(245, 158, 11, 0.3)',
  },
  disclaimerText: {
    flex: 1,
    fontSize: fonts.sizes.xs,
    color: colors.textSecondary,
    lineHeight: 18,
  },
  preciseTag: {
    fontSize: fonts.sizes.xs,
    color: colors.success,
  },
  approximateTag: {
    fontSize: fonts.sizes.xs,
    color: colors.warning,
  },
});
