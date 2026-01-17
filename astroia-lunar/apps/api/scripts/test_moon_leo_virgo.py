"""
Test pour trouver quand la Lune passe de Lion à Vierge le 9 février 2001
"""

import sys
from pathlib import Path
from datetime import datetime, timezone, timedelta

sys.path.insert(0, str(Path(__file__).parent.parent))

from services.swiss_ephemeris import get_moon_position

def find_moon_sign_change():
    """
    Cherche le moment où la Lune passe de Lion à Vierge le 9 février 2001
    """
    print("=" * 60)
    print("RECHERCHE DU PASSAGE LUNE LEO → VIRGO")
    print("9 février 2001 - Bordeaux")
    print("=" * 60)
    print()

    # Tester chaque heure de la journée
    base_date = datetime(2001, 2, 9, 0, 0, 0, tzinfo=timezone.utc)

    print("Positions de la Lune par heure (UTC):")
    print("-" * 60)

    leo_virgo_boundary = None

    for hour in range(24):
        test_time = base_date + timedelta(hours=hour)
        moon_pos = get_moon_position(test_time)

        status = "🌙" if moon_pos.sign == "Virgo" else "🦁"
        print(f"{hour:02d}:00 UTC → {status} {moon_pos.sign} ({moon_pos.longitude:.2f}°)")

        # Détecter le passage
        if hour > 0:
            prev_time = base_date + timedelta(hours=hour-1)
            prev_moon = get_moon_position(prev_time)
            if prev_moon.sign == "Leo" and moon_pos.sign == "Virgo":
                leo_virgo_boundary = (prev_time, test_time)

    print()
    print("=" * 60)

    if leo_virgo_boundary:
        print(f"✅ La Lune passe de Leo à Virgo entre:")
        print(f"   {leo_virgo_boundary[0].strftime('%H:%M')} UTC et {leo_virgo_boundary[1].strftime('%H:%M')} UTC")
        print()

        # Affiner la recherche
        start, end = leo_virgo_boundary
        for minute in range(0, 60, 10):
            test_time = start + timedelta(minutes=minute)
            moon_pos = get_moon_position(test_time)
            print(f"   {test_time.strftime('%H:%M')} UTC → {moon_pos.sign} ({moon_pos.longitude:.2f}°)")

        print()
        print("La frontière Leo/Virgo est à 150°")

    # Test spécifique pour Nathan (10:30 UTC = 11:30 Europe/Paris)
    print()
    print("=" * 60)
    print("POSITION POUR NATHAN:")
    print("=" * 60)
    nathan_time_utc = datetime(2001, 2, 9, 10, 30, 0, tzinfo=timezone.utc)
    nathan_moon = get_moon_position(nathan_time_utc)

    print(f"📅 Heure de naissance: 11:30 Europe/Paris (10:30 UTC)")
    print(f"🌙 Position Lune: {nathan_moon.sign} ({nathan_moon.longitude:.2f}°)")
    print(f"   Degré dans le signe: {nathan_moon.degree:.2f}°")
    print()

    if nathan_moon.sign == "Virgo":
        print("✅ Correct: La Lune est bien en Vierge")
    else:
        print(f"❌ Erreur: La Lune est en {nathan_moon.sign}, devrait être en Vierge")

if __name__ == "__main__":
    find_moon_sign_change()
