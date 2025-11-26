"""
Client Supabase pour interagir avec les tables via l'API REST
Utilisé pour lunar_returns qui est dans Supabase directement
"""

from supabase import create_client, Client
from config import settings
import logging

logger = logging.getLogger(__name__)

# Client Supabase (singleton)
_supabase_client: Client = None


def get_supabase_client() -> Client:
    """Retourne le client Supabase (singleton)"""
    global _supabase_client
    
    if _supabase_client is None:
        supabase_url = settings.SUPABASE_URL
        supabase_key = settings.SUPABASE_ANON_KEY
        
        if not supabase_url or not supabase_key:
            logger.warning("⚠️ SUPABASE_URL ou SUPABASE_ANON_KEY non configurés dans .env")
            logger.warning("   Les appels à Supabase vont échouer")
            logger.warning("   Ajoutez SUPABASE_URL et SUPABASE_ANON_KEY dans votre .env")
        
        _supabase_client = create_client(supabase_url, supabase_key)
        logger.info("✅ Client Supabase initialisé")
    
    return _supabase_client

