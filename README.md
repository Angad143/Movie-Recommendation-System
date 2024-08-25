# **Tools and Libraries Used in Our Project**

<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://img.shields.io/badge/Google%20Colab-blue" alt="Google Colab" style="flex: 1 1 30%;">
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white" alt="Pandas" style="flex: 1 1 30%;">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white" alt="Streamlit" style="flex: 1 1 30%;">
  <img src="https://img.shields.io/badge/Scikit%20Learn-F7931E?style=flat&logo=scikit-learn&logoColor=white" alt="Scikit Learn" style="flex: 1 1 30%;">
  <img src="https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white" alt="NumPy" style="flex: 1 1 30%;">
  <img src="https://img.shields.io/badge/nltk-4A5C7D?style=flat&logo=nltk&logoColor=white" alt="nltk" style="flex: 1 1 30%;">
  <img src="https://img.shields.io/badge/Cosine%20Similarity-FF5722?style=flat&logo=python&logoColor=white" alt="Cosine Similarity" style="flex: 1 1 30%;">
  <img src="https://img.shields.io/badge/IMDB%20API-000000?style=flat&logo=imdb&logoColor=white" alt="IMDB API" style="flex: 1 1 30%;">
</div>

# **Movies Recommendation System**

## **Project Overview**
This project focuses on building a **Movies Recommendation System** using **content-based filtering** techniques. The system suggests movies based on the content and characteristics of the movies themselves, tailored to user preferences. The project is deployed using **Streamlit** to provide an interactive web application for users.

## **Step-by-Step Process**

### **1. Setting Up the Environment**
The project is developed using **Python** and is deployed with **Streamlit**. Key libraries include **Pandas**, **Scikit-Learn**, and **NumPy**. These libraries are used for data processing, model development, and building the recommendation system.

### **2. Data Collection**
Movie data is collected from a dataset containing movie titles, genres, descriptions, and other relevant information. The dataset used for this project is the **MovieLens dataset** or a similar dataset available from public sources.

### **3. Data Preprocessing**
- **Text Preprocessing**: Movie descriptions and other textual data are cleaned and preprocessed, including tokenization and stopword removal.
- **Feature Extraction**: Textual data is converted into numerical features using techniques like **TF-IDF**.But, Here we use **Bags of word techniques.**
- **Similarity Calculation**: The similarity between movies is computed based on their features, using measures such as **Cosine Similarity**.

### **4. Building the Recommendation System**
- A **content-based filtering** model is developed to recommend movies based on the similarity of movie features.
- **Similarity scores** are calculated between movies, and recommendations are generated based on these scores.

### **5. Model Evaluation**
- The performance of the recommendation system is evaluated using metrics like **Precision**, **Recall**, and **F1 Score**, if applicable.
- User feedback or offline testing is used to assess the quality and relevance of the recommendations.

### **6. Deployment with Streamlit**
- **Streamlit** is used to develop an interactive web application where users can input their preferences and receive movie recommendations.
- The application includes a user-friendly interface to display recommendations, movie details, and other relevant information.

### **7. Conclusion**
This project demonstrates the effectiveness of content-based filtering for movie recommendations, providing users with personalized suggestions based on movie content. The use of Streamlit enhances the accessibility and usability of the recommendation system, allowing for a rich user experience.

## **How to Run the Project**
1. **Clone the repository**.
2. **Install the required libraries** using the provided `requirements.txt`.
3. **Run the Streamlit app** using the command `streamlit run app.py` to start the web application.
4. **Interact with the application** to input preferences and receive movie recommendations.

## **Acknowledgments**
- Data sourced from **[tmdb Movies dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)** or similar datasets.
- Built with **Pandas**, **Scikit-Learn**, **NumPy**, and **Streamlit**.
