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
import { colors, fonts, spacing, borderRadius } from '@/constants/theme';

const DISCLAIMER_TEXT = `⚠️ DISCLAIMER – LUNA - Cycle & Cosmos

À propos de LUNA

LUNA - Cycle & Cosmos est une application de bien-être et d'accompagnement personnel qui combine le suivi du cycle menstruel avec des informations astrologiques pour aider les utilisatrices à mieux comprendre leur énergie et leurs émotions.

🩺 Avertissement Médical

Ce que LUNA N'EST PAS :

❌ LUNA n'est PAS un dispositif médical
❌ LUNA n'est PAS un outil de diagnostic
❌ LUNA ne remplace PAS un avis médical professionnel
❌ LUNA ne fournit PAS de conseils médicaux

Ce que LUNA EST :

✅ Un outil de bien-être personnel
✅ Un journal pour suivre votre cycle et vos émotions
✅ Une source d'informations générales sur les cycles biologiques et lunaires
✅ Un assistant conversationnel pour le bien-être général (non médical)

🔍 Utilisation Recommandée

LUNA est conçu pour :
• Suivre votre cycle menstruel de manière informative
• Vous aider à mieux comprendre vos fluctuations émotionnelles et énergétiques
• Fournir des suggestions de bien-être adaptées à votre phase de cycle
• Offrir un journal personnel pour noter vos observations
• Proposer des insights basés sur l'astrologie (pour le divertissement et la réflexion personnelle)

⚠️ AVERTISSEMENT IMPORTANT

Si vous présentez l'un des symptômes suivants, consultez IMMÉDIATEMENT un professionnel de santé :

• Saignements anormaux ou hémorragiques
• Douleurs pelviennes sévères ou inhabituelles
• Cycles irréguliers soudains (si vous étiez régulière auparavant)
• Absence de règles (aménorrhée) sans raison évidente
• Symptômes de grossesse non planifiée
• Tout changement brusque ou inquiétant dans votre santé reproductive

🏥 Contraception et Prévention

LUNA N'EST PAS une méthode de contraception.

• Ne vous fiez JAMAIS aux prédictions de cycle de LUNA pour éviter une grossesse
• L'application ne remplace pas les méthodes contraceptives reconnues
• En cas de doute sur une grossesse, consultez un médecin ou faites un test

🔮 Astrologie et Intelligence Artificielle

• L'astrologie est considérée comme un système symbolique et n'est PAS reconnue comme une science exacte
• Les interprétations astrologiques fournies par LUNA ont un but de divertissement et de réflexion personnelle
• L'IA de LUNA (ChatGPT) génère des réponses automatiques qui ne sont PAS vérifiées par des professionnels de santé
• Ne prenez jamais de décisions médicales importantes basées uniquement sur des conseils astrologiques ou IA

🛡️ Votre Sécurité d'Abord

En cas de doute sur votre santé physique ou mentale :

1. Consultez un médecin généraliste
2. Contactez un gynécologue
3. Appelez le 15 (urgences médicales en France)
4. Rendez-vous aux urgences si nécessaire

📋 Responsabilité

En utilisant LUNA, vous reconnaissez et acceptez que :

• Vous êtes seule responsable de vos décisions de santé
• Les créateurs de LUNA ne peuvent être tenus responsables de décisions prises sur la base des informations fournies par l'application
• LUNA est un outil de bien-être complémentaire, jamais un substitut à un suivi médical professionnel
• Les données de cycle fournies sont des estimations basées sur des moyennes statistiques, pas des garanties

💜 Notre Engagement

Nous nous engageons à :

• Respecter strictement votre vie privée (RGPD)
• Ne jamais vendre vos données de santé
• Fournir des informations de bien-être basées sur des sources reconnues
• Vous rappeler régulièrement les limites de l'application
• Améliorer continuellement la qualité de nos recommandations de bien-être (non médicales)

📧 Contact

Si vous avez des questions ou des préoccupations :
• Email : support@luna-app.fr
• LUNA est développée et maintenue en France

Dernière mise à jour : 9 novembre 2025
Version : 2.0.0`;

export default function DisclaimerScreen() {
  return (
    <View style={styles.wrapper}>
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <SafeAreaView style={styles.safeArea} edges={['top']}>
          <Stack.Screen
            options={{
              title: 'Disclaimer Médical',
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
            <Text style={styles.disclaimerText}>{DISCLAIMER_TEXT}</Text>
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
  disclaimerText: {
    fontFamily: fonts.regular,
    fontSize: 15,
    lineHeight: 24,
    color: colors.textSecondary,
  },
});

