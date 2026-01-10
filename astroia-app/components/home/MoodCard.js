import React from 'react';
import { View, Text, Pressable } from 'react-native';

export default React.memo(function MoodCard({ onOpenJournal }) {
  return (
    <View style={{
      marginHorizontal: 16, marginTop: 12, marginBottom: 12, borderRadius: 18, padding: 16,
      backgroundColor: 'rgba(255,255,255,0.05)', borderWidth: 1, borderColor: 'rgba(255,255,255,0.08)'
    }}>
      <Text style={{ color: '#FFD37A', fontSize: 16, fontWeight: '700' }}>
        Humeur & émotions
      </Text>
      <Text style={{ color: '#CFCFEA', marginTop: 8 }}>Comment te sens-tu ?</Text>
      <Pressable 
        onPress={onOpenJournal}
        accessible={true}
        accessibilityRole="button"
        accessibilityLabel="Ouvrir mon journal d'humeur et émotions"
        accessibilityHint="Toucher deux fois pour créer une nouvelle entrée"
        style={{
          alignSelf: 'flex-start', 
          marginTop: 10, // Aligné avec AstroCard (10 au lieu de 12)
          backgroundColor: 'rgba(255,211,122,0.15)',
          paddingHorizontal: 12, 
          paddingVertical: 8, 
          borderRadius: 12,
          minHeight: 36, // Zone tactile minimale
        }}
      >
        <Text style={{ color: '#FFD37A', fontWeight: '700' }}>Ouvrir le journal</Text>
      </Pressable>
    </View>
  );
});

