# test_tools.py
from dotenv import load_dotenv
from tools.search_tool import search_online
from tools.weather_tool import get_weather

load_dotenv()  # Charge les clés API

def tester_outils():
    print("\n🔍 Test des outils indépendamment:")
    
    # Test recherche
    print("\n1. Test recherche web:")
    query_recherche = "Qui est le maire de Lyon ?"
    print(f"Requête: '{query_recherche}'")
    print("Résultat:", search_online(query_recherche))
    
    # Test météo
    print("\n2. Test météo:")
    query_meteo = "Paris"
    print(f"Requête: '{query_meteo}'")
    print("Résultat:", get_weather(query_meteo))

if __name__ == "__main__":
    tester_outils()