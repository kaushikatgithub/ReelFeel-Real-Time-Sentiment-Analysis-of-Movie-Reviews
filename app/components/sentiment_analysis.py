import streamlit as st
import pandas as pd
import emoji

from config import *
from utils.movie_api import fetch_movie_data
from components.review_card import display_review_card
from components.movie_card import display_movie_card
from utils.review_scrapper import get_reviews
from utils.predict_sentiment import predict
from components.analysis_plots import sentiment_distribution_plots
from components.analysis_plots import sentiment_score_analysis_plots
from components.analysis_plots import sentiment_vs_score_plots
from components.analysis_plots import content_analysis_plots
from components.analysis_plots import summary_statistics

# For Testing
# Initialize session state
# if 'movies' not in st.session_state:
#     st.session_state.movies = []
# if 'current_page' not in st.session_state:
#     st.session_state.current_page = 1
# if 'reviews' not in st.session_state:
#     st.session_state.reviews = {}
# if 'full_analysis' not in st.session_state:
#     st.session_state.full_analysis = {}

def display_review_analysis(reviews: list):

    # type check
    if not isinstance(reviews, list) or not reviews:
        st.warning("No valid reviews available to analyze.")
        return

    try:
        df = pd.DataFrame(reviews)
    except Exception as e:
        st.error(f"Error converting reviews to DataFrame: {e}")
        return

    # check for presence of columns
    required_cols = ['title', 'content', 'sentiment', 'score']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        st.error(f"Missing required column(s): {', '.join(missing_cols)}")
        return

    # sentiment counts
    sentiment_counts = df['sentiment'].value_counts()

    # tabs
    tabs = st.tabs([
        "Reviews",
        "Sentiment Distribution",
        "Score Analysis",
        "Sentiment vs Score",
        "Content Analysis",
        "Summary Stats"
    ])

    # Tab 01: Reviews with predicted sentiment and score
    with tabs[0]:
        st.markdown(f"#### {emoji.emojize(':memo:', language='alias')} Quick Review Summary")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Positive", sentiment_counts.get('POSITIVE', 0))
        with col2:
            st.metric("Negative", sentiment_counts.get('NEGATIVE', 0))
        with col3:
            st.metric("Neutral", sentiment_counts.get('NEUTRAL', 0))

        st.markdown("**Movie Reviews:**")
        for review in reviews:
            try:
                display_review_card(review)
            except Exception as e:
                st.warning(f"Skipped a review due to error: {e}")

    # Tab 02 to 06 for analysis 
    try:
        with tabs[1]:
            sentiment_distribution_plots(df)
    except Exception as e:
        st.error(f"Error in Sentiment Distribution tab: {e}")

    try:
        with tabs[2]:
            sentiment_score_analysis_plots(df)
    except Exception as e:
        st.error(f"Error in Score Analysis tab: {e}")

    try:
        with tabs[3]:
            sentiment_vs_score_plots(df)
    except Exception as e:
        st.error(f"Error in Sentiment vs Score tab: {e}")

    try:
        with tabs[4]:
            content_analysis_plots(df)
    except Exception as e:
        st.error(f"Error in Content Analysis tab: {e}")

    try:
        with tabs[5]:
            summary_statistics(df)
    except Exception as e:
        st.error(f"Error in Summary Statistics tab: {e}")

def sentiment_analysis_tab():

    st.markdown(f"## {emoji.emojize(':mag_right:', language='alias')} Movie Search & Analysis")
    search_query = st.text_input(
        f"{emoji.emojize(':clapper:', language='alias')} Enter movie name:", 
        placeholder="e.g., The Matrix, Inception, Avatar...", 
        key="search_input"
    )
    
    if search_query and search_query != st.session_state.last_search_query:
        try:
            with st.spinner("Searching for movies..."):
                total_movie_results = fetch_movie_data(search_query)
                st.session_state.movies = total_movie_results
                st.session_state.current_page = 1
                st.session_state.last_search_query = search_query

            if total_movie_results:
                st.success(f"Found {len(total_movie_results)} movies matching '{search_query}'")
            else:
                st.warning("No movies found. Try a different search term.")
        except Exception as e:
            st.error(f"Error while searching: {e}")
            return
    
    # search results
    if st.session_state.movies:
        st.markdown(f"### {emoji.emojize(':movie_camera:', language='alias')} Search Results")

        # pages to switch between movies
        total_movies = len(st.session_state.movies)
        total_pages = min(total_movies, 10) # only showing at most 10 pages 
        
        col1, col2, col3 = st.columns([4, 4, 1])
        with col1:
            if st.button(f"{emoji.emojize(':arrow_backward:', language='alias')} Previous") and st.session_state.current_page > 1:
                st.session_state.current_page -= 1
                st.rerun()  # immediate rerun so display updates
        with col2:
            st.write(f"Page {st.session_state.current_page} of {total_pages}")
        with col3:
            if st.button(f"{emoji.emojize(':arrow_forward:', language='alias')} Next") and st.session_state.current_page < total_pages:
                st.session_state.current_page += 1
                st.rerun()  # immediate rerun so display updates

        # print(st.session_state.current_page)
        currunt_movie_index = st.session_state.current_page - 1
        movie = st.session_state.movies[currunt_movie_index]

        # display movie
        try:
            display_movie_card(movie)
        except Exception as e:
            st.error(f"Failed to display movie card: {e}")
        

        if st.button(f"{emoji.emojize(':mag:', language='alias')} Perform Review Analysis", key="analyze_button"):
            try:
                with st.spinner("Fetching reviews..."):
                    reviews = get_reviews(movie.get('imdbID'))
                    if reviews == None or len(reviews) == 0:
                        raise ValueError("No reviews to fetch!")
                    reviews = predict(reviews)
                    st.session_state.reviews[movie.get('imdbID')] = reviews
                st.success("Reviews fetched successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Failed to fetch reviews: {e}")

        
        # display reviews analysis if reviews fetched
        if movie.get('imdbID') in st.session_state.get('reviews', {}):

            st.markdown(f"#### {emoji.emojize(':memo:', language='alias')} Detailed Review Sentiment Analysis")
            reviews = st.session_state.reviews[movie.get('imdbID')]

            try:
                display_review_analysis(reviews)
            except Exception as e:
                st.error(f"Error while performing review analysis: {e}")

# For testing
if __name__ == '__main__':
    sentiment_analysis_tab()