"""Script pour vérifier les routes disponibles"""
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from routes.natal import router

print("Routes disponibles dans natal router:")
print("=" * 60)
for route in router.routes:
    methods = list(route.methods) if hasattr(route, 'methods') else ['N/A']
    print(f"  {', '.join(methods):10} {route.path}")
print("=" * 60)

# Vérifier spécifiquement le endpoint purge
purge_found = any('/dev/purge' in route.path for route in router.routes)
print(f"\nEndpoint /natal-chart/dev/purge trouvé: {purge_found}")
