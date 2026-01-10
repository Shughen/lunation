import React from 'react';
import { View, Text } from 'react-native';

export default React.memo(function TodayHeader({ cycleLabel, moonLabel, mantra }) {
  return (
    <View style={{ paddingHorizontal: 20, paddingTop: 8, paddingBottom: 16 }}>
      <Text style={{ color: '#C9B6FF', fontSize: 12, letterSpacing: 1.2 }}>AUJOURD'HUI</Text>
      <Text style={{ color: 'white', fontSize: 18, fontWeight: '700', marginTop: 6 }}>
        {cycleLabel} • {moonLabel}
      </Text>
      {!!mantra && (
        <Text style={{ color: '#CFCFEA', fontSize: 14, marginTop: 6 }}>{mantra}</Text>
      )}
    </View>
  );
});

