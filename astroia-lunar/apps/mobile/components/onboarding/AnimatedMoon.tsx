/**
 * AnimatedMoon Component
 * Animation de lune pour le Welcome screen
 *
 * La lune se remplit progressivement (nouvelle → pleine)
 * avec un effet de glow et des étoiles animées en arrière-plan
 */

import React, { useEffect, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  Animated,
  Easing,
  Dimensions,
} from 'react-native';
import { colors } from '../../constants/theme';

const { width: SCREEN_WIDTH } = Dimensions.get('window');

// Phases de la lune pour l'animation (nouvelle → pleine)
const MOON_PHASES = ['🌑', '🌒', '🌓', '🌔', '🌕'];

interface AnimatedMoonProps {
  size?: number;
  animationDuration?: number;
  showStars?: boolean;
}

interface StarProps {
  delay: number;
  x: number;
  y: number;
  size: number;
}

/**
 * Étoile animée individuelle
 */
function AnimatedStar({ delay, x, y, size }: StarProps) {
  const opacityAnim = useRef(new Animated.Value(0)).current;
  const scaleAnim = useRef(new Animated.Value(0.5)).current;

  useEffect(() => {
    const animation = Animated.loop(
      Animated.sequence([
        Animated.delay(delay),
        Animated.parallel([
          Animated.timing(opacityAnim, {
            toValue: 1,
            duration: 1000,
            easing: Easing.inOut(Easing.ease),
            useNativeDriver: true,
          }),
          Animated.timing(scaleAnim, {
            toValue: 1,
            duration: 1000,
            easing: Easing.inOut(Easing.ease),
            useNativeDriver: true,
          }),
        ]),
        Animated.parallel([
          Animated.timing(opacityAnim, {
            toValue: 0.3,
            duration: 1500,
            easing: Easing.inOut(Easing.ease),
            useNativeDriver: true,
          }),
          Animated.timing(scaleAnim, {
            toValue: 0.7,
            duration: 1500,
            easing: Easing.inOut(Easing.ease),
            useNativeDriver: true,
          }),
        ]),
      ])
    );
    animation.start();
    return () => animation.stop();
  }, [delay, opacityAnim, scaleAnim]);

  return (
    <Animated.Text
      style={[
        styles.star,
        {
          left: x,
          top: y,
          fontSize: size,
          opacity: opacityAnim,
          transform: [{ scale: scaleAnim }],
        },
      ]}
    >
      ✦
    </Animated.Text>
  );
}

/**
 * Génère des positions aléatoires pour les étoiles
 */
function generateStarPositions(count: number): StarProps[] {
  const stars: StarProps[] = [];
  for (let i = 0; i < count; i++) {
    stars.push({
      delay: Math.random() * 2000,
      x: Math.random() * (SCREEN_WIDTH - 40),
      y: Math.random() * 300 - 50,
      size: Math.random() * 8 + 6,
    });
  }
  return stars;
}

export function AnimatedMoon({
  size = 100,
  animationDuration = 2000,
  showStars = true,
}: AnimatedMoonProps) {
  const [phaseIndex, setPhaseIndex] = React.useState(0);
  const scaleAnim = useRef(new Animated.Value(0.8)).current;
  const opacityAnim = useRef(new Animated.Value(0)).current;
  const glowAnim = useRef(new Animated.Value(0)).current;
  const starsRef = useRef(generateStarPositions(15));

  useEffect(() => {
    // Animation d'entrée
    Animated.parallel([
      Animated.timing(scaleAnim, {
        toValue: 1,
        duration: 600,
        easing: Easing.out(Easing.back(1.5)),
        useNativeDriver: true,
      }),
      Animated.timing(opacityAnim, {
        toValue: 1,
        duration: 400,
        useNativeDriver: true,
      }),
    ]).start();

    // Animation des phases de la lune
    const phaseInterval = animationDuration / MOON_PHASES.length;
    let currentPhase = 0;

    const phaseTimer = setInterval(() => {
      currentPhase++;
      if (currentPhase < MOON_PHASES.length) {
        setPhaseIndex(currentPhase);
      } else {
        clearInterval(phaseTimer);
        // Lancer l'animation de glow une fois pleine
        startGlowAnimation();
      }
    }, phaseInterval);

    return () => clearInterval(phaseTimer);
  }, [animationDuration, scaleAnim, opacityAnim]);

  const startGlowAnimation = () => {
    Animated.loop(
      Animated.sequence([
        Animated.timing(glowAnim, {
          toValue: 1,
          duration: 1500,
          easing: Easing.inOut(Easing.ease),
          useNativeDriver: true,
        }),
        Animated.timing(glowAnim, {
          toValue: 0,
          duration: 1500,
          easing: Easing.inOut(Easing.ease),
          useNativeDriver: true,
        }),
      ])
    ).start();
  };

  const glowScale = glowAnim.interpolate({
    inputRange: [0, 1],
    outputRange: [1, 1.1],
  });

  return (
    <View style={styles.container}>
      {/* Étoiles animées */}
      {showStars && (
        <View style={styles.starsContainer}>
          {starsRef.current.map((star, index) => (
            <AnimatedStar key={index} {...star} />
          ))}
        </View>
      )}

      {/* Lune principale */}
      <Animated.View
        style={[
          styles.moonContainer,
          {
            width: size + 40,
            height: size + 40,
            opacity: opacityAnim,
            transform: [{ scale: scaleAnim }, { scale: glowScale }],
          },
        ]}
      >
        {/* Glow effect */}
        <View
          style={[
            styles.glow,
            {
              width: size + 60,
              height: size + 60,
              borderRadius: (size + 60) / 2,
            },
          ]}
        />

        {/* Lune emoji */}
        <Text style={[styles.moon, { fontSize: size }]}>
          {MOON_PHASES[phaseIndex]}
        </Text>
      </Animated.View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'center',
    position: 'relative',
  },
  starsContainer: {
    position: 'absolute',
    width: SCREEN_WIDTH,
    height: 300,
    top: -100,
  },
  star: {
    position: 'absolute',
    color: colors.accent,
  },
  moonContainer: {
    alignItems: 'center',
    justifyContent: 'center',
    position: 'relative',
  },
  glow: {
    position: 'absolute',
    backgroundColor: 'rgba(183, 148, 246, 0.15)',
    shadowColor: colors.accent,
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0.5,
    shadowRadius: 30,
    elevation: 10,
  },
  moon: {
    textAlign: 'center',
    textShadowColor: 'rgba(183, 148, 246, 0.8)',
    textShadowOffset: { width: 0, height: 0 },
    textShadowRadius: 20,
  },
});

export default AnimatedMoon;
