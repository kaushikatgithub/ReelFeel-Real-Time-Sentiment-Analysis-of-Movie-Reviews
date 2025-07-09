import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from dotenv import load_dotenv
from pathlib import Path

# Load .env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

MAX_LEN = os.getenv("MAX_LEN")
MODEL_PATH = os.getenv("MODEL_PATH")

# Loading IMDB word index 
try:
    word_index = tf.keras.datasets.imdb.get_word_index()
    word_index = {k: (v + 3) for k, v in word_index.items()}
    word_index["<PAD>"] = 0
    word_index["<START>"] = 1
    word_index["<UNK>"] = 2
    word_index["<UNUSED>"] = 3
except Exception as e:
    raise RuntimeError(f"Failed to load IMDB word index: {e}")

# Model Loading
try:
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at path: {MODEL_PATH}")
    model = load_model(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Failed to load sentiment analysis model: {e}")

def sentiment(score: float) -> str:
    if score <= 0.4:
        return "NEGATIVE"
    elif score <= 0.6:
        return "NEUTRAL"
    else:
        return "POSITIVE"

def encode_review(text: str) -> list[int]:
    """
    Convert text to integer sequence based on IMDB word_index
    """
    if not isinstance(text, str):
        raise ValueError("Input text must be a string.")

    tokens = text.lower().split()
    encoded = [1]  # <START> token
    for word in tokens:
        index = word_index.get(word, 2)  # 2 = <UNK>
        encoded.append(index)
    return encoded

def predict(reviews: list[dict]) -> list[dict]:
    """
    Predict sentiment for list of review dictionaries.

    Args:
        reviews (list): Each dict must contain 'title' and 'content' keys.

    Returns:
        list: Reviews with added 'score' and 'sentiment' keys.
    """
    if not isinstance(reviews, list):
        raise TypeError("Input reviews must be a list of dictionaries.")

    try:
        encoded_reviews = []
        for review in reviews:
            if not isinstance(review, dict):
                raise ValueError("Each review must be a dictionary.")
            if 'title' not in review or 'content' not in review:
                raise KeyError("Each review must have 'title' and 'content' keys.")
            text = review['title'] + " " + review['content']
            encoded = encode_review(text)
            encoded_reviews.append(encoded)

        padded_reviews = pad_sequences(encoded_reviews, maxlen=MAX_LEN, padding='pre')

        predictions = model.predict(padded_reviews)

        for i, p in enumerate(predictions.flatten()):
            score = np.round(p, 4)
            reviews[i]['score'] = float(score)
            reviews[i]['sentiment'] = sentiment(score)

        return reviews

    except Exception as e:
        raise RuntimeError(f"Error during sentiment prediction: {e}")


# For Testing
# from dummy_data import sample_reviews
# if __name__ == '__main__':

#     results = predict_sentiment(sample_reviews)
#     for i, result in enumerate(results):
#         print(f"Actual Sentiment: {sample_reviews[i]['sentiment']}")
#         print(f"Predicted Sentiment: {result}", end="\n\n")

