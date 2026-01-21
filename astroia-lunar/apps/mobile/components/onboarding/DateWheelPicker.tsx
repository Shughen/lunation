/**
 * DateWheelPicker - Sélecteur de date moderne avec roues scrollables
 *
 * Features:
 * - 3 roues (jour, mois, année) avec scroll fluide
 * - Effet de snap pour sélectionner les valeurs
 * - Design cohérent avec le thème de l'app
 * - Validation automatique des jours selon le mois
 * - Debounce pour éviter les re-renders excessifs
 */

import React, { useRef, useEffect, useCallback, useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  Dimensions,
  NativeSyntheticEvent,
  NativeScrollEvent,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';

const ITEM_HEIGHT = 44;
const VISIBLE_ITEMS = 5;
const PICKER_HEIGHT = ITEM_HEIGHT * VISIBLE_ITEMS;

// Noms des mois en français
const MONTHS = [
  'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
  'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre',
];

// Années disponibles (1920 - année courante)
const CURRENT_YEAR = new Date().getFullYear();

interface DateWheelPickerProps {
  value: Date;
  onChange: (date: Date) => void;
  minYear?: number;
  maxYear?: number;
}

interface WheelColumnProps {
  data: (string | number)[];
  selectedIndex: number;
  onSelect: (index: number) => void;
  width: number;
  formatItem?: (item: string | number) => string;
}

// Composant pour chaque colonne - Approche vraiment "uncontrolled"
// Aucune synchronisation avec le parent après le montage initial
// Le parent est notifié via onSelectRef (ref stable)
function WheelColumn({
  data,
  selectedIndex,
  onSelect,
  width,
  formatItem
}: WheelColumnProps) {
  const scrollViewRef = useRef<ScrollView>(null);
  const [localIndex, setLocalIndex] = useState(selectedIndex);
  const onSelectRef = useRef(onSelect);
  const hasScrolledRef = useRef(false);

  // Toujours garder la ref à jour sans déclencher de re-render
  onSelectRef.current = onSelect;

  // Scroll initial - une seule fois au montage
  useEffect(() => {
    const timer = setTimeout(() => {
      scrollViewRef.current?.scrollTo({
        y: selectedIndex * ITEM_HEIGHT,
        animated: false,
      });
    }, 30);
    return () => clearTimeout(timer);
  }, []); // Dépendances vides = montage uniquement

  // Ajuster si le nombre d'éléments diminue (ex: 31 jours -> 28 jours)
  useEffect(() => {
    const maxIndex = data.length - 1;
    if (localIndex > maxIndex) {
      setLocalIndex(maxIndex);
      scrollViewRef.current?.scrollTo({
        y: maxIndex * ITEM_HEIGHT,
        animated: true,
      });
      // Notifier le parent du changement forcé
      onSelectRef.current(maxIndex);
    }
  }, [data.length]); // Seulement quand la taille des données change

  const handleScrollEnd = useCallback(
    (event: NativeSyntheticEvent<NativeScrollEvent>) => {
      const offsetY = event.nativeEvent.contentOffset.y;
      const index = Math.round(offsetY / ITEM_HEIGHT);
      const clampedIndex = Math.max(0, Math.min(index, data.length - 1));

      // Mettre à jour l'index local
      setLocalIndex(clampedIndex);
      hasScrolledRef.current = true;

      // Notifier le parent via la ref (évite les problèmes de closure)
      onSelectRef.current(clampedIndex);
    },
    [data.length]
  );

  // Padding pour centrer les éléments
  const paddingVertical = (PICKER_HEIGHT - ITEM_HEIGHT) / 2;

  return (
    <View style={[styles.wheelColumn, { width }]}>
      <ScrollView
        ref={scrollViewRef}
        showsVerticalScrollIndicator={false}
        snapToInterval={ITEM_HEIGHT}
        decelerationRate="fast"
        bounces={false}
        onMomentumScrollEnd={handleScrollEnd}
        onScrollEndDrag={(event) => {
          // Pour les scrolls courts sans momentum
          const velocity = event.nativeEvent.velocity?.y ?? 0;
          if (Math.abs(velocity) < 0.5) {
            handleScrollEnd(event);
          }
        }}
        contentContainerStyle={{
          paddingVertical,
        }}
        nestedScrollEnabled
        scrollEventThrottle={16}
      >
        {data.map((item, index) => {
          // Utiliser localIndex pour la sélection visuelle
          const isSelected = index === localIndex;
          const displayText = formatItem ? formatItem(item) : String(item);
          return (
            <View key={`${item}-${index}`} style={styles.wheelItem}>
              <Text
                style={[
                  styles.wheelText,
                  typeof item === 'string' && styles.wheelTextMonth,
                  isSelected && styles.wheelTextSelected
                ]}
                numberOfLines={1}
              >
                {displayText}
              </Text>
            </View>
          );
        })}
      </ScrollView>
    </View>
  );
}

export function DateWheelPicker({ value, onChange, minYear = 1920, maxYear = CURRENT_YEAR }: DateWheelPickerProps) {
  // État local pour éviter les re-renders du parent pendant le scroll
  const [localDate, setLocalDate] = useState(value);
  const debounceTimerRef = useRef<NodeJS.Timeout | null>(null);

  // Synchroniser avec la prop value quand elle change de l'extérieur
  useEffect(() => {
    if (value.getTime() !== localDate.getTime()) {
      setLocalDate(value);
    }
  }, [value]);

  const years = React.useMemo(
    () => Array.from({ length: maxYear - minYear + 1 }, (_, i) => minYear + i),
    [minYear, maxYear]
  );

  // Calcul des jours disponibles pour le mois sélectionné
  const getDaysInMonth = useCallback((month: number, year: number) => {
    return new Date(year, month + 1, 0).getDate();
  }, []);

  const currentDay = localDate.getDate();
  const currentMonth = localDate.getMonth();
  const currentYear = localDate.getFullYear();

  const daysInMonth = getDaysInMonth(currentMonth, currentYear);
  const days = React.useMemo(
    () => Array.from({ length: daysInMonth }, (_, i) => i + 1),
    [daysInMonth]
  );

  // Index sélectionnés
  const dayIndex = currentDay - 1;
  const monthIndex = currentMonth;
  const yearIndex = years.indexOf(currentYear);

  // Fonction pour mettre à jour la date avec debounce vers le parent
  const updateDate = useCallback((newDate: Date) => {
    setLocalDate(newDate);

    // Debounce l'appel au parent pour éviter les re-renders excessifs
    if (debounceTimerRef.current) {
      clearTimeout(debounceTimerRef.current);
    }
    debounceTimerRef.current = setTimeout(() => {
      onChange(newDate);
    }, 150);
  }, [onChange]);

  // Cleanup du timer
  useEffect(() => {
    return () => {
      if (debounceTimerRef.current) {
        clearTimeout(debounceTimerRef.current);
      }
    };
  }, []);

  const handleDayChange = useCallback((index: number) => {
    const newDate = new Date(localDate);
    newDate.setDate(index + 1);
    updateDate(newDate);
  }, [localDate, updateDate]);

  const handleMonthChange = useCallback((index: number) => {
    const newDate = new Date(localDate);
    const currentDay = newDate.getDate();
    const currentYear = newDate.getFullYear();

    // IMPORTANT: Ajuster le jour AVANT setMonth pour éviter le débordement JavaScript
    // Ex: 31 janvier → novembre: si on fait setMonth(10) d'abord, JS déborde au 1er décembre!
    const maxDayInNewMonth = getDaysInMonth(index, currentYear);
    if (currentDay > maxDayInNewMonth) {
      newDate.setDate(maxDayInNewMonth);
    }

    // MAINTENANT on peut changer le mois sans risque de débordement
    newDate.setMonth(index);
    updateDate(newDate);
  }, [localDate, getDaysInMonth, updateDate]);

  const handleYearChange = useCallback((index: number) => {
    const newYear = years[index];
    const newDate = new Date(localDate);
    const currentDay = newDate.getDate();
    const currentMonth = newDate.getMonth();

    // IMPORTANT: Ajuster le jour AVANT setFullYear pour éviter le débordement JavaScript
    // Ex: 29 février année bissextile → année non-bissextile: JS déborderait au 1er mars!
    const maxDayInNewYear = getDaysInMonth(currentMonth, newYear);
    if (currentDay > maxDayInNewYear) {
      newDate.setDate(maxDayInNewYear);
    }

    // MAINTENANT on peut changer l'année sans risque de débordement
    newDate.setFullYear(newYear);
    updateDate(newDate);
  }, [localDate, years, getDaysInMonth, updateDate]);

  const { width: screenWidth } = Dimensions.get('window');
  const pickerWidth = Math.min(screenWidth - spacing.xl * 2, 340);
  const dayWidth = pickerWidth * 0.2;
  const monthWidth = pickerWidth * 0.45;
  const yearWidth = pickerWidth * 0.35;

  const formatDay = useCallback((day: string | number) => String(day).padStart(2, '0'), []);

  return (
    <View style={[styles.container, { width: pickerWidth }]}>
      {/* Indicateur de sélection (ligne centrale) */}
      <View style={styles.selectionIndicator}>
        <LinearGradient
          colors={['rgba(183, 148, 246, 0)', 'rgba(183, 148, 246, 0.3)', 'rgba(183, 148, 246, 0)']}
          start={{ x: 0, y: 0.5 }}
          end={{ x: 1, y: 0.5 }}
          style={styles.selectionLine}
        />
      </View>

      {/* Masque de dégradé en haut */}
      <LinearGradient
        colors={['rgba(10, 14, 39, 1)', 'rgba(10, 14, 39, 0)']}
        style={styles.gradientTop}
        pointerEvents="none"
      />

      {/* Masque de dégradé en bas */}
      <LinearGradient
        colors={['rgba(10, 14, 39, 0)', 'rgba(10, 14, 39, 1)']}
        style={styles.gradientBottom}
        pointerEvents="none"
      />

      <View style={styles.wheelsContainer}>
        {/* Jour */}
        <WheelColumn
          data={days}
          selectedIndex={dayIndex}
          onSelect={handleDayChange}
          width={dayWidth}
          formatItem={formatDay}
        />

        {/* Mois */}
        <WheelColumn
          data={MONTHS}
          selectedIndex={monthIndex}
          onSelect={handleMonthChange}
          width={monthWidth}
        />

        {/* Année */}
        <WheelColumn
          data={years}
          selectedIndex={yearIndex >= 0 ? yearIndex : 0}
          onSelect={handleYearChange}
          width={yearWidth}
        />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    height: PICKER_HEIGHT,
    backgroundColor: 'rgba(183, 148, 246, 0.08)',
    borderRadius: borderRadius.lg,
    overflow: 'hidden',
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.2)',
  },
  wheelsContainer: {
    flexDirection: 'row',
    height: PICKER_HEIGHT,
  },
  wheelColumn: {
    height: PICKER_HEIGHT,
  },
  wheelItem: {
    height: ITEM_HEIGHT,
    justifyContent: 'center',
    alignItems: 'center',
  },
  wheelText: {
    fontSize: 18,
    color: 'rgba(255, 255, 255, 0.4)',
    fontWeight: '500',
  },
  wheelTextMonth: {
    fontSize: 16,
  },
  wheelTextSelected: {
    color: colors.text,
    fontWeight: '700',
    fontSize: 20,
    textShadowColor: 'rgba(183, 148, 246, 0.5)',
    textShadowOffset: { width: 0, height: 1 },
    textShadowRadius: 4,
  },
  selectionIndicator: {
    position: 'absolute',
    top: (PICKER_HEIGHT - ITEM_HEIGHT) / 2,
    left: 0,
    right: 0,
    height: ITEM_HEIGHT,
    justifyContent: 'center',
    zIndex: 1,
    pointerEvents: 'none',
  },
  selectionLine: {
    height: ITEM_HEIGHT,
    borderRadius: borderRadius.sm,
  },
  gradientTop: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    height: ITEM_HEIGHT * 1.5,
    zIndex: 2,
  },
  gradientBottom: {
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    height: ITEM_HEIGHT * 1.5,
    zIndex: 2,
  },
});

export default DateWheelPicker;
