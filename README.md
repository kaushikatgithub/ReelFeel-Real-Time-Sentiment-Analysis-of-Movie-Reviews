# ReelFeel – Movie Review Sentiment Analysis Dashboard

**ReelFeel** is an interactive web application developed using Streamlit that performs real-time sentiment analysis on IMDb movie reviews. It combines web scraping, natural language processing, and deep learning to provide insightful visualizations of audience sentiment for any selected movie.

---
## Live Demo

#### Check out the live application here: [Movie Review Analysis Dashboard](https://reelfeel-real-time-sentiment-analysis-of-movie-reviews.streamlit.app/)

## Overview

ReelFeel enables users to:

- Search and discover movies through a clean, paginated interface.
- Automatically fetch real user reviews from IMDb.
- NLP based sentiment analysis on reviews using a trained Recurrent Neural Network (RNN).
- View detailed movie profiles, including plot, cast, crew, and ratings.
- Explore visual insights such as sentiment breakdowns and score distributions.

This tool is suitable for data analysts and movie enthusiasts interested in understanding audience opinions at scale.

---

## Key Features

### Movie Search and Discovery

- Search movies by title
- View results with pagination and easy navigation
- Access detailed movie profiles with posters, plots, genres, and metadata

### Review Analysis

- Automatically scrape IMDb reviews for the selected movie
- Predict sentiment using a trained RNN model
- Generate a sentiment score per review
- Perform multi-dimensional analysis of public opinion

### Visual Insights

- Sentiment distribution charts (positive, negative, neutral)
- Histograms of predicted review scores
- Summary of ratings and emotional tone

---

## How It Works

1. Enter a movie title in the search bar.
2. Browse the search results and select a specific movie.
3. The app fetches details and real audience reviews.
4. Click on "Perform Analysis" to run sentiment prediction.
5. View the results through interactive graphs and summary metrics.

**Example Workflow:**

- Search for *The Dark Knight*
- Select the 2008 version from the results
- Review the plot, cast, and genre
- Click *Perform Analysis*
- Explore the sentiment chart, review scores, and keyword trends

---

## Technology Stack

### Frontend

- Streamlit (for building the web interface)
- Python (application logic)
- Custom UI components

### Data Handling and Visualization

- Pandas and NumPy (data processing)
- Plotly and Matplotlib (interactive charts)

### NLP and Machine Learning

- TensorFlow (RNN model for sentiment analysis)
- Text preprocessing with NLP tools
- Predictive scoring and classification

### API and Web Scraping

- OMDb API (movie details)
- IMDb (for user reviews)

---

## Analysis Capabilities

- Sentiment classification: Positive, Negative, Neutral
- Numerical score prediction from review content
- Sentiment trend detection (future enhancement)
- Rating and sentiment distribution charts
---

## Target Users

### Movie Enthusiasts

- Explore public perception before watching a movie
- Compare reviews across titles
- Create informed watchlists based on sentiment

### Data Analysts and Researchers

- Analyze real-world, unstructured review data
- Visualize public opinion using NLP
- Extract actionable insights from large text datasets

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/kaushikatgithub/ReelFeel-Real-Time-Sentiment-Analysis-of-Movie-Reviews.git
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure OMDb API

Obtain a free API key from [http://www.omdbapi.com/apikey.aspx](http://www.omdbapi.com/apikey.aspx).  
Set your API key in a `.env` file or update the `config.py` directly.

Example `.env`:
```
OMDB_API_KEY=your_api_key_here
```

### 4. Launch the Application

```bash
streamlit run app/main.py
```

---

## Project Structure

```
reelfeel/
├── app/
│   ├── main.py              # Entry point (Streamlit)
│   ├── config.py            # API configuration   
│   ├── style.css            # Basic style for components
│   ├── components/          # UI tab components and analysis functions
|   └── utils/               # OMDb integration, IMDb scraping and Sentiment prediction logic
│  
├── models/                  # Pretrained RNN model files
├── files/                   # Training logs
├── notebooks/               # Jupyter notebooks (training notebook)
├── requirements.txt         # Required Python packages
└── README.md
```
---

## Future Enhancements

- Support for multilingual reviews and translation
- Emotion-specific tagging (anger, joy, sadness)
- Time-series analysis of review trends
- Genre-based sentiment comparison
- User authentication and history tracking

---

## Acknowledgments

- TensorFlow and Keras for the RNN model
- OMDb API for movie metadata
- IMDb for review scraping
- Streamlit for the interactive dashboard framework
