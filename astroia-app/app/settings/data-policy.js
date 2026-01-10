import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Stack } from 'expo-router';
import { colors, fonts, spacing } from '@/constants/theme';

const POLICY_TEXT = `📋 POLITIQUE DE CONFIDENTIALITÉ ET DE PROTECTION DES DONNÉES
LUNA - Cycle & Cosmos

Dernière mise à jour : 9 novembre 2025
Version : 2.0.0

Cette politique explique comment LUNA collecte, utilise et protège vos données personnelles, en particulier vos données de santé relatives au cycle menstruel.

🛡️ Responsable du Traitement

Responsable : Rémi Beaurain
Contact DPO : privacy@luna-app.fr
Siège : France (UE)

📊 Données Collectées

1. Données de Profil
• Prénom
• Date de naissance
• Heure et lieu de naissance (pour calculs astrologiques)
• Adresse email (authentification)

2. Données de Santé (Art. 9 RGPD)
• Dates de règles
• Durée du cycle menstruel
• Phase de cycle actuelle
• Notes d'humeur et symptômes

Ces données de santé nécessitent votre CONSENTEMENT EXPLICITE.

3. Données d'Usage
• Interactions avec l'IA
• Historique de consultations (horoscope, compatibilité)
• Analyses effectuées
• Badges et streaks obtenus

4. Données Techniques (si consentement analytics)
• Type d'appareil et OS
• Version de l'app
• Événements d'utilisation anonymisés

🎯 Finalités du Traitement

Vos données sont utilisées pour :

• Calculs astrologiques personnalisés
• Suivi et prédiction du cycle menstruel
• Recommandations de bien-être adaptées à votre phase
• Génération de conseils IA personnalisés
• Amélioration de l'application (si consentement analytics)

Base légale :
• Consentement explicite (Art. 9 RGPD pour données de santé)
• Exécution du contrat (fourniture du service)

🔒 Sécurité et Stockage

Hébergement :
• Données stockées exclusivement dans l'UE (Supabase - Allemagne)
• Chiffrement en transit (TLS 1.3)
• Chiffrement au repos (AES-256)

Accès :
• Aucun accès humain sans votre consentement
• Logs d'accès conservés
• Authentification forte (Magic Link)

🌍 Sous-traitants (Art. 28 RGPD)

Nous utilisons les sous-traitants suivants (tous conformes RGPD avec DPA et SCC) :

1. Supabase (Allemagne - UE)
   • Base de données et authentification
   • Data Processing Agreement (DPA) : ✅
   • Standard Contractual Clauses (SCC) : ✅

2. Vercel (Pays-Bas - UE)
   • API proxy et serverless functions
   • DPA : ✅
   • SCC : ✅

3. OpenAI (USA)
   • Assistant IA conversationnel
   • DPA : ✅
   • SCC : ✅
   • Transferts UE-USA : sur base juridique valide

4. Mixpanel (USA)
   • Analytics anonymisés (si consentement)
   • DPA : ✅
   • SCC : ✅

⚠️ VOS DONNÉES DE SANTÉ NE SONT JAMAIS TRANSFÉRÉES HORS UE

Seules les interactions IA (texte) peuvent être transmises à OpenAI (USA).
Vos données de cycle restent exclusivement sur serveurs UE.

⏳ Durée de Conservation

• Données de profil : tant que compte actif + 30 jours après suppression
• Données de santé : tant que compte actif, supprimées immédiatement si compte supprimé
• Historique analyses : 2 ans max
• Logs techniques : 6 mois
• Logs d'audit RGPD : 3 ans (obligation légale)

Vous pouvez demander la suppression anticipée à tout moment.

✅ Vos Droits RGPD

Vous disposez des droits suivants :

1. Droit d'accès (Art. 15)
   • Obtenir une copie de vos données

2. Droit de rectification (Art. 16)
   • Corriger vos informations

3. Droit à l'effacement (Art. 17)
   • Supprimer votre compte et toutes vos données

4. Droit à la portabilité (Art. 20)
   • Exporter vos données au format JSON

5. Droit d'opposition (Art. 21)
   • Retirer votre consentement à tout moment

6. Droit de limitation (Art. 18)
   • Restreindre le traitement

📥 Exercer Vos Droits

Settings > Confidentialité > "Exporter mes données"
Settings > Confidentialité > "Supprimer mon compte"

Ou par email : privacy@luna-app.fr
Délai de réponse : 30 jours max (Art. 12.3 RGPD)

🇫🇷 Réclamation CNIL

Si vous estimez que vos droits ne sont pas respectés :

CNIL (Commission Nationale de l'Informatique et des Libertés)
3 Place de Fontenoy
TSA 80715
75334 PARIS CEDEX 07
Tél : 01 53 73 22 22
https://www.cnil.fr/

🍪 Cookies et Traceurs

LUNA n'utilise PAS de cookies tiers.

Traceurs utilisés (si consentement analytics) :
• Mixpanel SDK (analytics anonymisés)
• Sentry (monitoring erreurs)

Vous pouvez refuser les analytics dans Settings > Confidentialité.

🔄 Modifications de la Politique

En cas de modification substantielle :
• Notification par email
• Demande de nouveau consentement si nécessaire
• Version toujours accessible dans l'app

📧 Contact

Pour toute question sur vos données :
• Email : privacy@luna-app.fr
• DPO : dpo@luna-app.fr
• Support : support@luna-app.fr

Nous nous engageons à répondre sous 48h ouvrées.

💜 Notre Engagement

• Transparence totale sur l'usage de vos données
• Jamais de vente de données à des tiers
• Respect strict du RGPD
• Protection maximale des données de santé
• Vous gardez le contrôle total

Merci de votre confiance 🌙`;

export default function DataPolicyScreen() {
  return (
    <View style={styles.wrapper}>
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <SafeAreaView style={styles.safeArea} edges={['top']}>
          <Stack.Screen
            options={{
              title: 'Politique de Confidentialité',
              headerStyle: { backgroundColor: '#0F172A' },
              headerTintColor: '#fff',
              headerShadowVisible: false,
            }}
          />

          <ScrollView 
            style={styles.scrollView}
            contentContainerStyle={styles.content}
            showsVerticalScrollIndicator={false}
          >
            <Text style={styles.policyText}>{POLICY_TEXT}</Text>
          </ScrollView>
        </SafeAreaView>
      </LinearGradient>
    </View>
  );
}

const styles = StyleSheet.create({
  wrapper: {
    flex: 1,
    backgroundColor: '#0F172A',
  },
  container: {
    flex: 1,
  },
  safeArea: {
    flex: 1,
  },
  scrollView: {
    flex: 1,
  },
  content: {
    padding: spacing.md,
    paddingBottom: spacing.xl * 2,
  },
  policyText: {
    fontFamily: fonts.regular,
    fontSize: 15,
    lineHeight: 24,
    color: colors.textSecondary,
  },
});

