import streamlit as st
import pandas as pd
import plotly.express as px

def sentiment_distribution_plots(df: pd.DataFrame):
    "Function to plot sentiment distribution as pie and bar plots."

    st.subheader("Sentiment Distribution")

    try:
        if df.empty:
            st.warning("The input DataFrame is empty.")
            return

        if 'sentiment' not in df.columns:
            st.error("The DataFrame must contain a 'sentiment' column.")
            return

        sentiment_counts = df['sentiment'].value_counts()

        if sentiment_counts.empty:
            st.warning("No sentiment data available to plot.")
            return

        # pie chart
        fig_sentiment = px.pie(
            values=sentiment_counts.values,
            names=sentiment_counts.index,
            title="Distribution of Review Sentiments",
            color_discrete_map={'POSITIVE': '#2E8B57', 'NEGATIVE': '#DC143C', 'NEUTRAL': '#FFD700'}
        )
        st.plotly_chart(fig_sentiment, use_container_width=True)

        # bar plot
        fig_bar = px.bar(
            x=sentiment_counts.index,
            y=sentiment_counts.values,
            title="Sentiment Count",
            color=sentiment_counts.index,
            color_discrete_map={'POSITIVE': '#2E8B57', 'NEGATIVE': '#DC143C', 'NEUTRAL': '#FFD700'}
        )
        fig_bar.update_layout(xaxis_title="Sentiment", yaxis_title="Count")
        st.plotly_chart(fig_bar, use_container_width=True)

    except Exception as e:
        st.error(f"An error occurred while plotting sentiment distribution: {e}")

def sentiment_score_analysis_plots(df: pd.DataFrame):
    "Function to plot sentiment score distribution, box plot, and display statistics."

    st.subheader("Score Analysis")

    try:
        if df.empty:
            st.warning("The input DataFrame is empty.")
            return

        if 'score' not in df.columns:
            st.error("The DataFrame must contain a 'score' column.")
            return

        # only take valid score values
        df = df.copy()
        df['score'] = pd.to_numeric(df['score'], errors='coerce')
        df = df.dropna(subset=['score'])

        if df['score'].empty:
            st.warning("No valid numeric score data available to plot.")
            return

        # score distribution as a histogram
        fig_hist = px.histogram(
            df,
            x='score',
            nbins=20,
            title="Distribution of Review Scores",
            color_discrete_sequence=['#4CAF50']
        )
        fig_hist.update_layout(xaxis_title="Score", yaxis_title="Frequency")
        st.plotly_chart(fig_hist, use_container_width=True)

        # box plot of scores
        fig_box = px.box(
            df,
            y='score',
            title="Score Distribution (Box Plot)",
            color_discrete_sequence=['#2196F3']
        )
        st.plotly_chart(fig_box, use_container_width=True)

        # score statistics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Average Score", f"{df['score'].mean():.2f}")
        with col2:
            st.metric("Median Score", f"{df['score'].median():.2f}")
        with col3:
            st.metric("Min Score", f"{df['score'].min():.2f}")
        with col4:
            st.metric("Max Score", f"{df['score'].max():.2f}")

    except Exception as e:
        st.error(f"An error occurred during score analysis: {e}")

def sentiment_vs_score_plots(df: pd.DataFrame):
    "Function to compare sentiment and score via plots."

    st.subheader("Sentiment vs Score Analysis")

    try:
        if df.empty:
            st.warning("The input DataFrame is empty.")
            return

        required_cols = ['sentiment', 'score', 'title']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            st.error(f"Missing required column(s): {', '.join(missing_cols)}")
            return

        # only take valid score values
        df = df.copy()
        df['score'] = pd.to_numeric(df['score'], errors='coerce')
        df = df.dropna(subset=['sentiment', 'score', 'title'])

        if df.empty:
            st.warning("No valid data after cleaning. Please check for missing or invalid values.")
            return

        # scatter plot of socre with sentiment 
        fig_scatter = px.scatter(
            df,
            x='score',
            y='sentiment',
            title="Sentiment vs Score Distribution",
            color='sentiment',
            color_discrete_map={'POSITIVE': '#2E8B57', 'NEGATIVE': '#DC143C', 'NEUTRAL': '#FFD700'},
            hover_data=['title']
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

        # box plot by sentiment
        fig_box_sentiment = px.box(
            df,
            x='sentiment',
            y='score',
            title="Score Distribution by Sentiment",
            color='sentiment',
            color_discrete_map={'POSITIVE': '#2E8B57', 'NEGATIVE': '#DC143C', 'NEUTRAL': '#FFD700'}
        )
        st.plotly_chart(fig_box_sentiment, use_container_width=True)

        # average score by sentiment
        avg_scores = df.groupby('sentiment')['score'].mean().reset_index()
        fig_avg = px.bar(
            avg_scores,
            x='sentiment',
            y='score',
            title="Average Score by Sentiment",
            color='sentiment',
            color_discrete_map={'POSITIVE': '#2E8B57', 'NEGATIVE': '#DC143C', 'NEUTRAL': '#FFD700'}
        )
        st.plotly_chart(fig_avg, use_container_width=True)

    except Exception as e:
        st.error(f"An error occurred during sentiment vs score analysis: {e}")

def content_analysis_plots(df: pd.DataFrame):
    "Function to analyze content length and its relationship with sentiment and score."

    st.subheader("Content Analysis")

    try:
        if df.empty:
            st.warning("The input DataFrame is empty.")
            return

        required_cols = ['content', 'title', 'sentiment', 'score']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            st.error(f"Missing required column(s): {', '.join(missing_cols)}")
            return

        # Clean and convert necessary columns
        df = df.copy()
        df['content'] = df['content'].astype(str)
        df['title'] = df['title'].astype(str)
        df['score'] = pd.to_numeric(df['score'], errors='coerce')

        # Drop rows with any NaNs in required columns
        df = df.dropna(subset=['content', 'title', 'sentiment', 'score'])

        if df.empty:
            st.warning("No valid data after cleaning. Please check for missing or invalid values.")
            return

        # Calculate content and title lengths
        df['content_length'] = df['content'].str.len()
        df['title_length'] = df['title'].str.len()

        # Plot 1: Content length distribution
        fig_length = px.histogram(
            df,
            x='content_length',
            title="Distribution of Review Content Length",
            nbins=30,
            color_discrete_sequence=['#FF9800']
        )
        fig_length.update_layout(xaxis_title="Content Length (characters)", yaxis_title="Frequency")
        st.plotly_chart(fig_length, use_container_width=True)

        # Plot 2: Box plot of content length by sentiment
        fig_length_sentiment = px.box(
            df,
            x='sentiment',
            y='content_length',
            title="Content Length by Sentiment",
            color='sentiment',
            color_discrete_map={'POSITIVE': '#2E8B57', 'NEGATIVE': '#DC143C', 'NEUTRAL': '#FFD700'}
        )
        st.plotly_chart(fig_length_sentiment, use_container_width=True)

        # Plot 3: Scatter plot of content length vs score
        fig_length_score = px.scatter(
            df,
            x='content_length',
            y='score',
            title="Content Length vs Score",
            color='sentiment',
            color_discrete_map={'POSITIVE': '#2E8B57', 'NEGATIVE': '#DC143C', 'NEUTRAL': '#FFD700'},
            hover_data=['title']
        )
        st.plotly_chart(fig_length_score, use_container_width=True)

    except Exception as e:
        st.error(f"An error occurred during content analysis: {e}")

def summary_statistics(df: pd.DataFrame):
    st.subheader("Summary Statistics")

    try:
        if df.empty:
            st.warning("The input DataFrame is empty.")
            return

        required_cols = ['sentiment', 'score']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            st.error(f"Missing required column(s): {', '.join(missing_cols)}")
            return

        # valid dtypes
        df = df.copy()
        df['content_length'] = df['content'].str.len()
        df['score'] = pd.to_numeric(df['score'], errors='coerce')
        df['content_length'] = pd.to_numeric(df['content_length'], errors='coerce')
        df = df.dropna(subset=['sentiment', 'score', 'content_length'])

        if df.empty:
            st.warning("No valid data after cleaning.")
            return

        # summary table
        summary_stats = df.groupby('sentiment').agg({
            'score': ['count', 'mean', 'std', 'min', 'max'],
            'content_length': ['mean', 'std']
        }).round(2)

        # flattenning multi-index columns
        summary_stats.columns = ['_'.join(col).strip() for col in summary_stats.columns]
        summary_stats = summary_stats.reset_index()
        st.dataframe(summary_stats, use_container_width=True)

        # vverall Metrics
        st.subheader("Overall Metrics")
        total_reviews = len(df)
        pos = len(df[df['sentiment'] == 'POSITIVE'])
        neg = len(df[df['sentiment'] == 'NEGATIVE'])
        neu = len(df[df['sentiment'] == 'NEUTRAL'])
        pos_pct = (pos / total_reviews) * 100 if total_reviews > 0 else 0
        avg_score = df['score'].mean()

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Reviews", total_reviews)
            st.metric("Positive Reviews", pos)
        with col2:
            st.metric("Negative Reviews", neg)
            st.metric("Neutral Reviews", neu)
        with col3:
            st.metric("Positive Percentage", f"{pos_pct:.1f}%")
            st.metric("Overall Average Score", f"{avg_score:.2f}")

    except Exception as e:
        st.error(f"An error occurred during summary statistics calculation: {e}")
