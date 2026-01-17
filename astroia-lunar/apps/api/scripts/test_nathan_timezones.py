"""
Test des différentes timezones pour comprendre l'erreur de calcul de la Lune
"""

import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent.parent))

from services.swiss_ephemeris import get_moon_position

def test_different_timezones():
    """
    Test la position de la Lune avec différentes interprétations de timezone
    """
    print("=" * 60)
    print("TEST DIAGNOSTIC - POSITION LUNE SELON TIMEZONE")
    print("=" * 60)
    print()

    scenarios = [
        {
            "name": "CORRECT - 11:30 Europe/Paris (11:30 locale = 10:30 UTC en hiver)",
            "utc_time": datetime(2001, 2, 9, 10, 30, 0, tzinfo=timezone.utc),
            "expected": "Virgo (selon Astrotheme)"
        },
        {
            "name": "ERREUR 1 - 11:30 UTC (interprétation incorrecte)",
            "utc_time": datetime(2001, 2, 9, 11, 30, 0, tzinfo=timezone.utc),
            "expected": "Possiblement Leo?"
        },
        {
            "name": "ERREUR 2 - 11:30 Europe/Paris été (UTC+2 = 09:30 UTC)",
            "utc_time": datetime(2001, 2, 9, 9, 30, 0, tzinfo=timezone.utc),
            "expected": "Possiblement Leo?"
        },
    ]

    for scenario in scenarios:
        print(f"📅 Scénario: {scenario['name']}")
        print(f"   UTC: {scenario['utc_time'].isoformat()}")

        moon_pos = get_moon_position(scenario['utc_time'])

        status = "✅" if moon_pos.sign == "Virgo" else "❌"
        print(f"   {status} Résultat: {moon_pos.sign} à {moon_pos.longitude:.2f}°")
        print(f"   Note: {scenario['expected']}")
        print()

    print("=" * 60)
    print("DIAGNOSTIC:")
    print("=" * 60)
    print()
    print("Si la Lune est affichée en Lion (Leo) dans le thème de Nathan,")
    print("c'est probablement parce que le thème a été calculé avec:")
    print("  - 11:30 UTC au lieu de 11:30 Europe/Paris")
    print("  - OU une mauvaise gestion de la timezone lors du calcul initial")
    print()
    print("SOLUTION: Recalculer le thème avec les bonnes données (timezone=Europe/Paris)")
    print()

if __name__ == "__main__":
    test_different_timezones()
