/**
 * Écran de lecture complète de thème natal
 * Affiche Big 3, positions planétaires, aspects, et résumé
 */

import { useState, useEffect } from 'react';
import {
  View,
  Text,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
  StyleSheet,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { router } from 'expo-router';

import { getNatalReading, saveReadingLocally, filterAspectsByStrength, formatAspect } from '@/lib/services/natalReadingService';
import { color, space, type as typography, radius } from '@/theme/tokens';
import { translatePlanet, translateAspect, translateHouse, translateStrength } from '@/lib/utils/astrologyTranslations';
import { 
  generateAspectInterpretation, 
  generateBigThreeSummary,
  sortAspects,
  getSortedVisibleAspects,
  getAspectEmoji,
  getStrengthColor,
  MAJOR_ASPECTS,
} from '@/lib/utils/aspectInterpretations';
// Import des nouvelles fonctions (TypeScript)
// Metro bundler de React Native gère les imports .ts automatiquement
let isPersonalRelated;
let getReadableInterpretation;
let generateProfile;
let getUseGPTInterp;

try {
  const aspectCategories = require('@/lib/utils/aspectCategories');
  isPersonalRelated = aspectCategories.isPersonalRelated;
  
  const aspectTextTemplates = require('@/lib/utils/aspectTextTemplates');
  getReadableInterpretation = aspectTextTemplates.getReadableInterpretation;
  
  const profileGenerator = require('@/lib/utils/profileGenerator');
  generateProfile = profileGenerator.generateProfile;
  getUseGPTInterp = profileGenerator.getUseGPTInterp || (() => false);
} catch (err) {
  console.warn('[NatalReading] Erreur import nouveaux modules, utilisation fallback:', err);
  // Fallback: utiliser les anciennes fonctions
  isPersonalRelated = (asp) => {
    const PERSONAL = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Ascendant', 'Medium_Coeli'];
    return PERSONAL.includes(asp.from) || PERSONAL.includes(asp.to);
  };
  getReadableInterpretation = (asp) => {
    // Utiliser l'ancienne fonction
    return generateAspectInterpretation(asp);
  };
  generateProfile = async (data) => {
    return generateBigThreeSummary(data.big_three);
  };
  getUseGPTInterp = () => false;
}

export default function NatalReadingScreen() {
  const [loading, setLoading] = useState(false);
  const [reading, setReading] = useState(null);
  const [error, setError] = useState(null);
  const [showAllAspects, setShowAllAspects] = useState(false);
  const [profileText, setProfileText] = useState(null);

  // Reset et retour au setup
  const resetAndGoToSetup = async () => {
    try {
      await AsyncStorage.removeItem('user_birth_data');
      await AsyncStorage.removeItem('natal_reading');
      console.log('[NatalReading] 🗑️ Données effacées, retour au setup');
      router.replace('/natal-reading/setup');
    } catch (error) {
      console.error('[NatalReading] Erreur reset:', error);
    }
  };

  useEffect(() => {
    checkBirthDataAndLoad();
  }, []);

  // Générer le profil astrologique (nouvelle version avec templates/GPT)
  useEffect(() => {
    if (reading && reading.summary && reading.summary.big_three) {
      const { big_three, dominant_element } = reading.summary;
      const { positions = [] } = reading;
      
      generateProfile({
        big_three,
        dominant_element,
        positions,
      }).then(profile => {
        setProfileText(profile);
      }).catch(err => {
        console.error('[NatalReading] Erreur génération profil:', err);
        // Fallback sur l'ancienne version
        if (big_three) {
          const fallback = generateBigThreeSummary(big_three);
          setProfileText(fallback);
        } else {
          setProfileText(null);
        }
      });
    } else {
      setProfileText(null);
    }
  }, [reading]);

  const checkBirthDataAndLoad = async () => {
    try {
      setLoading(true);

      // Vérifier si les données de naissance existent
      const birthDataStr = await AsyncStorage.getItem('user_birth_data');
      
      if (!birthDataStr) {
        // Rediriger vers le setup
        console.log('[NatalReading] Aucune donnée de naissance → redirection setup');
        router.replace('/natal-reading/setup');
        return;
      }

      // Charger la lecture
      await loadReading();

    } catch (error) {
      console.error('[NatalReading] Erreur vérification:', error);
      setError(error.message);
      setLoading(false);
    }
  };

  const loadReading = async () => {
    try {
      setLoading(true);
      setError(null);

      // Récupérer les données de naissance depuis AsyncStorage
      const birthDataStr = await AsyncStorage.getItem('user_birth_data');
      
      if (!birthDataStr) {
        router.replace('/natal-reading/setup');
        return;
      }

      const birthData = JSON.parse(birthDataStr);

      // Appeler l'API avec force_refresh=false (utilise le cache)
      const data = await getNatalReading(birthData, {
        language: 'fr',
        force_refresh: false,
        include_interpretations: true,
      });

      setReading(data);
      await saveReadingLocally(data);

    } catch (err) {
      console.error('[NatalReading] Erreur:', err);
      setError(err.message || 'Erreur lors du chargement');
    } finally {
      setLoading(false);
    }
  };

  const refreshReading = async () => {
    try {
      setLoading(true);
      setError(null);

      const birthDataStr = await AsyncStorage.getItem('user_birth_data');
      const birthData = JSON.parse(birthDataStr);

      // Force un nouvel appel API
      const data = await getNatalReading(birthData, {
        language: 'fr',
        force_refresh: true,
        include_interpretations: true,
      });

      setReading(data);
      await saveReadingLocally(data);

    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color={color.primary} />
          <Text style={styles.loadingText}>Calcul de votre thème natal...</Text>
        </View>
      </SafeAreaView>
    );
  }

  if (error) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.errorContainer}>
          <Text style={styles.errorText}>❌ {error}</Text>
          <TouchableOpacity style={styles.retryButton} onPress={loadReading}>
            <Text style={styles.retryButtonText}>Réessayer</Text>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    );
  }

  if (!reading) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.errorContainer}>
          <Text style={styles.emptyText}>Aucun thème natal disponible</Text>
          <TouchableOpacity style={styles.retryButton} onPress={loadReading}>
            <Text style={styles.retryButtonText}>Charger</Text>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    );
  }

  const { positions = [], aspects = [], interpretations, summary, source, api_calls_count, created_at } = reading || {};
  const { big_three, personality_highlights, dominant_element } = summary || {};

  // Helper pour obtenir les aspects visibles triés (applique tri APRÈS filtrage)
  const allSortedAspects = getSortedVisibleAspects(aspects || [], false);
  
  // Aspects clés : stratégie de sélection améliorée
  // Objectif : Toujours montrer 7 aspects, avec minimum 4 aspects personnels
  // IMPORTANT : Les aspects candidats sont déjà triés par sortAspects()
  
  // Étape 1 : Filtrer les aspects candidats (majeurs + non weak) depuis les aspects triés
  const candidateAspects = allSortedAspects.filter(asp => {
    const isMajor = MAJOR_ASPECTS.includes(asp.aspect_type?.toLowerCase());
    const isNotWeak = asp.strength?.toLowerCase() !== 'weak';
    return isMajor && isNotWeak;
  });
  
  // Étape 2 : Séparer les aspects personnels des non-personnels
  // Ils sont déjà triés par sortAspects(), donc l'ordre est préservé
  const personalAspects = candidateAspects.filter(asp => isPersonalRelated(asp));
  const nonPersonalAspects = candidateAspects.filter(asp => !isPersonalRelated(asp));
  
  // Étape 3 : Construire keyAspects avec garantie de 7 aspects
  let keyAspects = [];
  
  // Stratégie : garantir au moins 4 aspects personnels, puis compléter jusqu'à 7
  if (personalAspects.length >= 4) {
    // Cas idéal : on a au moins 4 aspects personnels
    // Prendre 4 aspects personnels minimum (déjà triés)
    keyAspects = keyAspects.concat(personalAspects.slice(0, 4));
    
    // Compléter jusqu'à 7 : prioriser les aspects personnels supplémentaires, puis non-personnels
    const remainingSlots = 7 - keyAspects.length;
    if (personalAspects.length > 4) {
      // Prendre des aspects personnels supplémentaires s'il y en a
      const additionalPersonal = Math.min(remainingSlots, personalAspects.length - 4);
      keyAspects = keyAspects.concat(personalAspects.slice(4, 4 + additionalPersonal));
    }
    
    // Compléter avec des non-personnels si nécessaire
    const finalRemainingSlots = 7 - keyAspects.length;
    if (finalRemainingSlots > 0) {
      keyAspects = keyAspects.concat(nonPersonalAspects.slice(0, finalRemainingSlots));
    }
  } else {
    // Cas limite : moins de 4 aspects personnels disponibles
    // Prendre tous les aspects personnels disponibles
    keyAspects = keyAspects.concat(personalAspects);
    
    // Compléter avec des non-personnels pour atteindre 7
    const remainingSlots = 7 - keyAspects.length;
    if (remainingSlots > 0) {
      keyAspects = keyAspects.concat(nonPersonalAspects.slice(0, remainingSlots));
    }
  }
  
  // Limiter strictement à 7 maximum
  keyAspects = keyAspects.slice(0, 7);
  
  // Étape 4 : Validation finale (s'assurer qu'on respecte toujours les filtres)
  keyAspects = keyAspects.filter(asp => {
    const isMajor = MAJOR_ASPECTS.includes(asp.aspect_type?.toLowerCase());
    const isNotWeak = asp.strength?.toLowerCase() !== 'weak';
    return isMajor && isNotWeak;
  }).slice(0, 7);
  
  // Créer un Set des IDs des aspects clés pour éviter les doublons
  const keyAspectIds = new Set(
    keyAspects.map(asp => `${asp.from}-${asp.to}-${asp.aspect_type}`)
  );
  
  // Aspects filtrés pour la liste complète
  // IMPORTANT : Utiliser getSortedVisibleAspects() pour garantir le tri APRÈS le filtrage
  // Cela garantit que l'ordre reste strict même quand on toggle "masquer aspects faibles"
  const filteredAspects = getSortedVisibleAspects(
    (aspects || []).filter(asp => {
      const aspectId = `${asp.from}-${asp.to}-${asp.aspect_type}`;
      return !keyAspectIds.has(aspectId);
    }),
    !showAllAspects // hideWeak = true si showAllAspects = false
  );
  
  // Total d'aspects affichés (clés + filtrés)
  const totalDisplayed = keyAspects.length + filteredAspects.length;
  
  // Utiliser le nouveau profil si disponible, sinon fallback sur l'ancien
  const displayProfile = profileText || (big_three ? generateBigThreeSummary(big_three) : null);

  // Interprétations disponibles (safe check)
  const hasInterpretations = interpretations && typeof interpretations === 'object' && (
    Object.keys(interpretations.positions_interpretations || {}).length > 0 ||
    interpretations.general_summary
  );

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView
        style={styles.scrollView}
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        {/* Header */}
        <View style={styles.header}>
          <View style={styles.headerTop}>
            <TouchableOpacity onPress={() => router.back()} style={styles.backButton}>
              <Text style={styles.backButtonText}>← Retour</Text>
            </TouchableOpacity>
            <TouchableOpacity onPress={resetAndGoToSetup} style={styles.resetButton}>
              <Text style={styles.resetButtonText}>⚙️ Modifier</Text>
            </TouchableOpacity>
          </View>
          <Text style={styles.title}>🌟 Thème Natal</Text>
          <Text style={styles.subtitle}>{reading.subject_name}</Text>
          <Text style={styles.sourceInfo}>
            {source === 'cache' ? '💾 Depuis le cache' : '🌐 Nouvellement calculé'} 
            {api_calls_count !== undefined && api_calls_count > 0 && ` • ${api_calls_count} appel${api_calls_count > 1 ? 's' : ''} API`}
          </Text>
        </View>

        {/* Big Three */}
        {big_three?.sun && (
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>🌟 Big Three</Text>
            
            <View style={styles.bigThreeContainer}>
              <View style={styles.bigThreeCard}>
                <Text style={styles.bigThreeEmoji}>{big_three.sun.emoji}</Text>
                <Text style={styles.bigThreeLabel}>Soleil</Text>
                <Text style={styles.bigThreeSign}>{big_three.sun.sign_fr}</Text>
                <Text style={styles.bigThreeDegree}>{big_three.sun.degree}°</Text>
                <Text style={styles.bigThreeElement}>({big_three.sun.element})</Text>
              </View>

              <View style={styles.bigThreeCard}>
                <Text style={styles.bigThreeEmoji}>{big_three.moon?.emoji}</Text>
                <Text style={styles.bigThreeLabel}>Lune</Text>
                <Text style={styles.bigThreeSign}>{big_three.moon?.sign_fr}</Text>
                <Text style={styles.bigThreeDegree}>{big_three.moon?.degree}°</Text>
                <Text style={styles.bigThreeElement}>({big_three.moon?.element})</Text>
              </View>

              <View style={styles.bigThreeCard}>
                <Text style={styles.bigThreeEmoji}>{big_three.ascendant?.emoji}</Text>
                <Text style={styles.bigThreeLabel}>Ascendant</Text>
                <Text style={styles.bigThreeSign}>{big_three.ascendant?.sign_fr}</Text>
                <Text style={styles.bigThreeDegree}>{big_three.ascendant?.degree}°</Text>
                <Text style={styles.bigThreeElement}>({big_three.ascendant?.element})</Text>
              </View>
            </View>
          </View>
        )}

        {/* Résumé */}
        {(dominant_element || personality_highlights?.length > 0) && (
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>📊 Résumé</Text>
            <View style={styles.summaryCard}>
              {dominant_element && (
                <View style={styles.summaryRow}>
                  <Text style={styles.summaryLabel}>Élément dominant</Text>
                  <Text style={styles.summaryValue}>{dominant_element}</Text>
                </View>
              )}
              {personality_highlights?.length > 0 && (
                <View style={styles.summaryRow}>
                  <Text style={styles.summaryLabel}>Traits clés</Text>
                  <Text style={styles.summaryValue}>{personality_highlights.join(' • ')}</Text>
                </View>
              )}
            </View>
          </View>
        )}

        {/* Profil Astrologique (nouvelle version) */}
        {displayProfile && (
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>📖 Votre Profil Astrologique</Text>
            <View style={styles.interpretationCard}>
              <Text style={styles.interpretationText}>{displayProfile}</Text>
            </View>
          </View>
        )}

        {/* Résumé général (interprétation API si disponible) */}
        {interpretations?.general_summary && (
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>✨ Analyse Détaillée</Text>
            <View style={styles.interpretationCard}>
              <Text style={styles.interpretationText}>{interpretations.general_summary}</Text>
            </View>
          </View>
        )}

        {/* Positions planétaires */}
        {positions?.length > 0 && (() => {
          // Ordre préféré pour l'affichage des positions planétaires
          const PREFERRED_ORDER = [
            'Sun',
            'Ascendant',
            'Moon',
            'Medium_Coeli',
            'Mercury',
            'Venus',
            'Mars',
            'Jupiter',
            'Saturn',
          ];
          
          const getPositionIndex = (posName) => {
            const i = PREFERRED_ORDER.indexOf(posName);
            return i === -1 ? 999 : i; // Les planètes non listées vont à la fin
          };
          
          const sortedPositions = positions.slice().sort(
            (a, b) => getPositionIndex(a.name) - getPositionIndex(b.name)
          );
          
          return (
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>🪐 Positions Planétaires ({positions.length})</Text>
              {sortedPositions.map((planet, index) => {
              const planetInterp = interpretations?.positions_interpretations?.[planet.name];
              
              return (
                <View key={index} style={styles.planetCard}>
                  <View style={styles.planetHeader}>
                    <Text style={styles.planetEmoji}>{planet.emoji}</Text>
                    <Text style={styles.planetName}>{translatePlanet(planet.name)}</Text>
                    {planet.is_retrograde && (
                      <View style={styles.retroBadge}>
                        <Text style={styles.retroText}>R</Text>
                      </View>
                    )}
                  </View>
                  <View style={styles.planetDetails}>
                    <Text style={styles.planetSign}>{planet.sign_fr} {planet.degree.toFixed(2)}°</Text>
                    <Text style={styles.planetHouse}>{translateHouse(planet.house)}</Text>
                    <Text style={styles.planetElement}>{planet.element}</Text>
                  </View>
                  
                  {/* Interprétation de la position */}
                  {planetInterp && (
                    <View style={styles.planetInterpretation}>
                      {planetInterp.in_sign && (
                        <Text style={styles.interpText}>• {planetInterp.in_sign}</Text>
                      )}
                      {planetInterp.in_house && (
                        <Text style={styles.interpText}>• {planetInterp.in_house}</Text>
                      )}
                      {planetInterp.overall && (
                        <Text style={styles.interpText}>{planetInterp.overall}</Text>
                      )}
                    </View>
                  )}
                </View>
              );
              })}
            </View>
          );
        })()}

        {/* Aspects clés du thème */}
        {keyAspects?.length > 0 && (
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>🔗 Aspects clés du thème</Text>
            <Text style={styles.aspectsSubtitle}>
              Les aspects clés résument les influences les plus marquantes de ton thème.
            </Text>
            
            {keyAspects.map((aspect, index) => {
              const interpretation = getReadableInterpretation(aspect, { useGPT: getUseGPTInterp() });
              const strengthColor = getStrengthColor(aspect.strength);
              const strengthTextColor = aspect.strength === 'strong' 
                ? color.successText 
                : aspect.strength === 'medium' 
                  ? color.warningText 
                  : color.weakText;
              
              return (
                <View key={`key-${index}`} style={styles.aspectCard}>
                  <View style={styles.aspectHeader}>
                    <Text style={styles.aspectType}>
                      {getAspectEmoji(aspect.aspect_type)} {translateAspect(aspect.aspect_type)}
                    </Text>
                    <View style={[styles.strengthBadge, { backgroundColor: strengthColor }]}>
                      <Text style={[styles.strengthText, { color: strengthTextColor }]}>
                        {translateStrength(aspect.strength)}
                      </Text>
                    </View>
                  </View>
                  <Text style={styles.aspectDetails}>
                    {translatePlanet(aspect.from)} → {translatePlanet(aspect.to)}
                  </Text>
                  <Text style={styles.aspectOrb}>Orbe : {Math.abs(aspect.orb).toFixed(2)}°</Text>
                  
                  {/* Mini-interprétation */}
                  <View style={styles.aspectInterpretation}>
                    <Text style={styles.aspectInterpretationText}>{interpretation}</Text>
                  </View>
                </View>
              );
            })}
          </View>
        )}

        {/* Aspects clés du thème */}
        {keyAspects?.length > 0 && (
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>🔗 Aspects clés du thème</Text>
            <Text style={styles.aspectsSubtitle}>
              Les aspects clés résument les influences les plus marquantes de ton thème.
            </Text>
            
            {keyAspects.map((aspect, index) => {
              const interpretation = getReadableInterpretation(aspect, { useGPT: getUseGPTInterp() });
              const strengthColor = getStrengthColor(aspect.strength);
              const strengthTextColor = aspect.strength === 'strong' 
                ? color.successText 
                : aspect.strength === 'medium' 
                  ? color.warningText 
                  : color.weakText;
              
              return (
                <View key={`key-${index}`} style={styles.aspectCard}>
                  <View style={styles.aspectHeader}>
                    <Text style={styles.aspectType}>
                      {getAspectEmoji(aspect.aspect_type)} {translateAspect(aspect.aspect_type)}
                    </Text>
                    <View style={[styles.strengthBadge, { backgroundColor: strengthColor }]}>
                      <Text style={[styles.strengthText, { color: strengthTextColor }]}>
                        {translateStrength(aspect.strength)}
                      </Text>
                    </View>
                  </View>
                  <Text style={styles.aspectDetails}>
                    {translatePlanet(aspect.from)} → {translatePlanet(aspect.to)}
                  </Text>
                  <Text style={styles.aspectOrb}>Orbe : {Math.abs(aspect.orb).toFixed(2)}°</Text>
                  
                  {/* Mini-interprétation */}
                  <View style={styles.aspectInterpretation}>
                    <Text style={styles.aspectInterpretationText}>{interpretation}</Text>
                  </View>
                </View>
              );
            })}
          </View>
        )}

        {/* Aspects (liste complète) */}
        {aspects?.length > 0 && filteredAspects.length > 0 && (
          <View style={styles.section}>
            <View style={styles.aspectsHeader}>
              <Text style={styles.sectionTitle}>
                🔗 Aspects ({totalDisplayed}/{aspects?.length || 0})
              </Text>
              <TouchableOpacity onPress={() => setShowAllAspects(!showAllAspects)}>
                <Text style={styles.toggleText}>
                  {showAllAspects ? '🔽 Masquer aspects faibles' : '🔼 Tout afficher'}
                </Text>
              </TouchableOpacity>
            </View>
            
            {filteredAspects.map((aspect, index) => {
              const interpretation = getReadableInterpretation(aspect, { useGPT: getUseGPTInterp() });
              const strengthColor = getStrengthColor(aspect.strength);
              const strengthTextColor = aspect.strength === 'strong' 
                ? color.successText 
                : aspect.strength === 'medium' 
                  ? color.warningText 
                  : color.weakText;
              
              return (
                <View key={`all-${index}`} style={styles.aspectCard}>
                  <View style={styles.aspectHeader}>
                    <Text style={styles.aspectType}>
                      {getAspectEmoji(aspect.aspect_type)} {translateAspect(aspect.aspect_type)}
                    </Text>
                    <View style={[styles.strengthBadge, { backgroundColor: strengthColor }]}>
                      <Text style={[styles.strengthText, { color: strengthTextColor }]}>
                        {translateStrength(aspect.strength)}
                      </Text>
                    </View>
                  </View>
                  <Text style={styles.aspectDetails}>
                    {translatePlanet(aspect.from)} → {translatePlanet(aspect.to)}
                  </Text>
                  <Text style={styles.aspectOrb}>Orbe : {Math.abs(aspect.orb).toFixed(2)}°</Text>
                  
                  {/* Mini-interprétation */}
                  <View style={styles.aspectInterpretation}>
                    <Text style={styles.aspectInterpretationText}>{interpretation}</Text>
                  </View>
                </View>
              );
            })}
          </View>
        )}

        {/* Actions */}
        <View style={styles.actionsContainer}>
          <TouchableOpacity
            style={styles.refreshButton}
            onPress={refreshReading}
            disabled={loading}
          >
            <Text style={styles.refreshButtonText}>
              🔄 Rafraîchir
            </Text>
          </TouchableOpacity>
        </View>

        {/* Footer */}
        <View style={styles.footer}>
          <Text style={styles.footerText}>
            Données calculées via Best Astrology API
          </Text>
          <Text style={styles.footerText}>
            Outil de bien-être, non médical
          </Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

// Pas besoin de redéfinir ces helpers, on les importe depuis aspectInterpretations

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: color.bg,
  },
  scrollView: {
    flex: 1,
  },
  scrollContent: {
    padding: space.md,
    paddingBottom: space.xl * 2,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  loadingText: {
    marginTop: space.md,
    ...typography.body,
    color: color.textMuted,
  },
  errorContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: space.lg,
  },
  errorText: {
    ...typography.body,
    color: color.danger,
    textAlign: 'center',
    marginBottom: space.lg,
  },
  emptyText: {
    ...typography.body,
    color: color.textMuted,
    textAlign: 'center',
    marginBottom: space.lg,
  },
  retryButton: {
    backgroundColor: color.brand,
    paddingHorizontal: space.lg,
    paddingVertical: space.md,
    borderRadius: radius.lg,
  },
  retryButtonText: {
    ...typography.bodyMd,
    fontWeight: '600',
    color: '#FFFFFF',
  },
  header: {
    marginBottom: space.lg,
  },
  headerTop: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: space.sm,
  },
  backButton: {
    padding: space.xs,
  },
  backButtonText: {
    ...typography.body,
    color: color.brand,
  },
  resetButton: {
    padding: space.xs,
  },
  resetButtonText: {
    ...typography.bodySm,
    color: color.textMuted,
  },
  title: {
    ...typography.h1,
    color: color.text,
    marginBottom: space.xs,
  },
  subtitle: {
    ...typography.h3,
    color: color.textSecondary,
    marginBottom: space.xs,
  },
  sourceInfo: {
    ...typography.caption,
    color: color.textMuted,
  },
  section: {
    marginBottom: space.lg,
  },
  sectionTitle: {
    ...typography.h3,
    color: color.text,
    marginBottom: space.md,
  },
  
  // Big Three
  bigThreeContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    gap: space.sm,
  },
  bigThreeCard: {
    flex: 1,
    backgroundColor: color.surfaceElevated,
    borderRadius: radius.xl,
    padding: space.md,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: color.border,
  },
  bigThreeEmoji: {
    fontSize: 32,
    marginBottom: space.xs,
  },
  bigThreeLabel: {
    ...typography.caption,
    color: color.textMuted,
    marginBottom: space.xs,
  },
  bigThreeSign: {
    ...typography.bodyMd,
    fontWeight: '600',
    color: color.text,
  },
  bigThreeDegree: {
    ...typography.bodySm,
    color: color.textMuted,
  },
  bigThreeElement: {
    ...typography.caption,
    color: color.textDisabled,
  },

  // Résumé
  summaryCard: {
    backgroundColor: color.surfaceElevated,
    borderRadius: radius.xl,
    padding: space.md,
    borderWidth: 1,
    borderColor: color.border,
  },
  summaryRow: {
    marginBottom: space.sm,
  },
  summaryLabel: {
    ...typography.bodySm,
    fontWeight: '500',
    color: color.textMuted,
    marginBottom: space.xs,
  },
  summaryValue: {
    ...typography.body,
    color: color.text,
  },

  // Interprétations
  interpretationCard: {
    backgroundColor: color.surfaceElevated,
    borderRadius: radius.xl,
    padding: space.md,
    borderWidth: 1,
    borderColor: color.border,
  },
  interpretationText: {
    ...typography.body,
    color: color.text,
    lineHeight: 22,
  },

  // Planètes
  planetCard: {
    backgroundColor: color.surfaceElevated,
    borderRadius: radius.lg,
    padding: space.md,
    marginBottom: space.sm,
    borderWidth: 1,
    borderColor: color.border,
  },
  planetHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: space.xs,
  },
  planetEmoji: {
    fontSize: 24,
    marginRight: space.sm,
  },
  planetName: {
    ...typography.bodyMd,
    fontWeight: '600',
    color: color.text,
    flex: 1,
  },
  retroBadge: {
    backgroundColor: color.warning,
    borderRadius: radius.sm,
    paddingHorizontal: space.xs,
    paddingVertical: 2,
  },
  retroText: {
    fontSize: 10,
    fontWeight: '700',
    color: color.warningText,
  },
  planetDetails: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  planetSign: {
    ...typography.bodySm,
    fontWeight: '500',
    color: color.text,
    flex: 2,
  },
  planetHouse: {
    ...typography.bodySm,
    color: color.textMuted,
    flex: 1,
    textAlign: 'center',
  },
  planetElement: {
    ...typography.caption,
    color: color.textDisabled,
    flex: 1,
    textAlign: 'right',
  },
  planetInterpretation: {
    marginTop: space.sm,
    paddingTop: space.sm,
    borderTopWidth: 1,
    borderTopColor: color.border,
  },
  interpText: {
    ...typography.caption,
    color: color.textMuted,
    lineHeight: 16,
    marginBottom: space.xs,
  },

  // Aspects
  aspectsHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: space.md,
  },
  aspectsSubtitle: {
    ...typography.caption,
    color: color.textMuted,
    marginBottom: space.md,
    fontStyle: 'italic',
  },
  toggleText: {
    ...typography.bodySm,
    fontWeight: '600',
    color: color.brand,
  },
  aspectCard: {
    backgroundColor: color.surfaceElevated,
    borderRadius: radius.lg,
    padding: space.md,
    marginBottom: space.sm,
    borderWidth: 1,
    borderColor: color.border,
  },
  aspectHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: space.xs,
  },
  aspectType: {
    ...typography.bodySm,
    fontWeight: '600',
    color: color.text,
  },
  strengthBadge: {
    borderRadius: radius.sm,
    paddingHorizontal: space.sm,
    paddingVertical: 4,
  },
  strengthText: {
    fontSize: 11,
    fontWeight: '600',
    // Couleur définie dynamiquement selon l'intensité
    textTransform: 'capitalize',
  },
  aspectDetails: {
    ...typography.bodySm,
    color: color.textMuted,
    marginBottom: 2,
  },
  aspectOrb: {
    ...typography.caption,
    color: color.textDisabled,
  },
  aspectInterpretation: {
    marginTop: space.sm,
    paddingTop: space.sm,
    borderTopWidth: 1,
    borderTopColor: color.border,
  },
  aspectInterpretationText: {
    ...typography.caption,
    color: color.textMuted,
    lineHeight: 18,
    fontStyle: 'italic',
  },

  // Actions
  actionsContainer: {
    marginTop: space.md,
    marginBottom: space.lg,
  },
  refreshButton: {
    backgroundColor: color.surfaceElevated,
    borderWidth: 2,
    borderColor: color.brand,
    paddingVertical: space.md,
    borderRadius: radius.lg,
    alignItems: 'center',
  },
  refreshButtonText: {
    ...typography.bodyMd,
    fontWeight: '600',
    color: color.brand,
  },

  // Footer
  footer: {
    alignItems: 'center',
    paddingTop: space.lg,
    paddingBottom: space.md,
  },
  footerText: {
    ...typography.caption,
    color: color.textDisabled,
    textAlign: 'center',
  },
});
