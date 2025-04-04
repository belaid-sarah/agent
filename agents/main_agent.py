from langgraph.graph import Graph, END
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from typing import Dict, Any, List
import re
import logging
from tools.search_tool import search_online
from tools.weather_tool import get_weather

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UniversalSearchAgent:
    def __init__(self):
        try:
            self.llm = Ollama(model="llama3")
            self.workflow = Graph()
            self._setup_workflow()
            self.app = self.workflow.compile()
            logger.info("Agent initialisé avec succès")
        except Exception as e:
            logger.error(f"Erreur initialisation: {str(e)}")
            raise

    def _setup_workflow(self):
        """Workflow optimisé avec gestion claire des flux"""
        self.workflow.add_node("analyze", self._analyze_query)  # Corrigé: _analyze_query au lieu de _analyze_query
        self.workflow.add_node("search", self._execute_search)
        self.workflow.add_node("weather", self._execute_weather)
        self.workflow.add_node("respond", self._generate_response)

        self.workflow.set_entry_point("analyze")

        # Routage intelligent
        self.workflow.add_conditional_edges(
            "analyze",
            self._route_query,
            {
                "search": "search",
                "weather": "weather",
                "both": "search"  # On traite d'abord la recherche
            }
        )
        
        # Connexions conditionnelles
        self.workflow.add_conditional_edges(
            "search",
            lambda state: "weather" if state.get("needs_weather", False) else "respond",  # Ajout d'une valeur par défaut
        )
        
        self.workflow.add_edge("weather", "respond")
        self.workflow.add_edge("respond", END)

    def _route_query(self, state: Dict[str, Any]) -> str:
        """Décision de routage améliorée"""
        try:
            if state.get("error"):
                return "search"
                
            if state.get("needs_weather", False) and state.get("needs_search", False):
                return "both"
            elif state.get("needs_weather", False):
                return "weather"
            return "search"
        except Exception as e:
            logger.error(f"Erreur routage: {str(e)}")
            return "search"

    def _analyze_query(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Analyse plus robuste"""
        try:
            query = state["query"].lower()
            is_weather_only = all(kw in query for kw in ["météo", "temps"]) and not any(kw in query for kw in ["visiter", "monument"])
            return {
                "original_query": state["query"],
                "needs_search": not is_weather_only,
                "needs_weather": self._needs_weather_check(query),
                "cities": self._extract_cities(query),
                "error": None
            }
        except Exception as e:
            logger.error(f"Erreur analyse: {str(e)}")
            return {"error": str(e)}

    def _execute_search(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Exécute la recherche via Tavily"""
        try:
            query = state["original_query"]
            results = search_online(query)
            return {
                "search_results": results or "Aucun résultat trouvé",
                **state
            }
        except Exception as e:
            logger.error(f"Erreur recherche: {str(e)}")
            return {
                "search_results": self._get_search_fallback(state),
                **state
            }

    def _execute_weather(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Récupère les données météo"""
        try:
            cities = state.get("cities", ["Paris"])
            weather = get_weather(cities[0])
            return {
                "weather_data": weather,
                **state
            }
        except Exception as e:
            logger.error(f"Erreur météo: {str(e)}")
            return {
                "weather_data": "Données météo indisponibles",
                **state
            }

    def _generate_response(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Génère la réponse finale"""
        try:
            prompt_template = """
            Répondez à cette question en français:

            Question: {question}

            {context}

            Règles:
            1. Soyez concis et précis
            2. Structurez la réponse
            3. Utilisez uniquement les infos fournies
            """
            
            context = []
            if state.get("search_results"):
                context.append(f"Résultats de recherche:\n{state['search_results']}")
            if state.get("weather_data"):
                context.append(f"Météo:\n{state['weather_data']}")
            
            prompt = ChatPromptTemplate.from_template(prompt_template)
            chain = prompt | self.llm
            response = chain.invoke({
                "question": state["original_query"],
                "context": "\n\n".join(context) or "Aucune information trouvée"
            })
            
            return {
                "result": response.content if hasattr(response, 'content') else str(response),
                **state
            }
        except Exception as e:
            logger.error(f"Erreur génération: {str(e)}")
            return {
                "result": "Données brutes:\n" + "\n".join(filter(None, [
                    state.get("search_results", ""),
                    state.get("weather_data", "")
                ])),
                **state
            }

    def _needs_weather_check(self, query: str) -> bool:
        weather_kws = ["météo", "température", "temps", "pluie", "soleil"]
        return any(kw in query for kw in weather_kws)

    def _extract_cities(self, query: str) -> List[str]:
        matches = re.findall(r'(?:à|a|au|en|sur|pour|de)\s+([\w\s-]+)', query, re.IGNORECASE)
        return [m.strip().title() for m in matches if len(m.strip()) > 2]

    def _get_search_fallback(self, state: Dict[str, Any]) -> str:
        """Fallback contextuel"""
        query = state["original_query"].lower()
        if "maire" in query:
            return "Consultez le site officiel de la ville"
        return "Je n'ai pas trouvé de réponse précise"

    def run(self, query: str) -> str:
        """Version améliorée avec fallback météo"""
        try:
            result = self.app.invoke({"query": query})
            
            # Fallback spécifique pour les requêtes météo
            if "météo" in query.lower() and "indisponible" in result.get("result", ""):
                cities = self._extract_cities(query)
                city = cities[0] if cities else "Paris"
                return f"🌤 Météo manuelle pour {city} : Consultez https://www.meteo-paris.com/"
                
            return result.get("result", "Aucune réponse disponible")
        except Exception as e:
            logger.error(f"Erreur critique : {str(e)}")
            return "Service temporairement indisponible"