import React from 'react';
import { View, Text, Pressable } from 'react-native';

export default React.memo(function AstroCard({ moonSign, energyText, onPress }) {
  return (
    <Pressable 
      onPress={onPress}
      accessible={true}
      accessibilityRole="button"
      accessibilityLabel={`Astro du jour. ${moonSign}. ${energyText}. Toucher pour voir l'analyse complète.`}
      accessibilityHint="Toucher deux fois pour ouvrir l'analyse astrologique"
      style={{
        marginHorizontal: 16, marginTop: 12, marginBottom: 12, borderRadius: 18, padding: 16,
        backgroundColor: 'rgba(255,255,255,0.05)', borderWidth: 1, borderColor: 'rgba(255,255,255,0.08)'
      }}
    >
      <Text style={{ color: '#FFD37A', fontSize: 16, fontWeight: '700' }}>
        Astro du jour
      </Text>
      <Text style={{ color: 'white', fontSize: 18, fontWeight: '800', marginTop: 4 }}>
        {moonSign}
      </Text>
      <Text style={{ color: '#CFCFEA', marginTop: 6 }}>{energyText}</Text>
      <Text style={{ 
        color: '#B6B6D8', 
        marginTop: 10,
        minHeight: 36, // Alignement vertical avec bouton MoodCard
      }}>→ Voir analyse</Text>
    </Pressable>
  );
});

