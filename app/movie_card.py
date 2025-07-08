import streamlit as st

# css style is added in the single file named style.css

def display_movie_card(movie_data):
    """Display an enhanced movie card using Streamlit native components"""
    
    # movie card container
    st.markdown('<div class="movie-card">', unsafe_allow_html=True)
    
    # two columns for poster and info
    col1, col2 = st.columns([1, 2])
    
    with col1:

        # movie poster
        if movie_data.get('Poster') and movie_data.get('Poster') != 'N/A':
            st.image(movie_data.get('Poster'), width=200)
    
    with col2:

        # movie title and basic info
        st.markdown(f'<h1 class="movie-title">{movie_data.get("Title", "Unknown Title")}</h1>', unsafe_allow_html=True)
        st.markdown(f'<div class="movie-info">{movie_data.get("Year", "N/A")} • {movie_data.get("Rated", "Not Rated")} • {movie_data.get("Runtime", "N/A")}</div>', unsafe_allow_html=True)
        
        # imdb rating
        st.markdown("**Ratings:**")
        ratings_html = ""
        if movie_data.get('imdbRating'):
            ratings_html += f'<span class="rating-badge">⭐ IMDB: {movie_data.get("imdbRating")}/10</span>'
        
        # other ratings
        rotten_tomatoes = next((r['Value'] for r in movie_data.get('Ratings', []) if r['Source'] == 'Rotten Tomatoes'), None)
        if rotten_tomatoes:
            ratings_html += f'<span class="rating-badge">🍅 RT: {rotten_tomatoes}</span>'
        
        if movie_data.get('Metascore'):
            ratings_html += f'<span class="rating-badge">📊 Metacritic: {movie_data.get("Metascore")}/100</span>'
        
        st.markdown(ratings_html, unsafe_allow_html=True)
    
    # full movie details in a grid
    st.markdown("---")
    
    # 3 columns for tabs of details
    detail_col1, detail_col2, detail_col3 = st.columns(3)
    
    with detail_col1:
        st.markdown(f'<div class="detail-box"> <strong> 🎬 Director </strong> <br>{movie_data.get("Director", "N/A")}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="detail-box"> <strong> 🎪 Genre </strong> <br>{movie_data.get("Genre", "N/A")}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="detail-box"> <strong> 📅 Released </strong> <br>{movie_data.get("Released", "N/A")}</div>', unsafe_allow_html=True)
    
    with detail_col2:
        st.markdown(f'<div class="detail-box"> <strong> ✍️ Writer </strong> <br>{movie_data.get("Writer", "N/A")}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="detail-box"> <strong> 🗣️ Language </strong> <br>{movie_data.get("Language", "N/A")}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="detail-box"> <strong> 💰 Box Office </strong> <br>{movie_data.get("BoxOffice", "N/A")}</div>', unsafe_allow_html=True)
    
    with detail_col3:
        st.markdown(f'<div class="detail-box"> <strong> 🎭 Main Actors </strong> <br>{movie_data.get("Actors", "N/A")}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="detail-box"> <strong> 🌍 Country </strong> <br>{movie_data.get("Country", "N/A")}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="detail-box"> <strong> 👥 IMDB Votes </strong> <br>{movie_data.get("imdbVotes", "N/A")}</div>', unsafe_allow_html=True)
    
    # awards if any
    if movie_data.get('Awards') and movie_data.get('Awards') != 'N/A':
        st.markdown(f'<div class="awards-box">🏆 {movie_data.get("Awards")}</div>', unsafe_allow_html=True)
    
    # movie plot/subplot
    st.markdown(f'<div class="plot-box"> <strong> 📖 Plot </strong> <br>{movie_data.get("Plot", "No plot available.")}</div>', unsafe_allow_html=True)
    
    # end of movie card container
    st.markdown('</div>', unsafe_allow_html=True)


# For testing
# from dummy_data import MOCK_MOVIES
# display_movie_card(movie_data=MOCK_MOVIES[0])