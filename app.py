import streamlit as st
from agents.main_agent import UniversalSearchAgent
import time

st.set_page_config(
    page_title="🔍 Assistant Intelligent",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_resource(ttl=3600)
def load_agent():
    return UniversalSearchAgent()

def display_response(query: str, response: str, delay: float):
    """Affichage contextuel"""
    if "météo" in query.lower():
        st.info(f"## 🌤️ Météo\n{response}\n\n*(Traitement en {delay:.2f}s)*")
    else:
        st.success(f"## 📚 Réponse\n{response}\n\n*(Traitement en {delay:.2f}s)*")

def main():
    st.title("🔍 Assistant de Recherche Universel")
    st.markdown("Posez des questions sur n'importe quel sujet")
    
    agent = load_agent()
    query = st.text_input("Votre question:", key="query_input")
    
    if st.button("Rechercher", type="primary") or query:
        if not query.strip():
            st.warning("Veuillez saisir une question valide")
            return
            
        with st.spinner("Recherche en cours..."):
            start = time.time()
            response = agent.run(query)
            delay = time.time() - start
            
            if response:
                display_response(query, response, delay)
            else:
                st.error("Aucune réponse n'a pu être générée")

if __name__ == "__main__":
    main()