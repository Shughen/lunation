/**
 * Hook pour feedback haptique (vibrations iOS)
 */

import * as Haptics from 'expo-haptics';
import { Platform } from 'react-native';

export function useHapticFeedback() {
  const impact = {
    light: () => {
      if (Platform.OS === 'ios') {
        Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light);
      }
    },
    medium: () => {
      if (Platform.OS === 'ios') {
        Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Medium);
      }
    },
    heavy: () => {
      if (Platform.OS === 'ios') {
        Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Heavy);
      }
    },
  };

  const notification = {
    success: () => {
      if (Platform.OS === 'ios') {
        Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success);
      }
    },
    warning: () => {
      if (Platform.OS === 'ios') {
        Haptics.notificationAsync(Haptics.NotificationFeedbackType.Warning);
      }
    },
    error: () => {
      if (Platform.OS === 'ios') {
        Haptics.notificationAsync(Haptics.NotificationFeedbackType.Error);
      }
    },
  };

  const selection = () => {
    if (Platform.OS === 'ios') {
      Haptics.selectionAsync();
    }
  };

  return {
    impact,
    notification,
    selection,
  };
}

export default useHapticFeedback;

