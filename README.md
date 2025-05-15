# Spotify Analysis

## Project Overview

In this project, I explore a dataset of over 100,000 Spotify tracks to uncover patterns in song characteristics, genre trends, and audio-driven popularity. The dataset includes features like energy, danceability, loudness, valence, and explicitness, plus metadata such as genre and popularity scores.

The goal is to answer:
- What makes a song popular?
- How do audio features relate to each other?
- Are explicit songs more successful?
- Do genres differ in track length or energy?

Using data cleaning, aggregation, and visualization, I aim to extract insights while balancing statistical interpretation with musical intuition.

## Techniques Used

- **Data Cleaning**: Handling missing values, filtering noisy data
- **Exploratory Data Analysis (EDA)**: Summary statistics, grouped comparisons
- **Visualizations**: Line plots, histograms, boxplots, heatmaps
- **Feature Exploration**: Analyzing relationships between audio features and song popularity
- **Genre-Level Insights**: Examining how song duration and popularity vary across genres

## Tools & Libraries

- **Python 3.12** — Main programming language
- **Pandas** — Data manipulation and analysis
- **Matplotlib** — Core plotting library for visualizations
- **Seaborn** — Statistical data visualization built on top of matplotlib
- **Jupyter Notebook** — Interactive environment for running and presenting code- `matplotlib`

## Data Exploration & Cleaning

Before beginning analysis, I conducted a structured data exploration to ensure reliability:

- Reviewed the schema to interpret Spotify’s feature definitions
- Removed duplicate or null values
- Converted column types where necessary

This preparation step was crucial in making sure downstream visualizations were valid and interpretable.

## Key Visual Trends

- **Genre vs Popularity**: Some genres, especially pop and rap, dominate the popularity distribution.
- **Explicit vs Popularity**: Explicit songs trend toward higher popularity scores, possibly reflecting modern hit trends.
- **Energy vs Danceability**: Tracks with high energy often correlate with high danceability—EDM and pop tracks cluster in this area.
- **Duration by Genre**: Genres like jazz and classical tend to have longer average track durations than hip hop or electronic.

## What I Learned

This project helped me strengthen my ability to:

- Use visualizations to tell data-driven stories.
- Explore relationships across audio features and song metadata.
- Interpret musical trends using data.
- Work with real-world datasets in a structured analysis workflow.
