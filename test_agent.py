from agents.main_agent import MainAgent

def test_agent():
    agent = MainAgent()
    tests = [
        ("Qui est le maire de Lyon ?", "Recherche simple"),
        ("Météo à Paris et monuments", "Combinaison"),
        ("Température à Marseille", "Météo simple")
    ]
    
    for query, description in tests:
        print(f"\n=== {description} ===")
        print(f"Entrée: {query}")
        print("Sortie:", agent.run(query))

if __name__ == "__main__":
    test_agent()