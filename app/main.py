import streamlit as st
import emoji
from config import *

from components.about import about_app_tab
from components.sentiment_analysis import sentiment_analysis_tab

# Page configuration
st.set_page_config(
    page_title="ReelFeel Movie Dashboard",
    page_icon=emoji.emojize(":clapper_board:"),
    layout="wide",
    initial_sidebar_state="expanded"    
)

# Loading the style
with open('./app/style.css', 'r') as file:
    style = file.read()

st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)

# session state initialization 
for key, default in {
    'movies': [],
    'current_page': 1,
    'reviews': {},
    'full_analysis': {},
    'last_search_query': ""
}.items():
    if key not in st.session_state:
        st.session_state[key] = default


# Main App
def main():
    st.markdown(f'<h1 class="main-header">{emoji.emojize(":clapper_board:")} Movie Review Analysis Dashboard</h1>', unsafe_allow_html=True)
    
    # two tabs
    tab1, tab2 = st.tabs([
        f"{emoji.emojize(':house:')} How It Works", 
        f"{emoji.emojize(':bar_chart:')} Movie Reviews Sentiment Analysis"
    ])
    
    with tab1:
        try:
            about_app_tab()
        except Exception as e:
            st.error(f"Something went wrong in 'How It Works': {e}")

    with tab2:
        try:
            sentiment_analysis_tab()
        except Exception as e:
            st.error(f"An error occurred during sentiment analysis: {e}")
        
if __name__ == "__main__":
    main()