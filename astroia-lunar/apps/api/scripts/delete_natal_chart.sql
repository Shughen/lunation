-- Script pour supprimer le thème natal incorrect de user_id=1
-- À exécuter après le redémarrage de l'API avec RapidAPI

DELETE FROM natal_charts WHERE user_id = 1;

-- Vérifier qu'il est bien supprimé
SELECT COUNT(*) as remaining_charts FROM natal_charts WHERE user_id = 1;
-- Expected: 0
