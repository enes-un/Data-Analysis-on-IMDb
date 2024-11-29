# Data-Analysis-on-IMDb

This project is created for the course project of *Introduction to Data Science* at Sabancı University (2024-2025).  
The analysis explores my viewing habits for both movies and TV series using data from my IMDb activity and metadata retrieved from the IMDb database.  
The aim is to uncover patterns in my preferences, compare my ratings with IMDb user ratings, and gain insights into my behavior across both mediums.

## Table of Contents
1. [Motivation](#motivation)  
2. [Research Questions](#research-questions)  
3. [Data Source](#data-source)  
   - [Personal IMDb Data](#personal-imdb-data)  
   - [IMDb Metadata](#imdb-metadata)  

## Motivation

Movies and TV series are significant parts of my leisure time, and I often wonder how my preferences compare to common trends.  
The motivation behind this project is to better understand my viewing patterns, favorite genres, and how my personal ratings align or diverge from IMDb's scores.

## Research Questions

1. **What are my most-watched genres, and how do they compare to my favorite ones?**  
2. **How do my ratings align with or differ from IMDb's ratings?**  
3. **Who are my favorite directors and actors based on my viewing and ratings?**  
4. **What are the common properties (genre, duration, release year, etc.) of movies and TV series among my likes and dislikes?**  
5. **Are there differences in my preferences between movies and TV series (e.g., do I prefer certain genres in one over the other)?**  

## Data Source

### Personal IMDb Data
Exported from my IMDb account, including:
- Movie ratings and watchlist.  
- TV series ratings.  

### IMDb Metadata
Retrieved using the IMDbPY package, including:
- Genres, IMDb ratings, runtime, and release years for both movies and TV series.  
- Cast and directors for both movies and series.  
