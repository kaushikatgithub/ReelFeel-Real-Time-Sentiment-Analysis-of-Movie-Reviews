import requests
import pandas as pd

from bs4 import BeautifulSoup
from config import search_movie_url, request_headers
from config import class_names, review_container_class

def get_reviews(movie_id: str, spoiler_free: bool = False) -> pd.DataFrame:
    """Scrape user reviews for a given IMDb movie ID.

    Args:
        movie_id (str): IMDb ID of the movie (e.g., 'tt1234567')
        spoiler_free (bool): Whether to exclude reviews with spoilers

    Returns:
        pd.DataFrame: DataFrame containing title, rating, and content of reviews
    """
    try:
        url = search_movie_url(movie_id=movie_id, spoiler_free=spoiler_free)
        response = requests.get(url, headers=request_headers)

        if response.status_code != 200:
            raise ConnectionError(f"Failed to fetch page: {response.status_code}")

        soup = BeautifulSoup(response.text, 'html.parser')
        review_containers = soup.find_all('div', class_=review_container_class)

        reviews = []
        for container in review_containers:
            rating = container.find('span', class_=class_names['rating'])
            title = container.find('h3', class_=class_names['title'])
            content = container.find('div', class_=class_names['content'])

            review = {
                'rating': rating.get_text(strip=True) if rating else None,
                'title': title.get_text(strip=True) if title else None,
                'content': content.get_text(strip=True) if content else None
            }

            if review['content']:
                reviews.append(review)

        return reviews

    except Exception as e:
        print(f"[Error] Could not fetch reviews for {movie_id}: {e}")
        return None

# For testing
# if __name__ == "__main__":
#     reviews = get_reviews('tt2631186')
#     for review in reviews:
#         print(f'{review["rating"]} || {review["title"]} || {review["content"]}')