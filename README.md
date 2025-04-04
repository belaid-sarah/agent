# Search Agent

## 📌 Description
Search Agent est une application permettant d'exécuter des recherches spécifiques en utilisant Streamlit et Docker. Cette application est contenue dans un conteneur Docker pour faciliter son déploiement et son exécution. Elle intègre des modèles de recherche comme Llama et Ollama, offrant une interface simple pour interagir avec ces outils.

## 🚀 Fonctionnalités
- **Interface utilisateur avec Streamlit** : L'interface est développée avec Streamlit pour une expérience fluide et interactive.
- **Containerisation avec Docker** : L'application est contenue dans un conteneur Docker pour faciliter le déploiement sur n'importe quelle machine sans dépendances supplémentaires.
- **Intégration avec Llama et Ollama** : Le projet utilise des modèles Llama et Ollama pour effectuer des recherches avancées sur les données.

### 🌦️ **Weather Tool** 
- **API Utilisée** : WeatherAPI
- **Fonctionnalités** :
  - Récupération en temps réel des données météo
  - Support multi-villes (Paris, Lyon, Marseille...)
  - Affichage des données claires :
    - Température (°C)
    - Conditions atmosphériques
    - Vitesse du vent
  - Gestion d'erreur robuste avec fallback manuel

### 🔍 **Search Tool** 
- **API Utilisée** : Tavily Search API
- **Fonctionnalités** :
  - Recherche web avancée
  - Extraction des 3 premiers résultats pertinents
  - Filtrage intelligent des sources touristiques
  - Cache des requêtes pour performance
  - Fallback vers Google Search si échec

### 🧠 **Moteur d'Intelligence Artificielle**
- **Technologies** :
  - **LangChain** : Orchestration des composants AI
  - **LangGraph** : Gestion des workflows complexes
  - **Ollama** : Hébergement local des modèles LLM

- **Modèles Utilisés** :
  - `llama3` (8B paramètres) - Modèle principal
  - `mistral` (7B paramètres) - Alternative légère
  - `french-llama` - Optimisé pour le français

- **Fonctionnalités AI** :
  - Analyse sémantique des requêtes
  - Fusion intelligente des résultats (météo + web)
  - Génération de réponses naturelles en français
  - Système de fallback contextuel

### 🖥️ **Interface Utilisateur**
- Framework : **Streamlit**
- Fonctionnalités :
  - Saisie de requête naturelle
  - Affichage contextuel des résultats
  - Indicateurs visuels de statut
  - Adaptatif mobile/desktop
  - Temps de réponse visible

### 🐳 **Infrastructure**
- Containerisation via **Docker**
- Gestion des dépendances :
  - Isolation des environnements
  - Déploiement simplifié
  - Configuration via variables d'environnement

## 🛠 Installation et utilisation

### 1️⃣ **Cloner le projet**
```sh
git clone https://github.com/belaid-sarah/agent.git
cd nom-du-repo

## 🦙 Commandes Ollama

### Télécharger les modèles :
```bash
ollama pull llama3     # Modèle principal (7B paramètres)
ollama pull mistral    # Modèle alternatif (7B paramètres)

ollama serve           # Lancer en premier plan

streamlit run app.py     #run the app
