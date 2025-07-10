import streamlit as st

def about_app_tab():
    st.markdown("## Welcome to the Movie Review Analysis Dashboard")

    # Overview
    st.markdown("""
    ### **Overview**
    The Movie Analysis Dashboard is an interactive tool to search movies, fetch audience reviews, and analyze them with visual plots.
    Quickly find any movie, view its details, and gain insights from real user reviews using sentiment analysis and intuitive visualizations.
    """)

    # Key Features
    st.markdown("### Key Features")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **Movie Search & Discovery**
        - Search movies by title  
        - Browse results with pagination  
        - Switch between movie selections easily  
        - View detailed movie profiles  
        """)

        st.markdown("""
        **Review Analysis**
        - Automatically fetch real reviews  
        - AI-based sentiment prediction  
        - Numerical scoring and ratings  
        - Multi-dimensional analysis  
        """)

    with col2:
        st.markdown("""
        **Movie Information**
        - Plot summaries  
        - Cast, crew, and genre info  
        - Ratings and release details  
        """)

        st.markdown("""
        **Visual Insights**
        - Interactive sentiment graphs  
        - Review trends over time  
        - Score distribution charts  
        """)

    # How It Works
    st.markdown("""
        ### How It Works
        1. **Search:** "Enter a movie title in the search bar.,
        2. **Browse:** "Use pagination to navigate results.,
        3. **Select:** "Click a movie to view details.,
        4. **Analyze:** "Click 'Perform Analysis' to begin.,
        5. **Explore:** "Review sentiment scores and visual reports.
        """)
    steps = [
        
    ]
    for step, description in steps:
        st.markdown(f"- **{step}**: {description}")

    # Technology Stack
    st.markdown("### Technology Stack")
    tech_col1, tech_col2, tech_col3 = st.columns(3)

    with tech_col1:
        st.markdown("""
        **Frontend**
        - Streamlit  
        - Python  
        - Interactive UI Components  
        """)

    with tech_col2:
        st.markdown("""
        **Data Processing**
        - Pandas  
        - NumPy  
        - Plotly / Matplotlib  
        """)

    with tech_col3:
        st.markdown("""
        **AI/ML**
        - NLP-Tools
        - Predictive scoring using RNN Model  
        - Tensorflow 
        """)

    # Analysis Capabilities
    st.markdown("""
        ### Analysis Capabilities
        - Sentiment classification: Positive, Negative, Neutral,
        - Review-based score prediction,
        - Emotion and tone detection,
        - Trends over time from reviews,
        - Rating and sentiment distribution charts,
        - Frequent keywords and themes
        """)
    # analysis_features = [
        
    # ]
    # for feature in analysis_features:
    #     st.markdown(f"- {feature}")

    # Sample Workflow
    st.markdown("### Sample Workflow")
    st.markdown("""
    **Example:**  
    1. Search for "The Dark Knight"  
    2. Select the 2008 version  
    3. Review plot, cast, and ratings  
    4. Click **Perform Analysis**  
    5. Explore sentiment and visual data  
    """)

    # Audience
    st.markdown("### Who Can Benefit?")
    benefits_col1, benefits_col2 = st.columns(2)

    with benefits_col1:
        st.markdown("""
        **Movie Enthusiasts**
        - Access rich movie data  
        - Understand public sentiment  
        - Make informed watchlist decisions  
        """)

    with benefits_col2:
        st.markdown("""
        **Data Analysts**
        - Analyze structured review data  
        - Visualize audience feedback  
        - Extract actionable insights  
        """)

    # Getting Started
    st.markdown("### Get Started")
    st.success("""
    Go to the **Movie Search** tab to begin.  
    Enter any movie title to explore its details and perform AI-driven analysis.
    """)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #888; font-size: 0.9em;'>
        Built with Streamlit and advanced NLP technologies.
    </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    about_app_tab()
