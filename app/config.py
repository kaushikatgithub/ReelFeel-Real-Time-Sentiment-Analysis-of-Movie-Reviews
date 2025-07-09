def search_movie_url(movie_id: str, spoiler_free: bool = False) -> str:
    """Construct IMDb review URL for a movie with optional spoiler filtering."""

    # handling the case if movie_id is not provided
    if not movie_id:
        return "ERROR"
    
    base_url = f'https://www.imdb.com/title/{movie_id}/reviews/'
    spoiler_tag = '?spoilers=EXCLUDE'
    return base_url + spoiler_tag if spoiler_free else base_url

# IMDb review scraping configuration
review_container_class = 'ipc-list-card__content'

request_headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/80.0.3987.162 Safari/537.36'
    )
}

class_names = {
    'rating': 'ipc-rating-star--rating',
    'title': 'ipc-title__text ipc-title__text--reduced',
    'content': 'ipc-html-content-inner-div',
}
