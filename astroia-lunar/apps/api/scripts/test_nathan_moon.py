"""
Script de test pour vérifier la position de la Lune de Nathan
Né le 9 février 2001 à 11h30 à Bordeaux
D'après Astrotheme: Lune en Vierge
"""

import sys
from datetime import datetime, timezone
from pathlib import Path

# Ajouter le répertoire parent au PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from services.swiss_ephemeris import get_moon_position, degree_to_sign

def test_nathan_moon():
    """
    Test la position de la Lune pour Nathan
    Né le 9 février 2001 à 11h30 à Bordeaux
    Bordeaux: lat=44.8378, lon=-0.5792
    """
    # Date de naissance en UTC (11h30 heure locale = 10h30 UTC en hiver)
    # Le 9 février 2001, la France était en UTC+1 (heure d'hiver)
    birth_datetime_local = datetime(2001, 2, 9, 11, 30, 0)
    # Convertir en UTC : 11h30 - 1h = 10h30 UTC
    birth_datetime_utc = datetime(2001, 2, 9, 10, 30, 0, tzinfo=timezone.utc)

    print(f"📅 Date de naissance (locale): {birth_datetime_local.isoformat()}")
    print(f"📅 Date de naissance (UTC): {birth_datetime_utc.isoformat()}")
    print()

    # Calculer la position de la Lune avec Swiss Ephemeris
    moon_pos = get_moon_position(birth_datetime_utc)

    print(f"🌙 Position de la Lune calculée:")
    print(f"   - Longitude: {moon_pos.longitude}°")
    print(f"   - Signe: {moon_pos.sign}")
    print(f"   - Degré dans le signe: {moon_pos.degree}°")
    print(f"   - Phase: {moon_pos.phase}")
    print()

    # Vérification
    expected_sign = "Virgo"  # D'après Astrotheme
    if moon_pos.sign == expected_sign:
        print(f"✅ CORRECT: La Lune est bien en {expected_sign}")
    else:
        print(f"❌ ERREUR: La Lune devrait être en {expected_sign}, mais le calcul donne {moon_pos.sign}")
        print()
        print(f"💡 Debug:")
        print(f"   - Longitude attendue pour Vierge: 150-180°")
        print(f"   - Longitude calculée: {moon_pos.longitude}°")

        # Test avec différents décalages de timezone
        print()
        print(f"🔍 Test avec différents décalages de timezone:")
        for tz_offset in [0, 1, 2]:
            test_utc = datetime(2001, 2, 9, 11 - tz_offset, 30, 0, tzinfo=timezone.utc)
            test_moon = get_moon_position(test_utc)
            print(f"   UTC-{tz_offset}h: {test_moon.sign} ({test_moon.longitude:.2f}°)")

if __name__ == "__main__":
    test_nathan_moon()
