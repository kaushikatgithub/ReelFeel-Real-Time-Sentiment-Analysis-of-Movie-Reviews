import os
import requests

from imdb import Cinemagoer
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)
API_KEY = os.getenv("API_KEY")

def fetch_movie_data(movie_name: str) -> dict:
    """Fetch movie details using IMDbPy and OMDb API.

    Args:
        movie_name (str): Name of the movie to search.

    Returns:
        dict: Dictionary containing movie data from OMDb API.
    """
    try:
        # Search movie using IMDbPy
        imdb_obj = Cinemagoer()
        search_results = imdb_obj.search_movie(movie_name)
        
        if not search_results:
            raise ValueError("No movie found with the given name.")

        data_list = []
        for movie in search_results[:5]:
            # movie = search_results[0]
            movie_title = movie.get('title', '')
            
            # Query OMDb API using the movie title
            url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"
            response = requests.get(url)

            if response.status_code != 200:
                raise ConnectionError(f"OMDb API error: {response.status_code}")

            data = response.json()
            if data.get('Response') == 'False':
                raise ValueError(f"OMDb Error: {data.get('Error')}")

            # Add cover page
            if 'full-size cover url' in movie:
                data['Cover Image'] = movie['full-size cover url']

            data_list.append(data)
            
        return data_list
    except Exception as e:
        print(f"Error fetching movie data: {e}")
        return {}

for movie in fetch_movie_data('krish'):
    print("\n\n New Movie:") 
    print(movie)
    print("\n\n")