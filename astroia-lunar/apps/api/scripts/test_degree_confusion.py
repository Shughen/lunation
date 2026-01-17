"""
Test pour vérifier s'il y a une confusion entre degree et absolute_longitude
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

def test_degree_confusion():
    """
    Test différentes interprétations du champ 'degree'
    """
    print("=" * 80)
    print("TEST - CONFUSION DEGREE vs ABSOLUTE_LONGITUDE")
    print("=" * 80)
    print()

    # Données RapidAPI pour la Lune de Nathan
    moon_data = {
        "degree": 6.9,
        "absolute_longitude": 156.9,
        "sign": "Vir"
    }

    signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
             'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

    print("Données RapidAPI:")
    print(f"  degree: {moon_data['degree']}")
    print(f"  absolute_longitude: {moon_data['absolute_longitude']}")
    print(f"  sign: {moon_data['sign']}")
    print()

    # Scénario 1: degree = degré dans le signe (CORRECT)
    print("Scénario 1: degree = degré dans le signe")
    print(f"  → {moon_data['degree']}° en {moon_data['sign']} (Virgo)")
    print(f"  → ✅ CORRECT")
    print()

    # Scénario 2: degree = longitude absolue (ERREUR)
    print("Scénario 2: Si on confond degree avec longitude absolue")
    sign_index = int(moon_data['degree'] / 30)
    if sign_index < len(signs):
        wrong_sign = signs[sign_index]
        print(f"  → {moon_data['degree']}° / 30 = signe index {sign_index} = {wrong_sign}")
        print(f"  → ❌ ERREUR: donnerait {wrong_sign} au lieu de Virgo")
    print()

    # Scénario 3: absolute_longitude interprété comme degree (CORRECT normalement)
    print("Scénario 3: absolute_longitude converti en signe")
    sign_index = int(moon_data['absolute_longitude'] / 30)
    degree_in_sign = moon_data['absolute_longitude'] % 30
    if sign_index < len(signs):
        calculated_sign = signs[sign_index]
        print(f"  → {moon_data['absolute_longitude']}° / 30 = signe index {sign_index} = {calculated_sign}")
        print(f"  → Degré dans le signe: {degree_in_sign:.2f}°")
        print(f"  → ✅ CORRECT")
    print()

    # Scénario 4: Calcul inverse - quelle longitude donnerait Leo?
    print("Scénario 4: Pour avoir Leo, il faudrait:")
    leo_index = signs.index('Leo')
    leo_start = leo_index * 30
    leo_end = (leo_index + 1) * 30
    print(f"  → Longitude entre {leo_start}° et {leo_end}°")
    print(f"  → Exemple: 136.9° donnerait Leo à 6.9°")
    print()

    # Test: quelle longitude donnerait Leo avec le même degree?
    test_longitude = leo_start + moon_data['degree']
    test_sign_index = int(test_longitude / 30)
    test_sign = signs[test_sign_index]
    print(f"Test: {test_longitude}° → {test_sign} {moon_data['degree']}°")
    print()

    # Hypothèse: Est-ce que RapidAPI retourne parfois degree comme longitude?
    print("=" * 80)
    print("HYPOTHÈSE:")
    print("=" * 80)
    print()
    print("Si RapidAPI retourne parfois:")
    print("  - degree = 136.9 (longitude absolue, mais nommé 'degree')")
    print("  - sign = 'Leo' (calculé depuis cette longitude)")
    print()
    print("Alors le code qui fait degree % 30 donnerait:")
    test_wrong = 136.9 % 30
    print(f"  136.9 % 30 = {test_wrong:.2f}° → Leo {test_wrong:.2f}°")
    print()
    print("Mais cela semble peu probable car RapidAPI retourne actuellement:")
    print(f"  degree = {moon_data['degree']} ✅ (degree dans le signe)")
    print(f"  absolute_longitude = {moon_data['absolute_longitude']} ✅ (longitude totale)")
    print()

if __name__ == "__main__":
    test_degree_confusion()
