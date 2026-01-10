## 1. Objectif du MVP

Astroia Lunar est une app d'astrologie centrée sur les **révolutions lunaires**.

Le MVP doit permettre à un utilisateur de :

1. Créer un compte et enregistrer ses données de naissance (date, heure, lieu).
2. Calculer un **mois lunaire personnel** à partir de sa révolution lunaire :
   - prochaine date de révolution lunaire,
   - découpage du cycle en 4 phases (début, montée, apogée, intégration),
   - assigner un "jour de cycle" (1 à 28) à chaque date.
3. Consulter :
   - un écran **"Mois lunaire"** avec une vue globale du cycle en cours,
   - un écran **"Aujourd'hui"** qui explique où il se trouve dans le cycle et ce que ça signifie.
4. Discuter avec un **chat IA** qui répond en tenant compte de :
   - son thème natal,
   - sa position dans le cycle lunaire,
   - son focus principal (émotionnel / pro).

Le but est de proposer une expérience :
- précise et transparente,
- centrée sur les émotions et les décisions du mois en cours,
- sans modèle de monétisation agressif dans le MVP.


## 4. Modèle de cycle lunaire simplifié (v1)

Pour le MVP, nous utilisons un modèle simplifié :

- Le cycle lunaire personnel dure 28 jours.
- Le **Jour 1** correspond à la date exacte de la prochaine révolution lunaire.
- Les phases sont :
  - Phase 1 (Jours 1-7) : "Ouverture & nouveaux ressentis"
  - Phase 2 (Jours 8-14) : "Montée émotionnelle & prises de conscience"
  - Phase 3 (Jours 15-21) : "Apogée & tension intérieure"
  - Phase 4 (Jours 22-28) : "Intégration & retour à soi"

Ce modèle sera affiné plus tard avec de vrais aspects/maisons.


### Table `lunar_cycles`

- id (uuid)
- user_id (fk users.id)
- cycle_start_date (date)  // date du jour 1 (révolution lunaire)
- cycle_end_date (date)    // cycle_start_date + 27 jours
- created_at (timestamp)

### Table `lunar_daily_states`

- id (uuid)
- user_id (fk users.id)
- date (date)
- cycle_day (int)          // 1 à 28, null si hors cycle
- phase (text)             // 'start', 'rise', 'peak', 'integration'
- created_at (timestamp)