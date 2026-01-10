#!/usr/bin/env node
/**
 * Vérifie la compatibilité Expo Go
 * Détecte les imports de modules natifs incompatibles
 */

const fs = require('fs');
const path = require('path');

const INCOMPATIBLE_MODULES = [
  'expo-notifications',
  'expo-print',
  'expo-sharing',
  '@sentry/react-native',
  'expo-camera',
  'expo-media-library',
];

const DIRS_TO_CHECK = ['app', 'components', 'lib'];

let hasErrors = false;

function checkFile(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  
  INCOMPATIBLE_MODULES.forEach(module => {
    if (content.includes(`from '${module}'`) || content.includes(`from "${module}"`)) {
      console.error(`❌ ${filePath}: imports "${module}" (incompatible Expo Go)`);
      hasErrors = true;
    }
  });
}

function scanDirectory(dir) {
  const items = fs.readdirSync(dir);
  
  items.forEach(item => {
    const fullPath = path.join(dir, item);
    const stat = fs.statSync(fullPath);
    
    if (stat.isDirectory() && !item.startsWith('.') && item !== 'node_modules') {
      scanDirectory(fullPath);
    } else if (item.endsWith('.js') || item.endsWith('.jsx')) {
      checkFile(fullPath);
    }
  });
}

console.log('🔍 Vérification compatibilité Expo Go...\n');

DIRS_TO_CHECK.forEach(dir => {
  if (fs.existsSync(dir)) {
    scanDirectory(dir);
  }
});

if (hasErrors) {
  console.log('\n❌ Modules natifs détectés ! Utilise "npx expo run:ios" ou désactive-les.\n');
  process.exit(1);
} else {
  console.log('✅ Aucun module natif détecté. Compatible Expo Go !\n');
  process.exit(0);
}

