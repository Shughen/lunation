## Daily Climate - Persistance de la consultation

### 🎯 Améliorations

**Persistance de la consultation**
- La consultation du Daily Climate est maintenant persistée lors du chargement depuis l'écran Lunar (flag AsyncStorage `dailyClimate:lastViewedDate`)
- Un badge discret "✓ Consulté aujourd'hui" s'affiche automatiquement sur Home et Lunar quand le Daily Climate a été consulté dans la journée

**Rechargement automatique sur Lunar**
- Si le Daily Climate a déjà été consulté aujourd'hui, il se ré-affiche automatiquement au retour sur l'écran Lunar
- Le rechargement utilise le cache `requestGuard` (pas de nouveau fetch API)
- Le badge "✓ Consulté aujourd'hui" reste visible

**Navigation améliorée depuis Home**
- Le bouton CTA "Voir le climat lunaire" dans la carte Daily Ritual ouvre directement `/lunar?focus=daily_climate`
- Scroll automatique vers la section Daily Climate à l'arrivée

### 🔧 Détails techniques

- AsyncStorage : clé `dailyClimate:lastViewedDate` (format YYYY-MM-DD)
- Tracking analytics : événement `daily_climate_view` avec propriétés `{ firstOfDay, source: 'lunar' | 'home' }`
- Badge UI : style discret (fond vert semi-transparent, coin supérieur droit de la carte)

