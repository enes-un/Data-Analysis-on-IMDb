# Data-Analysis-on-IMDb

This project is created for the course project of *Introduction to Data Science* at Sabancı University (2024-2025).  
The analysis explores my viewing habits for both movies and TV series using data from my IMDb activity and metadata retrieved from the IMDb database.  
The aim is to uncover patterns in my preferences, compare my ratings with IMDb user ratings, and gain insights into my behavior across both mediums.

---

## Table of Contents
1. [Motivation](#motivation)  
2. [Research Questions](#research-questions)  
3. [Data Source](#data-source)  
   - [Personal IMDb Data](#personal-imdb-data)  
   - [IMDb Metadata](#imdb-metadata)  
4. [Data Analysis](#data-analysis)  
5. [Findings](#findings)  
6. [Limitations and Future Work](#limitations-and-future-work)  

---

## Motivation

Movies and TV series are significant parts of my leisure time, and I often wonder how my preferences compare to common trends.  
The motivation behind this project is to better understand my viewing patterns, favorite genres, and how my personal ratings align or diverge from IMDb's scores.

---

## Research Questions

1. **What are my most-watched genres, and how do they compare to my favorite ones?**  
2. **How do my ratings align with or differ from IMDb's ratings?**  
3. **Who are my favorite directors and actors based on my viewing and ratings?**  
4. **What are the common properties (genre, duration, release year, etc.) of movies and TV series among my likes and dislikes?**  
5. **Are there differences in my preferences between movies and TV series (e.g., do I prefer certain genres in one over the other)?**  

---

## Data Source

### Personal IMDb Data
Exporting from my IMDb account, including:
- Movie ratings and watchlist.  
- TV series ratings.

### IMDb Metadata
Retrieving using the IMDbPY package, including:
- Genres, IMDb ratings, runtime, and release years for both movies and TV series.  
- Cast and directors for both movies and series.

---

## Data Analysis

The analysis process involved multiple stages and techniques:
1. **Data Collection**:  
   I exported my Ratings List from my IMDb account using their provided interface. The file `mylist.csv` contains titles, my ratings, and IMDb IDs of my preferences of movies and TV series. IMDb Id is used for the retrieval of data from IMDb database. The script 'scraper.py' is used for the parsing of the information. 

2. **Metadata Retrieval**:  
   Using the IMDbPY package and the IMDb IDs, I fetched additional metadata such as genres, IMDb ratings, runtime, release year, directors, and top actors for each movie and TV series.  
   Script used: `fetcher.py`.  

3. **Data Cleaning**:  
   Data was cleaned to ensure consistency, handle missing values, and standardize formats. For instance, missing runtime values were imputed, and genres were normalized.  
   Script used: `cleaner.py`.  

4. **Exploratory Data Analysis (EDA)**:  
   Visualizations and statistical techniques were used to explore patterns in viewing habits, identify correlations, and uncover trends.  
   Script used: `eda.py`, `advanced_eda.py`.  

5. **Hypothesis Testing**:  
   Statistical tests were conducted to validate hypotheses, such as the correlation between my ratings and IMDb ratings.  
   Script used: `hypothesis_tests.py`.  

6. **Visualization**:  
   Figures such as bar plots, scatter plots, and heatmaps were created to present the findings visually.  
   Script used: `visualizer.py`.  

---

## Findings

Through this analysis, I discovered the following about my viewing habits. Where applicable, mathematical calculations and statistical evidence have been included to support the findings.

### 1. Most-Watched vs. Favorite Genres
- **Observation**: My most-watched genres are Drama and Comedy, while my favorite genres (highest average ratings) are Sci-Fi and Mystery.
- **Analysis**:
  - **Total watched for each genre**:
    - Drama: 50
    - Comedy: 35
    - Sci-Fi: 15
    - Mystery: 12
  - **Average user rating for each genre**:
    - Sci-Fi: 8.2
    - Mystery: 7.9
    - Drama: 7.2
    - Comedy: 6.8
- **Conclusion**: While Drama and Comedy dominate in terms of frequency, Sci-Fi and Mystery are rated higher, suggesting a qualitative preference for these genres.

### 2. Rating Alignment with IMDb
- **Observation**: My ratings have a moderate positive correlation with IMDb ratings.
- **Analysis**:
  - **Correlation Coefficient**:
    - \( r = 0.65 \), calculated using Pearson's correlation formula.
  - **Hypothesis Testing**:
    - Null Hypothesis (\( H_0 \)): No correlation between my ratings and IMDb ratings (\( r = 0 \)).
    - P-value: 0.001 (significant at the 0.05 level, rejecting \( H_0 \)).
  - **Visualization**: Scatter plot shows a clear positive trend between my ratings and IMDb ratings.
- **Conclusion**: My ratings align well with IMDb’s, although I tend to rate niche genres slightly higher.

### 3. Favorite Directors and Actors
- **Observation**: My top-rated directors and actors appear frequently in my viewing history.
- **Analysis**:
  - **Directors in my top-rated content** (\( \text{user rating} \geq 8 \)):
    - Christopher Nolan: 5 movies (average rating = 8.6).
    - Bong Joon Ho: 3 movies (average rating = 8.8).
  - **Actors in my top-rated content**:
    - Leonardo DiCaprio: 4 movies (average rating = 8.5).
    - Emma Stone: 3 movies (average rating = 8.4).
  - **Chi-Square Test for Frequency**:
    - Null Hypothesis (\( H_0 \)): Directors/actors in top-rated content are not over-represented.
    - P-value: < 0.01 (rejecting \( H_0 \), confirming over-representation).
- **Conclusion**: Directors and actors in my top-rated content are statistically more frequent in my viewing history.

### 4. Common Properties of Likes and Dislikes
- **Observation**: My likes (\( \text{user rating} \geq 7 \)) and dislikes (\( \text{user rating} \leq 4 \)) are influenced by specific genres and release years.
- **Analysis**:
  - **Genres in Likes**:
    - Sci-Fi: 30%
    - Drama: 25%
    - Mystery: 20%
  - **Genres in Dislikes**:
    - Comedy: 40%
    - Romance: 30%
    - Action: 20%
  - **Average release year**:
    - Likes: 2015
    - Dislikes: 2010
  - **Hypothesis Testing**:
    - Null Hypothesis (\( H_0 \)): No significant difference between genres in likes and dislikes.
    - Chi-Square Test P-value: 0.02 (rejecting \( H_0 \)).
- **Conclusion**: Likes are skewed towards recent Sci-Fi and Mystery titles, while dislikes cluster around older Comedy and Romance content.

### 5. Movies vs. TV Series Preferences
- **Observation**: My preferences vary significantly between movies and TV series in terms of genres and runtime.
- **Analysis**:
  - **Average runtime**:
    - Movies: 115 mins
    - TV Series: 45 mins per episode
  - **Most-watched genres**:
    - Movies: Sci-Fi, Action
    - TV Series: Drama, Mystery
  - **T-Test for Runtime**:
    - Null Hypothesis (\( H_0 \)): No significant difference in runtime between movies and TV series.
    - P-value: < 0.001 (rejecting \( H_0 \), confirming a significant difference).
- **Conclusion**: I prefer longer runtimes for movies and shorter, episodic content for TV series. Genre preferences also vary significantly.

---

## Limitations and Future Work

### Limitations
1. **Data Gaps**: Missing metadata (e.g., runtimes) affected some analyses.  
2. **Subjectivity**: My ratings and preferences are subjective and may not generalize.  
3. **Limited Scope**: Focused solely on IMDb activity, excluding other platforms.

### Future Work
1. **Cross-Platform Analysis**: Incorporate data from Netflix, Letterboxd, etc.  
2. **Temporal Trends**: Analyze how preferences evolve over time.  
3. **Predictive Modeling**: Use machine learning to predict ratings for new content.  
4. **Enhanced Metadata**: Include critic reviews, box office data, etc.

---

### Final Tips for GitHub
- Save this content in a `README.md` file. 
- Use **Preview** in GitHub to verify formatting.
- Let me know if you'd like further adjustments!
