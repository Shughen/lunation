import { Tabs } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../../constants/theme';

export default function TabsLayout() {
  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: COLORS.accent,
        tabBarInactiveTintColor: COLORS.textMuted,
        tabBarStyle: {
          backgroundColor: '#0F172A',
          borderTopColor: 'rgba(139, 92, 246, 0.3)',
          borderTopWidth: 1,
          height: 90,
          paddingBottom: 25,
          paddingTop: 10,
        },
        tabBarLabelStyle: {
          fontSize: 12,
          fontWeight: '600',
        },
        headerStyle: {
          backgroundColor: '#0F172A',
          borderBottomColor: 'rgba(139, 92, 246, 0.3)',
          borderBottomWidth: 1,
        },
        headerTintColor: COLORS.text,
        headerTitleStyle: {
          fontWeight: 'bold',
          fontSize: 20,
        },
      }}
    >
      <Tabs.Screen
        name="home"
        options={{
          title: 'Accueil',
          headerTitle: '🌙 LUNA',
          tabBarIcon: ({ color, size }) => (
            <Ionicons name="home" size={size} color={color} />
          ),
          tabBarAccessibilityLabel: 'Accueil, onglet principal de LUNA',
        }}
      />
      <Tabs.Screen
        name="profile"
        options={{
          title: 'Profil',
          headerTitle: '🌙 Mon Profil Astral',
          tabBarIcon: ({ color, size }) => (
            <Ionicons name="person-circle" size={size} color={color} />
          ),
          tabBarAccessibilityLabel: 'Profil, voir et modifier mes informations astrologiques',
        }}
      />
      <Tabs.Screen
        name="lunar-month"
        options={{
          title: 'Mois lunaire',
          headerTitle: '🌙 Mois lunaire',
          tabBarIcon: ({ color, size }) => (
            <Ionicons name="moon" size={size} color={color} />
          ),
          tabBarAccessibilityLabel: 'Mois lunaire, voir ton cycle lunaire personnel',
        }}
      />
      <Tabs.Screen
        name="chat"
        options={{
          title: 'LUNA',
          headerTitle: '💬 Assistant LUNA',
          tabBarIcon: ({ color, size }) => (
            <Ionicons name="chatbubbles" size={size} color={color} />
          ),
          tabBarAccessibilityLabel: 'Assistant LUNA, discuter avec l\'intelligence artificielle',
        }}
      />
    </Tabs>
  );
}

