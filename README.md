# Search Agent

## 📌 Description
Search Agent est une application permettant d'exécuter des recherches spécifiques en utilisant Streamlit et Docker. Cette application est contenue dans un conteneur Docker pour faciliter son déploiement et son exécution. Elle intègre des modèles de recherche comme Llama et Ollama, offrant une interface simple pour interagir avec ces outils.

## 🚀 Fonctionnalités
- **Interface utilisateur avec Streamlit** : L'interface est développée avec Streamlit pour une expérience fluide et interactive.
- **Containerisation avec Docker** : L'application est contenue dans un conteneur Docker pour faciliter le déploiement sur n'importe quelle machine sans dépendances supplémentaires.
- **Intégration avec Llama et Ollama** : Le projet utilise des modèles Llama et Ollama pour effectuer des recherches avancées sur les données.

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
