from dotenv import load_dotenv
import os
import sys

# Charge les variables depuis .env
load_dotenv()

def verify_keys():
    """Vérifie la présence des clés API"""
    required_keys = {
        "TAVILY_API_KEY": "https://tavily.com/",
        "OPENWEATHER_API_KEY": "https://openweathermap.org/"
    }
    
    missing = []
    print("\n🔍 Vérification des clés API...")
    for key, url in required_keys.items():
        value = os.getenv(key)
        if not value:
            missing.append((key, url))
            print(f"❌ {key}: NON TROUVÉ")
        else:
            print(f"✅ {key}: PRÉSENT (début: {value[:3]}...)")
    
    if missing:
        print("\n⚠️ ACTIONS REQUISES:")
        for key, url in missing:
            print(f"- Obtenir '{key}' sur {url} et l'ajouter à .env")
        sys.exit(1)  # Quitte avec erreur
    else:
        print("\n🎉 Toutes les clés sont configurées correctement !")

if __name__ == "__main__":
    verify_keys()