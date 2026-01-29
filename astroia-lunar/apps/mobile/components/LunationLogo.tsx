/**
 * LunationLogo Component
 *
 * Logo Lunation utilisant les images PNG des assets
 * Variantes : horizontal (texte), stacked (grande lune), icon (petite icône)
 */

import React from 'react';
import { View, Image, StyleSheet, ImageSourcePropType } from 'react-native';

interface LunationLogoProps {
  variant: 'horizontal' | 'stacked' | 'icon';
  size?: number;
}

export function LunationLogo({
  variant,
  size = 120,
}: LunationLogoProps) {
  // Sélection de l'image selon la variante
  let source: ImageSourcePropType;
  let imageSize: { width: number; height: number };

  if (variant === 'horizontal') {
    // Pour le header : utiliser l'icône
    source = require('../assets/lunation-icon-1024.png');
    imageSize = { width: size, height: size };
  } else if (variant === 'stacked') {
    // Pour le welcome screen : grande icône
    source = require('../assets/lunation-icon-1024.png');
    imageSize = { width: size, height: size };
  } else {
    // variant === 'icon' : petite icône
    source = require('../assets/lunation-icon-512.png');
    imageSize = { width: size, height: size };
  }

  return (
    <View style={styles.container}>
      <Image
        source={source}
        style={[
          imageSize,
          {
            resizeMode: 'contain',
          },
        ]}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'center',
  },
});
