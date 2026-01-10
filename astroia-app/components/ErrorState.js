/**
 * Composant Error State réutilisable
 * Affiche un message d'erreur élégant avec retry
 */

import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { Ionicons } from '@expo/vector-icons';

export function ErrorState({
  icon = 'alert-circle-outline',
  title = 'Une erreur est survenue',
  message = 'Impossible de charger les données',
  retryLabel = 'Réessayer',
  onRetry,
  style,
}) {
  return (
    <View style={[styles.container, style]}>
      <Ionicons name={icon} size={80} color="#EF4444" />
      <Text style={styles.title}>{title}</Text>
      <Text style={styles.message}>{message}</Text>
      
      {onRetry && (
        <TouchableOpacity style={styles.retryButton} onPress={onRetry}>
          <Ionicons name="refresh" size={20} color="#fff" />
          <Text style={styles.retryText}>{retryLabel}</Text>
        </TouchableOpacity>
      )}
    </View>
  );
}

export function NetworkError({ onRetry }) {
  return (
    <ErrorState
      icon="cloud-offline-outline"
      title="Pas de connexion"
      message="Vérifiez votre connexion internet et réessayez"
      onRetry={onRetry}
    />
  );
}

export function ServerError({ onRetry }) {
  return (
    <ErrorState
      icon="server-outline"
      title="Problème serveur"
      message="Nos serveurs rencontrent un problème temporaire"
      onRetry={onRetry}
    />
  );
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 60,
    paddingHorizontal: 40,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff',
    marginTop: 20,
    marginBottom: 10,
    textAlign: 'center',
  },
  message: {
    fontSize: 14,
    color: 'rgba(255, 255, 255, 0.7)',
    textAlign: 'center',
    lineHeight: 20,
    marginBottom: 24,
  },
  retryButton: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: 'rgba(139, 92, 246, 0.8)',
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 12,
  },
  retryText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
});

