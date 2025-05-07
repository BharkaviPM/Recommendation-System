# Recommendation-System
Using ML and Matrix Factorization

---

*COMPANY:* CODTECH IT SOLUTIONS  
*NAME:* BHARKAVI P M  
*INTERN ID:* CT04DK897  
*DOMAIN:* MACHINE LEARNING  
*DURATION:* 4 WEEKS  (30th APR - 30th MAY)  
*MENTOR:* NEELA SANTHOSH  
*Current date:* Saturday, May 03, 2025, 5:45 PM IST

---

## *Project Overview*

This project demonstrates how to build a *Recommendation System* using *collaborative filtering* and *content-based filtering* techniques. The goal is to suggest movies to users based on their preferences and similarities between movies. The deliverable is a *Jupyter Notebook* that showcases the recommendation pipeline, displays sample recommendations, and evaluates the system's effectiveness.

---

## *Motivation*

*Recommendation systems* are essential in today’s digital platforms, powering user experiences for streaming services, e-commerce, and social media. By leveraging user ratings and movie content, such systems can personalize suggestions, increase user engagement, and enhance satisfaction. This project provides practical experience in building a recommendation engine using real-world movie data.

---

## *Tools and Technologies*

- *Python:* The primary programming language for this implementation.
- *Jupyter Notebook:* For interactive code execution, visualization, and documentation.
- *Pandas:* For data loading, manipulation, and analysis.
- *scikit-learn:* For feature extraction and similarity computation:
  - *TfidfVectorizer* for converting movie metadata into numerical features.
  - *cosine_similarity* for measuring similarity between movies.
- *CSV Files:*  
  - *ratings.csv:* Contains user ratings for movies.
  - *movies.csv:* Contains movie titles and genres.

---

## *Dataset*

- *movies.csv:* Includes movie titles and genres, used for content-based filtering.
- *ratings.csv:* (Optional for this example) Contains user ratings, which can be used for collaborative filtering approaches.
- Both datasets are standard in movie recommendation system tutorials and provide a robust foundation for building and testing recommendation algorithms.

---

## *Workflow*

1. *Data Loading:*  
   Load movies.csv and ratings.csv into Pandas DataFrames.

2. *Data Preprocessing:*  
   - Remove missing values from the movie dataset.
   - Combine movie titles and genres into a single feature called *"tags"* for each movie.

3. *Feature Extraction:*  
   - Use *TF-IDF Vectorization* to convert the combined tags into numerical feature vectors, capturing the importance of words in the context of the entire dataset.

4. *Similarity Computation:*  
   - Compute the *cosine similarity matrix* between all movies, quantifying how similar each movie is to every other based on their content features.

5. *Recommendation Function:*  
   - Implement a function that, given a movie title, finds the most similar movies using the similarity matrix and returns a list of recommendations.

6. *Example Usage:*  
   - Provide sample recommendations for a given movie (e.g., "Toy Story (1995)") and display the top 5 most similar movies.

---

## *How to Run*

1. Ensure movies.csv (and optionally ratings.csv) are present in your working directory.
2. Open the provided Jupyter Notebook.
3. Run each cell sequentially to load data, build the recommendation system, and generate sample recommendations.

---

## *Learning Outcomes*

- Understand the principles of *content-based filtering* and *collaborative filtering*.
- Gain experience with *TF-IDF vectorization* and *cosine similarity* for measuring item similarity.
- Learn to design and implement a recommendation function.
- Develop skills in data preprocessing, feature engineering, and model evaluation for recommendation systems.

---

## *Conclusion*

This project delivers a hands-on approach to building a *Recommendation System* using Python and scikit-learn. By combining content-based filtering with robust similarity measures, the system can effectively suggest movies similar to a user’s choice. The workflow is adaptable for more advanced recommendation strategies, including collaborative filtering and hybrid models, making it an excellent foundation for further exploration in recommender systems.

---

# Output

---

![Image](https://github.com/user-attachments/assets/df65b501-8481-449a-acf9-1ed280ad9e26)

---
