import React, { useState, useEffect, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Animated,
  ActivityIndicator,
  SafeAreaView,
  Alert,
  Modal,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { Ionicons } from '@expo/vector-icons';
import { Stack, router, useFocusEffect } from 'expo-router';
import { useCallback } from 'react';
import { useProfileStore } from '@/stores/profileStore';
import { getDashboardStats, getFullHistory, deleteAnalysis } from '@/lib/api/dashboardService';
import { SkeletonCard } from '@/components/SkeletonLoader';
import { EmptyState } from '@/components/EmptyState';
import { MoodCycleChart } from '@/components/charts/MoodCycleChart';
import { EnergyCycleChart } from '@/components/charts/EnergyCycleChart';
import { generateInsights } from '@/lib/services/chartDataService';
import { trackEvents } from '@/lib/analytics';
import THEME from '@/constants/theme';

export default function DashboardScreen() {
  const profile = useProfileStore((state) => state.profile);
  const [stats, setStats] = useState(null);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState('all'); // all, parent-child, couple, friends, colleagues, cycle-astro
  const [selectedAnalysis, setSelectedAnalysis] = useState(null);
  const [insights, setInsights] = useState([]);

  const fadeAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    loadDashboard();
  }, []);

  // Recharger quand on revient sur le screen
  useFocusEffect(
    useCallback(() => {
      console.log('[Dashboard] Screen focused, reloading...');
      loadDashboard();
    }, [])
  );

  useEffect(() => {
    if (stats) {
      Animated.timing(fadeAnim, {
        toValue: 1,
        duration: 600,
        useNativeDriver: true,
      }).start();
    }
  }, [stats]);

  const loadDashboard = async () => {
    try {
      setLoading(true);
      const dashboardStats = await getDashboardStats();
      const fullHistory = await getFullHistory(50);
      const dashboardInsights = await generateInsights();
      
      setStats(dashboardStats);
      setHistory(fullHistory);
      setInsights(dashboardInsights);
      
      // Analytics
      trackEvents.dashboardViewed();
    } catch (error) {
      console.error('Load dashboard error:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteAnalysis = (id, type) => {
    Alert.alert(
      'Supprimer',
      'Voulez-vous vraiment supprimer cette analyse ?',
      [
        { text: 'Annuler', style: 'cancel' },
        {
          text: 'Supprimer',
          style: 'destructive',
          onPress: async () => {
            const success = await deleteAnalysis(id, type);
            if (success) {
              setHistory(history.filter(item => item.id !== id));
              loadDashboard(); // Recharger les stats
            }
          },
        },
      ]
    );
  };

  const filteredHistory = filter === 'all'
    ? history
    : history.filter(item => item.type === filter);

  if (loading) {
    return (
      <View style={styles.wrapper}>
        <LinearGradient colors={THEME.colors.gradientDark} style={styles.container}>
          <SafeAreaView style={styles.safeArea}>
            <View style={styles.header}>
              <TouchableOpacity style={styles.backButton} onPress={() => router.back()}>
                <Ionicons name="arrow-back" size={24} color="#fff" />
                <Text style={styles.backButtonText}>Retour</Text>
              </TouchableOpacity>
            </View>
            <ScrollView contentContainerStyle={styles.scrollContent}>
              <View style={styles.titleSection}>
                <Text style={styles.mainTitle}>📊 Mon Dashboard</Text>
                <Text style={styles.subtitle}>Chargement de vos statistiques...</Text>
              </View>
              <SkeletonCard />
              <SkeletonCard />
              <SkeletonCard />
            </ScrollView>
          </SafeAreaView>
        </LinearGradient>
      </View>
    );
  }

  return (
    <View style={styles.wrapper}>
      <LinearGradient colors={THEME.colors.gradientDark} style={styles.container}>
        <SafeAreaView style={styles.safeArea}>
          <Stack.Screen
            options={{
              title: 'Mon Dashboard',
              headerStyle: { backgroundColor: '#0F172A' },
              headerTintColor: '#fff',
              headerShadowVisible: false,
            }}
          />

          {/* Header */}
          <View style={styles.header}>
            <TouchableOpacity style={styles.backButton} onPress={() => router.back()}>
              <Ionicons name="arrow-back" size={24} color="#fff" />
              <Text style={styles.backButtonText}>Retour</Text>
            </TouchableOpacity>
          </View>

          <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
            <Animated.View style={{ opacity: fadeAnim }}>
              {/* Titre */}
              <View style={styles.titleSection}>
                <Text style={styles.mainTitle}>📊 Mon Dashboard</Text>
                <Text style={styles.subtitle}>Vue d'ensemble de votre activité astrologique</Text>
              </View>

              {/* Stats Cards */}
              <View style={styles.statsGrid}>
                <View style={styles.statCard}>
                  <Text style={styles.statIcon}>📊</Text>
                  <Text style={styles.statValue}>{stats?.totalAnalyses || 0}</Text>
                  <Text style={styles.statLabel}>Analyses totales</Text>
                </View>

                <View style={styles.statCard}>
                  <Text style={styles.statIcon}>👶</Text>
                  <Text style={styles.statValue}>{stats?.parentChildAnalyses || 0}</Text>
                  <Text style={styles.statLabel}>Parent-Enfant</Text>
                </View>

                <View style={styles.statCard}>
                  <Text style={styles.statIcon}>💕</Text>
                  <Text style={styles.statValue}>{stats?.compatibilityAnalyses || 0}</Text>
                  <Text style={styles.statLabel}>Relations</Text>
                </View>

                <View style={styles.statCard}>
                  <Text style={styles.statIcon}>📅</Text>
                  <Text style={styles.statValue}>{stats?.horoscopesViewed || 0}</Text>
                  <Text style={styles.statLabel}>Horoscopes</Text>
                </View>

                <View style={styles.statCard}>
                  <Text style={styles.statIcon}>🌙</Text>
                  <Text style={styles.statValue}>{stats?.cycleAstroAnalyses || 0}</Text>
                  <Text style={styles.statLabel}>Cycle & Astro</Text>
                </View>
              </View>

              {/* Profil Card */}
              <View style={styles.profileCard}>
                <View style={styles.profileHeader}>
                  <Text style={styles.profileIcon}>✨</Text>
                  <Text style={styles.profileTitle}>Mon Profil Astral</Text>
                </View>
                {profile?.birthDate ? (
                  <>
                    <Text style={styles.profileName}>{profile.name || 'Utilisateur'}</Text>
                    <Text style={styles.profileSign}>
                      {useProfileStore.getState().getSunSign()?.emoji} {useProfileStore.getState().getSunSign()?.name || useProfileStore.getState().getZodiacSign()?.sign}
                    </Text>
                    {profile.birthPlace && (
                      <Text style={styles.profilePlace}>📍 {profile.birthPlace}</Text>
                    )}
                  </>
                ) : (
                  <TouchableOpacity
                    style={styles.completeProfileButton}
                    onPress={() => router.push('/(tabs)/profile')}
                  >
                    <Text style={styles.completeProfileText}>Compléter mon profil</Text>
                  </TouchableOpacity>
                )}
              </View>

              {/* Badges */}
              {stats?.badges && stats.badges.length > 0 && (
                <View style={styles.badgesSection}>
                  <Text style={styles.sectionTitle}>🏆 Mes Badges</Text>
                  <View style={styles.badgesGrid}>
                    {stats.badges.map((badge) => (
                      <View key={badge.id} style={styles.badgeCard}>
                        <Text style={styles.badgeEmoji}>{badge.emoji}</Text>
                        <Text style={styles.badgeName}>{badge.name}</Text>
                        <Text style={styles.badgeDescription}>{badge.description}</Text>
                      </View>
                    ))}
                  </View>
                </View>
              )}

              {/* Streak */}
              {stats?.streak > 0 && (
                <View style={styles.streakCard}>
                  <Text style={styles.streakIcon}>🔥</Text>
                  <View style={styles.streakContent}>
                    <Text style={styles.streakValue}>{stats.streak} jours</Text>
                    <Text style={styles.streakLabel}>Série en cours !</Text>
                  </View>
                </View>
              )}

              {/* Insights IA */}
              {insights && insights.length > 0 && (
                <View style={styles.insightsSection}>
                  <Text style={styles.sectionTitle}>💡 Tes Insights</Text>
                  <View style={styles.insightsGrid}>
                    {insights.map((insight, index) => (
                      <View key={index} style={styles.insightCard}>
                        <Text style={styles.insightEmoji}>{insight.emoji}</Text>
                        <Text style={styles.insightText}>{insight.text}</Text>
                      </View>
                    ))}
                  </View>
                </View>
              )}

              {/* Graphiques */}
              <View style={styles.chartsSection}>
                <Text style={styles.sectionTitle}>📊 Tes Graphiques</Text>
                <MoodCycleChart />
                <EnergyCycleChart />
              </View>

              {/* Historique */}
              <View style={styles.historySection}>
                <Text style={styles.sectionTitle}>📚 Historique des Analyses</Text>

                {/* Filtres */}
                <ScrollView horizontal showsHorizontalScrollIndicator={false} style={styles.filters}>
                  {[
                    { id: 'all', label: 'Toutes', icon: '📊' },
                    { id: 'parent-child', label: 'Parent-Enfant', icon: '👶' },
                    { id: 'cycle-astro', label: 'Cycle & Astro', icon: '🌙' },
                    { id: 'couple', label: 'Couple', icon: '💑' },
                    { id: 'friends', label: 'Amis', icon: '🤝' },
                    { id: 'colleagues', label: 'Collègues', icon: '💼' },
                  ].map((filterOption) => (
                    <TouchableOpacity
                      key={filterOption.id}
                      style={[
                        styles.filterButton,
                        filter === filterOption.id && styles.filterButtonActive,
                      ]}
                      onPress={() => setFilter(filterOption.id)}
                    >
                      <Text style={styles.filterIcon}>{filterOption.icon}</Text>
                      <Text style={[
                        styles.filterText,
                        filter === filterOption.id && styles.filterTextActive,
                      ]}>
                        {filterOption.label}
                      </Text>
                    </TouchableOpacity>
                  ))}
                </ScrollView>

                {/* Liste */}
                {filteredHistory.length === 0 ? (
                  <EmptyState
                    icon="analytics-outline"
                    title="Aucune analyse"
                    message="Créez votre première analyse pour commencer votre voyage astrologique"
                    actionLabel="Créer une analyse"
                    onAction={() => router.push('/choose-analysis')}
                  />
                ) : (
                  <View style={styles.historyList}>
                    {filteredHistory.map((item, index) => (
                      <TouchableOpacity
                        key={item.id || index}
                        style={styles.historyCard}
                        onPress={() => setSelectedAnalysis(item)}
                        activeOpacity={0.7}
                      >
                        <View style={styles.historyHeader}>
                          <View style={styles.historyLeft}>
                            <Text style={styles.historyIcon}>{item.icon}</Text>
                            <View style={styles.historyInfo}>
                              <Text style={styles.historyType}>
                                {item.type === 'parent-child' ? 'Parent-Enfant' : 
                                 item.type === 'cycle-astro' ? 'Cycle & Astrologie' :
                                 item.type === 'couple' ? 'Couple' :
                                 item.type === 'friends' ? 'Amis' : 'Collègues'}
                              </Text>
                              <Text style={styles.historyDate}>
                                {new Date(item.created_at).toLocaleDateString('fr-FR', {
                                  day: 'numeric',
                                  month: 'short',
                                  hour: '2-digit',
                                  minute: '2-digit',
                                })}
                              </Text>
                            </View>
                          </View>
                          <View style={styles.historyRight}>
                            <Text style={styles.historyScore}>
                              {item.type === 'cycle-astro' ? `${item.score}` : `${item.score}%`}
                            </Text>
                            <TouchableOpacity
                              onPress={(e) => {
                                e.stopPropagation();
                                handleDeleteAnalysis(item.id, item.type);
                              }}
                              style={styles.deleteButton}
                            >
                              <Ionicons name="trash-outline" size={18} color="rgba(255,255,255,0.5)" />
                            </TouchableOpacity>
                          </View>
                        </View>
                        <View style={styles.viewDetailsHint}>
                          <Ionicons name="eye-outline" size={14} color="rgba(255,255,255,0.5)" />
                          <Text style={styles.viewDetailsText}>Voir les détails</Text>
                        </View>
                      </TouchableOpacity>
                    ))}
                  </View>
                )}
              </View>
            </Animated.View>
          </ScrollView>

          {/* Modal Détails */}
          <Modal
            visible={selectedAnalysis !== null}
            animationType="slide"
            presentationStyle="pageSheet"
            onRequestClose={() => setSelectedAnalysis(null)}
          >
            <View style={styles.modalWrapper}>
              <LinearGradient colors={THEME.colors.gradientDark} style={styles.modalContainer}>
                <SafeAreaView style={styles.modalSafeArea}>
                  {/* Header Modal */}
                  <View style={styles.modalHeader}>
                    <Text style={styles.modalTitle}>Détails de l'analyse</Text>
                    <TouchableOpacity
                      style={styles.modalClose}
                      onPress={() => setSelectedAnalysis(null)}
                    >
                      <Ionicons name="close" size={28} color="#fff" />
                    </TouchableOpacity>
                  </View>

                  {selectedAnalysis && (
                    <ScrollView contentContainerStyle={styles.modalContent}>
                      {/* Score */}
                      <View style={styles.modalScoreCard}>
                        <Text style={styles.modalIcon}>{selectedAnalysis.icon}</Text>
                        <Text style={styles.modalScore}>{selectedAnalysis.score}%</Text>
                        <Text style={styles.modalType}>
                          {selectedAnalysis.type === 'parent-child' ? 'Compatibilité Parent-Enfant' :
                           selectedAnalysis.type === 'cycle-astro' ? 'Analyse Cycle & Astrologie' :
                           selectedAnalysis.type === 'couple' ? 'Compatibilité Amoureuse' :
                           selectedAnalysis.type === 'friends' ? 'Compatibilité Amicale' : 'Compatibilité Professionnelle'}
                        </Text>
                        <Text style={styles.modalDate}>
                          {new Date(selectedAnalysis.created_at).toLocaleDateString('fr-FR', {
                            weekday: 'long',
                            day: 'numeric',
                            month: 'long',
                            year: 'numeric',
                            hour: '2-digit',
                            minute: '2-digit',
                          })}
                        </Text>
                      </View>

                      {/* Interprétation */}
                      {selectedAnalysis.interpretation && (
                        <View style={styles.modalSection}>
                          <Text style={styles.modalSectionTitle}>
                            {selectedAnalysis.interpretation.emoji} {selectedAnalysis.interpretation.title}
                          </Text>
                          <Text style={styles.modalSectionText}>
                            {selectedAnalysis.interpretation.description}
                          </Text>
                        </View>
                      )}

                      {/* Scores détaillés */}
                      {selectedAnalysis.detailedScores && (
                        <View style={styles.modalSection}>
                          <Text style={styles.modalSectionTitle}>📊 Scores détaillés</Text>
                          <View style={styles.detailsGrid}>
                            <View style={styles.detailItem}>
                              <Text style={styles.detailLabel}>💬 Communication</Text>
                              <Text style={styles.detailValue}>{selectedAnalysis.detailedScores.communication}%</Text>
                            </View>
                            <View style={styles.detailItem}>
                              <Text style={styles.detailLabel}>🔥 Passion</Text>
                              <Text style={styles.detailValue}>{selectedAnalysis.detailedScores.passion}%</Text>
                            </View>
                            <View style={styles.detailItem}>
                              <Text style={styles.detailLabel}>🤝 Complicité</Text>
                              <Text style={styles.detailValue}>{selectedAnalysis.detailedScores.complicity}%</Text>
                            </View>
                            <View style={styles.detailItem}>
                              <Text style={styles.detailLabel}>🎯 Objectifs</Text>
                              <Text style={styles.detailValue}>{selectedAnalysis.detailedScores.goals}%</Text>
                            </View>
                          </View>
                        </View>
                      )}

                      {/* Recommandations */}
                      {selectedAnalysis.recommendations && selectedAnalysis.recommendations.length > 0 && (
                        <View style={styles.modalSection}>
                          <Text style={styles.modalSectionTitle}>💡 Conseils</Text>
                          {selectedAnalysis.recommendations.map((rec, i) => (
                            <Text key={i} style={styles.modalRecommendation}>
                              {rec.icon} {rec.text}
                            </Text>
                          ))}
                        </View>
                      )}

                      {/* Bouton Fermer */}
                      <TouchableOpacity
                        style={styles.modalCloseButton}
                        onPress={() => setSelectedAnalysis(null)}
                      >
                        <Text style={styles.modalCloseButtonText}>Fermer</Text>
                      </TouchableOpacity>
                    </ScrollView>
                  )}
                </SafeAreaView>
              </LinearGradient>
            </View>
          </Modal>
        </SafeAreaView>
      </LinearGradient>
    </View>
  );
}

const styles = StyleSheet.create({
  wrapper: {
    flex: 1,
    backgroundColor: '#0F172A',
  },
  safeArea: {
    flex: 1,
  },
  container: {
    flex: 1,
  },
  header: {
    paddingHorizontal: 20,
    paddingTop: 10,
    paddingBottom: 10,
  },
  backButton: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    paddingVertical: 10,
    paddingHorizontal: 12,
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 12,
    alignSelf: 'flex-start',
  },
  backButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    gap: 15,
  },
  loadingText: {
    fontSize: 16,
    color: 'rgba(255,255,255,0.8)',
  },
  scrollContent: {
    padding: 20,
    paddingTop: 5,
    paddingBottom: 40,
  },
  titleSection: {
    marginBottom: 25,
  },
  mainTitle: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 5,
  },
  subtitle: {
    fontSize: 14,
    color: 'rgba(255,255,255,0.7)',
  },
  statsGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 12,
    marginBottom: 20,
  },
  statCard: {
    flex: 1,
    minWidth: '47%',
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 16,
    padding: 20,
    alignItems: 'center',
  },
  statIcon: {
    fontSize: 32,
    marginBottom: 10,
  },
  statValue: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 5,
  },
  statLabel: {
    fontSize: 12,
    color: 'rgba(255,255,255,0.7)',
    textAlign: 'center',
  },
  profileCard: {
    backgroundColor: 'rgba(139, 92, 246, 0.2)',
    borderRadius: 16,
    padding: 20,
    marginBottom: 20,
  },
  profileHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
    marginBottom: 15,
  },
  profileIcon: {
    fontSize: 24,
  },
  profileTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#fff',
  },
  profileName: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 5,
  },
  profileSign: {
    fontSize: 16,
    color: 'rgba(255,255,255,0.9)',
    marginBottom: 5,
  },
  profilePlace: {
    fontSize: 14,
    color: 'rgba(255,255,255,0.7)',
  },
  completeProfileButton: {
    backgroundColor: 'rgba(255, 255, 255, 0.15)',
    paddingVertical: 12,
    borderRadius: 10,
    alignItems: 'center',
  },
  completeProfileText: {
    color: '#fff',
    fontSize: 15,
    fontWeight: '600',
  },
  badgesSection: {
    marginBottom: 20,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 15,
  },
  badgesGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 12,
  },
  badgeCard: {
    flex: 1,
    minWidth: '47%',
    backgroundColor: 'rgba(245, 158, 11, 0.15)',
    borderRadius: 12,
    padding: 16,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: 'rgba(245, 158, 11, 0.3)',
  },
  badgeEmoji: {
    fontSize: 40,
    marginBottom: 8,
  },
  badgeName: {
    fontSize: 14,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 4,
  },
  badgeDescription: {
    fontSize: 11,
    color: 'rgba(255,255,255,0.7)',
    textAlign: 'center',
  },
  streakCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(239, 68, 68, 0.15)',
    borderRadius: 16,
    padding: 20,
    marginBottom: 20,
    gap: 15,
  },
  streakIcon: {
    fontSize: 40,
  },
  streakContent: {
    flex: 1,
  },
  streakValue: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 2,
  },
  streakLabel: {
    fontSize: 14,
    color: 'rgba(255,255,255,0.8)',
  },
  insightsSection: {
    marginBottom: 20,
  },
  insightsGrid: {
    gap: 12,
  },
  insightCard: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    backgroundColor: 'rgba(255, 182, 193, 0.12)',
    borderRadius: 12,
    padding: 16,
    borderWidth: 1,
    borderColor: 'rgba(255, 182, 193, 0.25)',
  },
  insightEmoji: {
    fontSize: 28,
  },
  insightText: {
    flex: 1,
    fontSize: 14,
    color: 'rgba(255,255,255,0.9)',
    fontWeight: '500',
    lineHeight: 20,
  },
  chartsSection: {
    marginBottom: 20,
  },
  historySection: {
    marginBottom: 20,
  },
  filters: {
    marginBottom: 15,
  },
  filterButton: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingVertical: 10,
    paddingHorizontal: 16,
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 12,
    marginRight: 10,
    borderWidth: 2,
    borderColor: 'transparent',
  },
  filterButtonActive: {
    backgroundColor: 'rgba(139, 92, 246, 0.3)',
    borderColor: 'rgba(139, 92, 246, 0.6)',
  },
  filterIcon: {
    fontSize: 16,
  },
  filterText: {
    fontSize: 14,
    color: 'rgba(255,255,255,0.7)',
    fontWeight: '500',
  },
  filterTextActive: {
    color: '#fff',
    fontWeight: 'bold',
  },
  emptyState: {
    alignItems: 'center',
    paddingVertical: 40,
  },
  emptyIcon: {
    fontSize: 60,
    marginBottom: 15,
  },
  emptyText: {
    fontSize: 16,
    color: 'rgba(255,255,255,0.6)',
  },
  historyList: {
    gap: 12,
  },
  historyCard: {
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 14,
    padding: 16,
  },
  historyHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  historyLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    flex: 1,
  },
  historyInfo: {
    flex: 1,
  },
  historyIcon: {
    fontSize: 28,
  },
  historyType: {
    fontSize: 15,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 3,
  },
  historyDate: {
    fontSize: 12,
    color: 'rgba(255,255,255,0.6)',
  },
  historyRight: {
    alignItems: 'flex-end',
    gap: 8,
  },
  historyScore: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#F59E0B',
  },
  deleteButton: {
    padding: 4,
  },
  viewDetailsHint: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    marginTop: 10,
    paddingTop: 10,
    borderTopWidth: 1,
    borderTopColor: 'rgba(255,255,255,0.1)',
  },
  viewDetailsText: {
    fontSize: 13,
    color: 'rgba(255,255,255,0.5)',
    fontStyle: 'italic',
  },
  // Modal
  modalWrapper: {
    flex: 1,
    backgroundColor: '#0F172A',
  },
  modalContainer: {
    flex: 1,
  },
  modalSafeArea: {
    flex: 1,
  },
  modalHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    padding: 20,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255,255,255,0.1)',
  },
  modalTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff',
  },
  modalClose: {
    width: 44,
    height: 44,
    alignItems: 'center',
    justifyContent: 'center',
  },
  modalContent: {
    padding: 20,
    paddingBottom: 40,
  },
  modalScoreCard: {
    alignItems: 'center',
    backgroundColor: 'rgba(255,255,255,0.1)',
    borderRadius: 20,
    padding: 30,
    marginBottom: 20,
  },
  modalIcon: {
    fontSize: 60,
    marginBottom: 10,
  },
  modalScore: {
    fontSize: 64,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 10,
  },
  modalType: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 8,
  },
  modalDate: {
    fontSize: 14,
    color: 'rgba(255,255,255,0.6)',
  },
  modalSection: {
    backgroundColor: 'rgba(255,255,255,0.05)',
    borderRadius: 16,
    padding: 20,
    marginBottom: 16,
  },
  modalSectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 12,
  },
  modalSectionText: {
    fontSize: 14,
    color: 'rgba(255,255,255,0.9)',
    lineHeight: 22,
  },
  detailsGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 12,
  },
  detailItem: {
    flex: 1,
    minWidth: '47%',
    backgroundColor: 'rgba(255,255,255,0.08)',
    borderRadius: 12,
    padding: 14,
  },
  detailLabel: {
    fontSize: 13,
    color: 'rgba(255,255,255,0.7)',
    marginBottom: 6,
  },
  detailValue: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#F59E0B',
  },
  modalRecommendation: {
    fontSize: 14,
    color: '#fff',
    lineHeight: 22,
    marginBottom: 10,
  },
  modalCloseButton: {
    backgroundColor: 'rgba(255,255,255,0.15)',
    paddingVertical: 16,
    borderRadius: 12,
    alignItems: 'center',
    marginTop: 10,
  },
  modalCloseButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
});

