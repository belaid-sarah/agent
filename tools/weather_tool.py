import requests
from dotenv import load_dotenv
import os
import logging

# Initialisation du logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

def get_weather(city: str) -> str:
    """Version corrigée avec logger défini"""
    try:
        api_key = os.getenv("WEATHERAPI_KEY")
        if not api_key:
            logger.error("Clé API WEATHER manquante dans .env")
            raise ValueError("Clé API manquante")
        
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&lang=fr"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        current = data["current"]
        
        return (
            f"{current['temp_c']}°C, "
            f"{current['condition']['text']}, "
            f"vent {current['wind_kph']} km/h"
        )
    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur API météo: {str(e)}")
        return "Service météo indisponible"
    except Exception as e:
        logger.error(f"Erreur inattendue: {str(e)}")
        return "Données météo non disponibles"