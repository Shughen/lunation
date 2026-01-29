/**
 * Tab Navigator Layout
 * 5 onglets: Accueil, Calendrier, Horoscope, Rituels, Profil
 */

import React from 'react';
import { Tabs } from 'expo-router';
import { View, StyleSheet, Platform } from 'react-native';
import Svg, { Path, Circle, G, Rect } from 'react-native-svg';
import { colors } from '../../constants/theme';

// Tab bar configuration
const TAB_BAR_HEIGHT = 70;
const ICON_SIZE = 24;

// Icon components for each tab
function HomeIcon({ color, focused }: { color: string; focused: boolean }) {
  return (
    <Svg width={ICON_SIZE} height={ICON_SIZE} viewBox="0 0 24 24" fill="none">
      <Path
        d="M12 3L4 9v12h5v-7h6v7h5V9l-8-6z"
        stroke={color}
        strokeWidth={focused ? 2 : 1.5}
        strokeLinecap="round"
        strokeLinejoin="round"
        fill={focused ? `${color}20` : 'none'}
      />
      {/* Moon crescent */}
      <Path
        d="M14 7c0 1.1-.9 2-2 2s-2-.9-2-2 .9-2 2-2"
        stroke={color}
        strokeWidth={1.5}
        strokeLinecap="round"
      />
    </Svg>
  );
}

function CalendarIcon({ color, focused }: { color: string; focused: boolean }) {
  return (
    <Svg width={ICON_SIZE} height={ICON_SIZE} viewBox="0 0 24 24" fill="none">
      <Rect
        x="3"
        y="4"
        width="18"
        height="18"
        rx="2"
        stroke={color}
        strokeWidth={focused ? 2 : 1.5}
        fill={focused ? `${color}20` : 'none'}
      />
      <Path d="M3 10h18" stroke={color} strokeWidth={1.5} />
      <Path d="M8 2v4M16 2v4" stroke={color} strokeWidth={1.5} strokeLinecap="round" />
      {/* Moon phase dot */}
      <Circle cx="12" cy="15" r="2" fill={color} opacity={focused ? 1 : 0.6} />
    </Svg>
  );
}

function HoroscopeIcon({ color, focused }: { color: string; focused: boolean }) {
  return (
    <Svg width={ICON_SIZE + 4} height={ICON_SIZE + 4} viewBox="0 0 24 24" fill="none">
      {/* Eye shape */}
      <Path
        d="M12 5C7 5 3 9 2 12c1 3 5 7 10 7s9-4 10-7c-1-3-5-7-10-7z"
        stroke={color}
        strokeWidth={focused ? 2 : 1.5}
        strokeLinecap="round"
        strokeLinejoin="round"
        fill={focused ? `${color}20` : 'none'}
      />
      {/* Inner circle / iris */}
      <Circle
        cx="12"
        cy="12"
        r="3"
        stroke={color}
        strokeWidth={1.5}
        fill={focused ? color : 'none'}
      />
    </Svg>
  );
}

function RitualsIcon({ color, focused }: { color: string; focused: boolean }) {
  return (
    <Svg width={ICON_SIZE} height={ICON_SIZE} viewBox="0 0 24 24" fill="none">
      {/* Lightbulb shape */}
      <Path
        d="M12 2C8.5 2 6 4.5 6 8c0 2.5 1.5 4.5 3 5.5V16h6v-2.5c1.5-1 3-3 3-5.5 0-3.5-2.5-6-6-6z"
        stroke={color}
        strokeWidth={focused ? 2 : 1.5}
        strokeLinecap="round"
        strokeLinejoin="round"
        fill={focused ? `${color}20` : 'none'}
      />
      {/* Lightbulb base */}
      <Path d="M9 19h6M9 22h6" stroke={color} strokeWidth={1.5} strokeLinecap="round" />
      {/* Inner glow */}
      {focused && <Circle cx="12" cy="8" r="2" fill={color} opacity={0.5} />}
    </Svg>
  );
}

function ProfileIcon({ color, focused }: { color: string; focused: boolean }) {
  return (
    <Svg width={ICON_SIZE} height={ICON_SIZE} viewBox="0 0 24 24" fill="none">
      {/* Head */}
      <Circle
        cx="12"
        cy="8"
        r="4"
        stroke={color}
        strokeWidth={focused ? 2 : 1.5}
        fill={focused ? `${color}20` : 'none'}
      />
      {/* Body */}
      <Path
        d="M4 20c0-4 4-6 8-6s8 2 8 6"
        stroke={color}
        strokeWidth={focused ? 2 : 1.5}
        strokeLinecap="round"
        fill={focused ? `${color}20` : 'none'}
      />
    </Svg>
  );
}

export default function TabLayout() {
  return (
    <Tabs
      screenOptions={{
        headerShown: false,
        tabBarActiveTintColor: colors.gold,
        tabBarInactiveTintColor: colors.textMuted,
        tabBarStyle: styles.tabBar,
        tabBarLabelStyle: styles.tabBarLabel,
        tabBarItemStyle: styles.tabBarItem,
      }}
    >
      <Tabs.Screen
        name="home"
        options={{
          title: 'Accueil',
          tabBarIcon: ({ color, focused }) => <HomeIcon color={color} focused={focused} />,
        }}
      />
      <Tabs.Screen
        name="calendar"
        options={{
          title: 'Calendrier',
          tabBarIcon: ({ color, focused }) => <CalendarIcon color={color} focused={focused} />,
        }}
      />
      <Tabs.Screen
        name="horoscope"
        options={{
          title: 'Horoscope',
          tabBarIcon: ({ color, focused }) => <HoroscopeIcon color={color} focused={focused} />,
        }}
      />
      <Tabs.Screen
        name="rituals"
        options={{
          title: 'Rituels',
          tabBarIcon: ({ color, focused }) => <RitualsIcon color={color} focused={focused} />,
        }}
      />
      <Tabs.Screen
        name="profile"
        options={{
          title: 'Profil',
          tabBarIcon: ({ color, focused }) => <ProfileIcon color={color} focused={focused} />,
        }}
      />
    </Tabs>
  );
}

const styles = StyleSheet.create({
  tabBar: {
    backgroundColor: '#1a0b2e',
    borderTopColor: 'rgba(183, 148, 246, 0.15)',
    borderTopWidth: 1,
    height: TAB_BAR_HEIGHT + (Platform.OS === 'ios' ? 20 : 0),
    paddingTop: 8,
    paddingBottom: Platform.OS === 'ios' ? 24 : 8,
  },
  tabBarLabel: {
    fontSize: 10,
    fontWeight: '500',
    marginTop: 4,
  },
  tabBarItem: {
    paddingVertical: 4,
  },
});
