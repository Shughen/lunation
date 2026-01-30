"""
Tests pour le filtrage v4 des aspects majeurs
Valide: sextile inclus, orbes variables (8°/10°), exclusion Lilith
"""

import pytest
from services.aspect_explanation_service import (
    filter_major_aspects_v4,
    get_max_orb,
    MAJOR_ASPECT_TYPES,
    MAX_ORB_STANDARD,
    MAX_ORB_LUMINARIES,
)


class TestGetMaxOrb:
    """Tests pour la fonction get_max_orb (orbes variables)"""

    def test_luminaries_sun_returns_10(self):
        """Aspect avec Soleil → 10°"""
        assert get_max_orb('Sun', 'Neptune') == MAX_ORB_LUMINARIES
        assert get_max_orb('sun', 'mars') == MAX_ORB_LUMINARIES

    def test_luminaries_moon_returns_10(self):
        """Aspect avec Lune → 10°"""
        assert get_max_orb('Moon', 'Venus') == MAX_ORB_LUMINARIES
        assert get_max_orb('moon', 'jupiter') == MAX_ORB_LUMINARIES

    def test_both_luminaries_returns_10(self):
        """Aspect Soleil-Lune → 10°"""
        assert get_max_orb('Sun', 'Moon') == MAX_ORB_LUMINARIES
        assert get_max_orb('moon', 'sun') == MAX_ORB_LUMINARIES

    def test_no_luminaries_returns_8(self):
        """Aspect sans luminaires → 8°"""
        assert get_max_orb('Mars', 'Neptune') == MAX_ORB_STANDARD
        assert get_max_orb('mercury', 'venus') == MAX_ORB_STANDARD
        assert get_max_orb('Saturn', 'Uranus') == MAX_ORB_STANDARD


class TestFilterMajorAspectsV4:
    """Tests pour filter_major_aspects_v4"""

    @pytest.fixture
    def mock_aspects(self):
        """Jeu de données de test avec tous les cas"""
        return [
            # ✅ Aspects majeurs valides
            {'planet1': 'Sun', 'planet2': 'Moon', 'type': 'conjunction', 'orb': 2.5},  # Luminaires
            {'planet1': 'Mercury', 'planet2': 'Venus', 'type': 'sextile', 'orb': 1.0},  # Sextile < 8°
            {'planet1': 'Mars', 'planet2': 'Jupiter', 'type': 'trine', 'orb': 4.5},  # < 8°
            {'planet1': 'Saturn', 'planet2': 'Uranus', 'type': 'square', 'orb': 7.0},  # < 8°
            {'planet1': 'Neptune', 'planet2': 'Pluto', 'type': 'opposition', 'orb': 5.8},  # < 8°
            {'planet1': 'Moon', 'planet2': 'Chiron', 'type': 'trine', 'orb': 6.0},  # Luminaire < 10°
            {'planet1': 'Sun', 'planet2': 'Neptune', 'type': 'trine', 'orb': 9.5},  # Luminaire < 10°

            # ❌ Aspects à exclure
            {'planet1': 'mean_lilith', 'planet2': 'Sun', 'type': 'conjunction', 'orb': 3.0},  # Lilith
            {'planet1': 'Venus', 'planet2': 'Mars', 'type': 'quincunx', 'orb': 2.0},  # Type mineur
            {'planet1': 'Mars', 'planet2': 'Neptune', 'type': 'trine', 'orb': 9.5},  # > 8° sans luminaire
            {'planet1': 'Saturn', 'planet2': 'Uranus', 'type': 'square', 'orb': 8.5},  # > 8°
        ]

    def test_includes_sextile(self, mock_aspects):
        """Sextile est inclus dans les aspects majeurs"""
        assert 'sextile' in MAJOR_ASPECT_TYPES

        filtered = filter_major_aspects_v4(mock_aspects)
        sextile_aspects = [a for a in filtered if a['type'] == 'sextile']
        assert len(sextile_aspects) == 1
        assert sextile_aspects[0]['planet1'] == 'Mercury'

    def test_filters_major_types_only(self, mock_aspects):
        """Filtre uniquement les 5 types majeurs"""
        filtered = filter_major_aspects_v4(mock_aspects)

        for aspect in filtered:
            assert aspect['type'].lower() in MAJOR_ASPECT_TYPES

    def test_excludes_lilith(self, mock_aspects):
        """Exclut tous les aspects impliquant Lilith"""
        filtered = filter_major_aspects_v4(mock_aspects)

        for aspect in filtered:
            planet1 = aspect['planet1'].lower().replace('_', '').replace(' ', '').replace('-', '')
            planet2 = aspect['planet2'].lower().replace('_', '').replace(' ', '').replace('-', '')
            assert 'lilith' not in planet1
            assert 'lilith' not in planet2

    def test_applies_10_deg_orb_for_luminaries(self, mock_aspects):
        """Applique orbe 10° pour aspects avec Soleil ou Lune"""
        filtered = filter_major_aspects_v4(mock_aspects)

        # Sun-Neptune trine (9.5°) doit être inclus
        sun_neptune = next((a for a in filtered
                           if (a['planet1'] == 'Sun' and a['planet2'] == 'Neptune')
                           or (a['planet1'] == 'Neptune' and a['planet2'] == 'Sun')), None)
        assert sun_neptune is not None
        assert abs(sun_neptune['orb']) == 9.5

    def test_applies_8_deg_orb_for_non_luminaries(self, mock_aspects):
        """Applique orbe 8° pour aspects sans luminaires"""
        filtered = filter_major_aspects_v4(mock_aspects)

        # Mars-Neptune trine (9.5°) doit être exclu (> 8°)
        mars_neptune = next((a for a in filtered
                            if (a['planet1'] == 'Mars' and a['planet2'] == 'Neptune')
                            or (a['planet1'] == 'Neptune' and a['planet2'] == 'Mars')), None)
        assert mars_neptune is None

    def test_sorts_by_type_then_orb_astrotheme_style(self, mock_aspects):
        """Trie comme Astrotheme: par type d'abord, puis par orbe au sein de chaque type"""
        filtered = filter_major_aspects_v4(mock_aspects)

        # Vérifier que les aspects sont groupés par type
        types_order = [a['type'] for a in filtered]

        # Vérifier que les conjonctions viennent avant les oppositions
        if 'conjunction' in types_order and 'opposition' in types_order:
            conj_index = types_order.index('conjunction')
            opp_index = types_order.index('opposition')
            assert conj_index < opp_index, "Conjonctions doivent venir avant oppositions"

        # Vérifier que les oppositions viennent avant les carrés
        if 'opposition' in types_order and 'square' in types_order:
            opp_index = types_order.index('opposition')
            square_index = types_order.index('square')
            assert opp_index < square_index, "Oppositions doivent venir avant carrés"

        # Vérifier que les carrés viennent avant les trigones
        if 'square' in types_order and 'trine' in types_order:
            square_index = types_order.index('square')
            trine_index = types_order.index('trine')
            assert square_index < trine_index, "Carrés doivent venir avant trigones"

        # Vérifier que les trigones viennent avant les sextiles
        if 'trine' in types_order and 'sextile' in types_order:
            trine_index = types_order.index('trine')
            sextile_index = types_order.index('sextile')
            assert trine_index < sextile_index, "Trigones doivent venir avant sextiles"

        # Vérifier que au sein de chaque type, les aspects sont triés par orbe
        from itertools import groupby
        for aspect_type, group in groupby(filtered, key=lambda a: a['type']):
            group_list = list(group)
            orbs = [abs(a['orb']) for a in group_list]
            assert orbs == sorted(orbs), f"Orbes dans {aspect_type} pas triés: {orbs}"

    def test_returns_7_valid_aspects(self, mock_aspects):
        """Retourne les 7 aspects valides du jeu de test"""
        filtered = filter_major_aspects_v4(mock_aspects)

        # Attendus:
        # 1. Mercury-Venus sextile (1.0°)
        # 2. Sun-Moon conjunction (2.5°)
        # 3. Mars-Jupiter trine (4.5°)
        # 4. Neptune-Pluto opposition (5.8°)
        # 5. Moon-Chiron trine (6.0°)
        # 6. Saturn-Uranus square (7.0°)
        # 7. Sun-Neptune trine (9.5°)
        assert len(filtered) == 7

    def test_handles_empty_list(self):
        """Gère correctement une liste vide"""
        filtered = filter_major_aspects_v4([])
        assert filtered == []

    def test_handles_negative_orbs(self):
        """Gère correctement les orbes négatifs (valeur absolue)"""
        aspects = [
            {'planet1': 'Sun', 'planet2': 'Moon', 'type': 'conjunction', 'orb': -3.5}
        ]
        filtered = filter_major_aspects_v4(aspects)

        assert len(filtered) == 1
        assert abs(filtered[0]['orb']) == 3.5
