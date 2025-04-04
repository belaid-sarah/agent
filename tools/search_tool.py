from tavily import TavilyClient
from dotenv import load_dotenv
import os
import logging
from typing import Dict

# Configuration du logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

def search_online(query: str) -> str:
    """Version corrigée sans self"""
    try:
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            logger.error("Clé API Tavily manquante dans .env")
            raise ValueError("Configuration manquante")

        client = TavilyClient(api_key=api_key)
        response = client.search(
            query=query,
            search_depth="basic",
            include_answer=True,
            max_results=3
        )
        return _format_response(response)  # Appel sans self
    except Exception as e:
        logger.error(f"Erreur recherche: {str(e)}")
        return _search_fallback(query)  # Appel sans self

def _format_response(response: Dict) -> str:
    """Fonction helper autonome"""
    if answer := response.get("answer"):
        return f"🔍 Réponse directe:\n{answer}"
    return "\n".join(f"• {r['title']}: {r['content'][:100]}..." for r in response.get("results", []))

def _search_fallback(query: str) -> str:
    """Fonction de repli autonome"""
    return f"⚠ Recherche limitée\nℹ Essayez: https://www.google.com/search?q={query.replace(' ', '+')}"