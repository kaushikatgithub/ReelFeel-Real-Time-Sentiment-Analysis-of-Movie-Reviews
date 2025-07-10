import os
import requests
from imdb import Cinemagoer
from dotenv import load_dotenv
from pathlib import Path
import streamlit as st

# for deployement
try:
    # Try to load from Streamlit secrets (used in deployed app)
    API_KEY = st.secrets["API_KEY"]
except Exception:
    # Fallback to .env for local development
    env_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(dotenv_path=env_path)
    API_KEY = os.getenv("API_KEY")



def fetch_movie_data(movie_name: str) -> list[dict]:
    """Fetch movie details using IMDbPy and OMDb API.

    Args:
        movie_name (str): Name of the movie to search.

    Returns:
        list[dict]: List of dictionaries containing movie data.
    """
    data_list = []
    try:
        if not API_KEY:
            raise EnvironmentError("API_KEY not found in environment.")

        imdb_obj = Cinemagoer()
        search_results = imdb_obj.search_movie(movie_name)

        if not search_results:
            raise ValueError("No movie found with the given name.")

        total_results = len(search_results)
        for i in range(min(total_results, 10)):
            movie = search_results[i]
            movie_title = movie.get('title', '')
            if not movie_title:
                continue

            url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                data = response.json()

                if data.get('Response') == 'False':
                    print(f"OMDb Error for '{movie_title}': {data.get('Error')}")
                    continue

                if 'full-size cover url' in movie:
                    data['Cover Image'] = movie['full-size cover url']

                data_list.append(data)

            except requests.exceptions.RequestException as re:
                print(f"Network error for movie '{movie_title}': {re}")
                return None
            except ValueError as ve:
                print(f"OMDb response parsing error: {ve}")
                return None

    except Exception as e:
        print(f"Fatal error fetching movie data: {e}")
        return None

    return data_list

# for testing
# for movie in fetch_movie_data('Inception'):
#     print("\n\n New Movie:\n", movie) 