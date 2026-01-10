"""
API ML - Prédiction compatibilité Parent-Enfant
Utilise le modèle XGBoost optimisé (98.19% ROC-AUC)
"""
from http.server import BaseHTTPRequestHandler
import json
import os
import sys

# Ajouter le path pour imports locaux
sys.path.insert(0, os.path.dirname(__file__))

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # CORS
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()

            # Lire le body
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body.decode('utf-8'))

            # Import du modèle (lazy loading)
            import joblib
            import numpy as np
            
            # Charger le modèle
            model_path = os.path.join(os.path.dirname(__file__), 'xgb_best.pkl')
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Modèle non trouvé: {model_path}")
            
            model = joblib.load(model_path)

            # Extraire les features depuis la requête
            features = self._extract_features(data)
            
            # Prédiction
            prediction = model.predict([features])[0]
            probability = model.predict_proba([features])[0]
            
            # Score de compatibilité (0-100)
            compatibility_score = int(probability[1] * 100)
            
            # Générer recommandations
            recommendations = self._generate_recommendations(
                compatibility_score, 
                data
            )

            result = {
                "success": True,
                "prediction": int(prediction),
                "compatibility_score": compatibility_score,
                "probability": {
                    "difficile": round(float(probability[0]), 4),
                    "harmonieuse": round(float(probability[1]), 4)
                },
                "interpretation": self._interpret_score(compatibility_score),
                "recommendations": recommendations,
                "model_accuracy": 98.19
            }

            self.wfile.write(json.dumps(result).encode())

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = {
                "success": False,
                "error": str(e)
            }
            self.wfile.write(json.dumps(error_response).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def _extract_features(self, data):
        """Extrait les 20 features depuis les données reçues"""
        parent = data.get('parent', {})
        enfant = data.get('enfant', {})
        
        features = [
            parent.get('sun_sign', 1),
            parent.get('moon_sign', 1),
            parent.get('ascendant', 1),
            parent.get('mercury', 1),
            parent.get('venus', 1),
            parent.get('mars', 1),
            enfant.get('sun_sign', 1),
            enfant.get('moon_sign', 1),
            enfant.get('ascendant', 1),
            enfant.get('mercury', 1),
            enfant.get('venus', 1),
            enfant.get('mars', 1),
            data.get('age_diff', 25),
            data.get('house_overlap', 0.5),
            self._calculate_element_compatibility(parent, enfant),
            self._calculate_aspect_score(parent, enfant),
            data.get('moon_phase_birth', 0.5),
            self._get_dominant_element(parent),
            self._get_dominant_element(enfant),
            data.get('karmic_nodes', 0.0)
        ]
        
        return features

    def _calculate_element_compatibility(self, parent, enfant):
        """Calcule compatibilité élémentaire (Feu/Terre/Air/Eau)"""
        elements = {
            1: 1, 5: 1, 9: 1,   # Feu: Bélier, Lion, Sagittaire
            2: 2, 6: 2, 10: 2,  # Terre: Taureau, Vierge, Capricorne
            3: 3, 7: 3, 11: 3,  # Air: Gémeaux, Balance, Verseau
            4: 4, 8: 4, 12: 4   # Eau: Cancer, Scorpion, Poissons
        }
        
        parent_elem = elements.get(parent.get('sun_sign', 1), 1)
        enfant_elem = elements.get(enfant.get('sun_sign', 1), 1)
        
        # Compatibilité: même élément ou éléments compatibles
        if parent_elem == enfant_elem:
            return 0.9
        elif (parent_elem in [1, 3] and enfant_elem in [1, 3]) or \
             (parent_elem in [2, 4] and enfant_elem in [2, 4]):
            return 0.7
        else:
            return 0.4

    def _calculate_aspect_score(self, parent, enfant):
        """Calcule score des aspects astrologiques"""
        parent_sun = parent.get('sun_sign', 1)
        enfant_sun = enfant.get('sun_sign', 1)
        
        diff = abs(parent_sun - enfant_sun)
        
        # Trigone (4 signes) = harmonieux
        if diff in [4, 8]:
            return 0.8
        # Sextile (2 signes) = favorable
        elif diff in [2, 10]:
            return 0.6
        # Opposition (6 signes) = tension
        elif diff == 6:
            return -0.5
        # Carré (3 signes) = défi
        elif diff in [3, 9]:
            return -0.3
        else:
            return 0.0

    def _get_dominant_element(self, person):
        """Détermine l'élément dominant"""
        signs = [
            person.get('sun_sign', 1),
            person.get('moon_sign', 1),
            person.get('ascendant', 1)
        ]
        
        elements = {1: 0, 2: 0, 3: 0, 4: 0}  # Feu, Terre, Air, Eau
        
        for sign in signs:
            if sign in [1, 5, 9]:
                elements[1] += 1
            elif sign in [2, 6, 10]:
                elements[2] += 1
            elif sign in [3, 7, 11]:
                elements[3] += 1
            elif sign in [4, 8, 12]:
                elements[4] += 1
        
        return max(elements, key=elements.get)

    def _interpret_score(self, score):
        """Interprète le score de compatibilité"""
        if score >= 85:
            return {
                "level": "Excellente",
                "emoji": "💚",
                "title": "Relation très harmonieuse",
                "description": "Votre relation parent-enfant présente d'excellentes bases astrologiques. Les énergies sont très compatibles et favorisent une communication fluide."
            }
        elif score >= 70:
            return {
                "level": "Bonne",
                "emoji": "💙",
                "title": "Relation harmonieuse",
                "description": "Belle compatibilité astrologique. Quelques ajustements peuvent renforcer encore plus votre complicité."
            }
        elif score >= 55:
            return {
                "level": "Moyenne",
                "emoji": "💛",
                "title": "Relation équilibrée",
                "description": "Compatibilité correcte avec des défis à surmonter. La compréhension mutuelle demande des efforts conscients."
            }
        else:
            return {
                "level": "Délicate",
                "emoji": "🧡",
                "title": "Relation à travailler",
                "description": "Les énergies astrologiques sont contrastées. Une attention particulière à la communication est recommandée."
            }

    def _generate_recommendations(self, score, data):
        """Génère des recommandations personnalisées"""
        recommendations = []
        
        parent = data.get('parent', {})
        enfant = data.get('enfant', {})
        
        # Recommandations basées sur le score
        if score >= 70:
            recommendations.append({
                "type": "strength",
                "icon": "✨",
                "text": "Cultivez votre complicité naturelle à travers des activités partagées."
            })
        else:
            recommendations.append({
                "type": "improvement",
                "icon": "🔧",
                "text": "Accordez une attention particulière à l'écoute active et à la validation des émotions."
            })
        
        # Recommandations basées sur les éléments
        elem_compat = self._calculate_element_compatibility(parent, enfant)
        if elem_compat < 0.6:
            recommendations.append({
                "type": "advice",
                "icon": "🌊",
                "text": "Vos éléments astrologiques diffèrent : prenez le temps de comprendre vos modes de fonctionnement respectifs."
            })
        
        # Recommandation générale
        recommendations.append({
            "type": "general",
            "icon": "💫",
            "text": "L'astrologie éclaire, mais l'amour et la communication construisent les vraies relations."
        })
        
        return recommendations

