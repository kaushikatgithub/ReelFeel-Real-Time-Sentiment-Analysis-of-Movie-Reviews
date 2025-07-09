import streamlit as st
import emoji

def get_sentiment_style(sentiment):
    """Return (color, emoji) tuple based on sentiment label."""
    sentiment = sentiment.upper()
    color_map = {
        "POSITIVE": "green",
        "NEUTRAL": "orange",
        "NEGATIVE": "red"
    }
    emoji_map = {
        "POSITIVE": ":smile:",
        "NEUTRAL": ":neutral_face:",
        "NEGATIVE": ":disappointed:"
    }
    return color_map.get(sentiment, "gray"), emoji.emojize(emoji_map.get(sentiment, ":question:"), language='alias')

def get_score_emoji(score):
    """Return an emoji based on the sentiment score."""
    thresholds = [
        (0.8, ":fire:"),
        (0.6, ":blush:"),
        (0.4, ":neutral_face:"),
        (0.2, ":confused:"),
        (0.0, ":skull:")
    ]
    
    for threshold, emoji_code in thresholds:
        if score >= threshold:
            return emoji.emojize(emoji_code, language='alias')
    return emoji.emojize(":question:", language='alias')


def display_review_card(review):
    """Render a styled review card in Streamlit showing sentiment, score, and optional rating."""

    try:
        heading = review['title']
        user_review = review['content']
        predicted_sentiment = review['sentiment']
        sentiment_score = review['score']

        sentiment_color, sentiment_emoji = get_sentiment_style(predicted_sentiment)

        with st.container():
            st.markdown(
                f"""
                <div style="background-color: #1e1e1e; border-left: 8px solid {sentiment_color}; border-radius: 10px; padding: 1rem; margin-bottom: 1rem; box-shadow: 0 0 10px rgba(0,0,0,0.3);">
                    <p style="font-size: 1.1rem; color: #fff;"><b>{emoji.emojize(":pushpin:", language="alias")} {heading}</b></p>
                    <p style="font-size: 1rem; color: #ccc;"><i>{user_review}</i></p>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <p style="margin: 0; font-weight: bold; color: {sentiment_color};">{sentiment_emoji} Sentiment: {predicted_sentiment}</p>
                        <p style="margin: 0; color: #aaa;"> {get_score_emoji(sentiment_score)} Score: <b>{sentiment_score:.2f}</b></p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
    except (KeyError, TypeError, ValueError) as e:
        st.error(f"Error displaying review: {e}")
        
# For testing
# from dummy_data import sample_reviews
# for review in sample_reviews:
#     display_review_card(review)
