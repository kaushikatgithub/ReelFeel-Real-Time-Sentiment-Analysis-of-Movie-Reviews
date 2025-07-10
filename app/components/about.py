import streamlit as st

def about_app_tab():
    st.markdown("## 🎯 Welcome to the Movie Analysis Dashboard!")
    
    # App overview
    st.markdown("""
    ### 🎬 **Overview**
    The Movie Analysis Dashboard is an AI-powered tool that lets you explore movies and dive into audience reviews through advanced sentiment analysis.
    
    Search any movie, view detailed info, and unlock meaningful insights from real user feedback.
    """)

    # Key features section
    st.markdown("### ✨ **Key Features**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🔍 Movie Search & Discovery**
        - Search movies by title  
        - Paginated search results  
        - Seamless switching between movies  
        - Detailed movie view  
        """)
        
        st.markdown("""
        **📊 Review Analysis**
        - Auto-fetch real reviews  
        - AI sentiment prediction  
        - Review scoring system  
        - Multiple analysis dimensions  
        """)
    
    with col2:
        st.markdown("""
        **🎯 Movie Details**
        - Plot summaries  
        - Cast and crew  
        - Genre & ratings  
        - Release information  
        """)
        
        st.markdown("""
        **📈 Visual Insights**
        - Interactive graphs  
        - Sentiment distribution  
        - Review patterns over time  
        - Score visualizations  
        """)

    # How it works section
    st.markdown("### 🚀 **How It Works**")
    
    steps = [
        ("1️⃣ **Search**", "Type a movie name in the search bar."),
        ("2️⃣ **Browse**", "Use pagination to view matching results."),
        ("3️⃣ **Select**", "Click on a movie to explore its details."),
        ("4️⃣ **Analyze**", "Click 'Perform Analysis' to start."),
        ("5️⃣ **Explore**", "View sentiment stats, scores, and patterns.")
    ]
    
    for step, description in steps:
        st.markdown(f"- {step}: {description}")
    
    # Technology stack
    st.markdown("### 🛠️ **Technology Stack**")
    
    tech_col1, tech_col2, tech_col3 = st.columns(3)
    
    with tech_col1:
        st.markdown("""
        **Frontend**
        - Streamlit  
        - Python  
        - Interactive UI  
        """)
    
    with tech_col2:
        st.markdown("""
        **Data Processing**
        - Pandas  
        - NumPy  
        - Matplotlib/Plotly  
        """)
    
    with tech_col3:
        st.markdown("""
        **AI/ML**
        - NLP models  
        - Sentiment analysis  
        - Predictive scoring  
        """)
    
    # Analysis capabilities
    st.markdown("### 📊 **What You Can Analyze**")
    
    analysis_features = [
        "Sentiment Classification (Positive, Negative, Neutral)",
        "Score Prediction based on reviews",
        "Emotion & Tone Analysis",
        "Review Trends over Time",
        "Rating Distribution Charts",
        "Keyword & Theme Extraction"
    ]
    
    for feature in analysis_features:
        st.markdown(f"- {feature}")
    
    # Sample workflow
    st.markdown("### 🧪 **Sample Workflow**")
    
    st.info("""
    **Example:**  
    1. Search for `"The Dark Knight"`  
    2. Select the 2008 version from results  
    3. View plot, cast, and ratings  
    4. Click **Perform Analysis**  
    5. Explore sentiment charts and insights  
    """)

    # Benefits section
    st.markdown("### 🎯 **Who Is It For?**")
    
    benefits_col1, benefits_col2 = st.columns(2)
    
    with benefits_col1:
        st.markdown("""
        **🎥 Movie Lovers**
        - Discover rich movie information  
        - Understand public opinions  
        - Decide what to watch next  
        - Explore trends in storytelling  
        """)
    
    with benefits_col2:
        st.markdown("""
        **📊 Data Enthusiasts**
        - Work with structured review data  
        - Analyze sentiment patterns  
        - Visualize audience response  
        - Export insights for reports  
        """)
    
    # Getting started
    st.markdown("### 🚀 **Get Started**")
    
    st.success("""
    Head over to the **Movie Search** tab and start exploring!  
    Enter a movie title to begin your sentiment journey 🎬
    """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.9em;'>
        Built with ❤️ using Streamlit & AI-powered NLP models
    </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    about_app_tab()