import React from 'react';
import { View, Text, Pressable } from 'react-native';

export default React.memo(function CycleCard({ phase, dayLabel, energy, fertile, onPress }) {
  const isConfigured = phase !== 'Configure ton cycle';
  
  return (
    <Pressable
      onPress={onPress}
      accessible={true}
      accessibilityRole="button"
      accessibilityLabel={isConfigured 
        ? `Mon cycle aujourd'hui : ${dayLabel}. Énergie ${energy}. ${fertile ? 'Phase fertile.' : ''} Toucher pour voir les détails.`
        : "Configurer mon cycle menstruel pour commencer le suivi"
      }
      accessibilityHint="Toucher deux fois pour ouvrir"
      style={{
        marginHorizontal: 16, 
        marginBottom: 12, // +4px supplémentaire pour aérer
        borderRadius: 18, 
        padding: 16,
        backgroundColor: 'rgba(255,255,255,0.06)', 
        borderWidth: 1, 
        borderColor: 'rgba(255,255,255,0.08)'
      }}
    >
      <Text style={{ color: '#FFD37A', fontSize: 16, fontWeight: '700', marginBottom: 4 }}>
        Mon cycle aujourd'hui
      </Text>
      <Text style={{ color: 'white', fontSize: 22, fontWeight: '800' }}>
        {dayLabel} — {phase}
      </Text>
      <Text style={{ color: '#CFCFEA', marginTop: 6 }}>
        Énergie : {energy} {fertile ? '• Phase fertile' : ''}
      </Text>
      <Text style={{ color: '#B6B6D8', marginTop: 10 }}>→ Voir détails</Text>
    </Pressable>
  );
});

