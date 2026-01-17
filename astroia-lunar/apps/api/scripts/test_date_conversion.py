"""
Test de conversion de date pour comprendre le décalage d'un jour
"""

from datetime import date, datetime, time, timezone
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

def test_date_conversion():
    """
    Test différentes conversions de date pour identifier le bug
    """
    print("=" * 80)
    print("TEST - CONVERSION DE DATE (BUG -1 JOUR)")
    print("=" * 80)
    print()

    # Ce que le mobile envoie (supposément)
    input_date_string = "2001-02-09"
    input_time_string = "11:30"

    print(f"INPUT (ce que le mobile envoie):")
    print(f"  date: {input_date_string}")
    print(f"  time: {input_time_string}")
    print()

    # Conversion côté backend (routes/natal.py ligne 371)
    print("CONVERSION 1 - Backend (date.fromisoformat)")
    print("-" * 80)
    birth_date_obj = date.fromisoformat(input_date_string)
    print(f"  date.fromisoformat('{input_date_string}')")
    print(f"  → {birth_date_obj}")
    print(f"  → type: {type(birth_date_obj)}")
    print()

    # Conversion time
    print("CONVERSION 2 - Backend (time)")
    print("-" * 80)
    hour, minute = map(int, input_time_string.split(":"))
    birth_time_obj = time(hour, minute)
    print(f"  time({hour}, {minute})")
    print(f"  → {birth_time_obj}")
    print()

    # Test: Est-ce que la date change quand on la combine avec l'heure et le timezone?
    print("CONVERSION 3 - Combinaison date + time + timezone")
    print("-" * 80)

    # Créer datetime en local
    dt_naive = datetime.combine(birth_date_obj, birth_time_obj)
    print(f"  datetime.combine(date, time) [naive]:")
    print(f"  → {dt_naive}")
    print()

    # Appliquer timezone Europe/Paris
    from zoneinfo import ZoneInfo
    try:
        paris_tz = ZoneInfo("Europe/Paris")
        dt_paris = dt_naive.replace(tzinfo=paris_tz)
        print(f"  .replace(tzinfo=ZoneInfo('Europe/Paris')):")
        print(f"  → {dt_paris}")
        print(f"  → ISO: {dt_paris.isoformat()}")
        print()

        # Convertir en UTC
        dt_utc = dt_paris.astimezone(timezone.utc)
        print(f"  .astimezone(timezone.utc):")
        print(f"  → {dt_utc}")
        print(f"  → Date UTC: {dt_utc.date()}")
        print()

        # ALERTE: Si on convertit en UTC, la date pourrait changer!
        if dt_utc.date() != birth_date_obj:
            print(f"  ⚠️ ATTENTION: La date a changé après conversion UTC!")
            print(f"     {birth_date_obj} → {dt_utc.date()}")
        else:
            print(f"  ✅ La date reste la même après conversion UTC")
    except Exception as e:
        print(f"  ❌ Erreur: {e}")
    print()

    # Test: Si le mobile envoie un datetime ISO avec timezone au lieu d'une date
    print("SCÉNARIO POSSIBLE - Mobile envoie datetime ISO avec timezone")
    print("-" * 80)

    # Si le mobile envoie "2001-02-09T23:00:00Z" (minuit en Europe/Paris = 23h UTC la veille)
    test_datetime_strings = [
        "2001-02-09T00:00:00+01:00",  # Minuit Paris (heure d'hiver)
        "2001-02-09T23:00:00Z",        # Minuit Paris en UTC (veille)
        "2001-02-09",                  # Juste la date (correct)
    ]

    for dt_str in test_datetime_strings:
        print(f"  Si mobile envoie: {dt_str}")
        try:
            if "T" in dt_str:
                parsed = datetime.fromisoformat(dt_str.replace("Z", "+00:00"))
                result_date = parsed.date()
            else:
                result_date = date.fromisoformat(dt_str)

            status = "✅" if result_date == date(2001, 2, 9) else "❌"
            print(f"    {status} Résultat: {result_date}")
        except Exception as e:
            print(f"    ❌ Erreur: {e}")
    print()

    # Test: Conversion SQLAlchemy
    print("CONVERSION 4 - SQLAlchemy Date column")
    print("-" * 80)
    print(f"  birth_date = Column(Date, nullable=False)")
    print(f"  Valeur assignée: {birth_date_obj}")
    print(f"  Type: {type(birth_date_obj)}")
    print()
    print(f"  ✅ Devrait être stocké tel quel en base: {birth_date_obj}")
    print()

    print("=" * 80)
    print("DIAGNOSTIC:")
    print("=" * 80)
    print()
    print("Si la date en base est 2001-02-08 au lieu de 2001-02-09:")
    print()
    print("1. Le mobile envoie peut-être un datetime ISO avec timezone")
    print("   → Vérifier le payload JSON dans les logs de l'API")
    print()
    print("2. Il y a peut-être une conversion timezone quelque part")
    print("   → Chercher datetime.astimezone() ou pytz dans le code")
    print()
    print("3. La base PostgreSQL pourrait faire une conversion automatique")
    print("   → Vérifier le type de colonne: DATE (pas TIMESTAMP)")
    print()
    print("4. Le code JavaScript du mobile fait peut-être new Date()")
    print("   → qui convertit en UTC et change la date")
    print()

if __name__ == "__main__":
    test_date_conversion()
