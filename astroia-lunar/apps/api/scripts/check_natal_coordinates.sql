-- Vérifier si le natal_chart a bien les coordonnées
SELECT
    id,
    user_id,
    birth_date,
    birth_time,
    birth_place,
    latitude,
    longitude,
    timezone,
    created_at,
    updated_at
FROM natal_charts
WHERE user_id = 1
ORDER BY updated_at DESC
LIMIT 1;
