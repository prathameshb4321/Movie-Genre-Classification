LINK - https://web-production-69431.up.railway.app


# 🎬 Movie Genre Classification using Machine Learning

## 📌 Project Overview

This project predicts the **genre of a movie** from its **plot summary** using Machine Learning and Natural Language Processing (NLP). The application preprocesses the movie description, converts it into TF-IDF features, and predicts the genre using a trained **Linear Support Vector Machine (Linear SVM)** model.

A Flask web application is included to provide an interactive interface where users can enter a movie plot and instantly receive the predicted genre.

---

## 🚀 Features

* Predicts movie genre from plot summaries.
* Text preprocessing using NLP techniques.
* TF-IDF feature extraction.
* Linear SVM classifier.
* User-friendly Flask web interface.
* Trained model saved using Joblib.
* Easy deployment on cloud platforms.

---

## 🛠️ Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* NLTK
* Joblib
* HTML
* CSS

---

## 📂 Dataset

Dataset: Movie Genre Classification Dataset

Each record contains:

* Movie ID
* Movie Title
* Movie Genre
* Movie Description

The model learns from the movie descriptions and predicts the corresponding genre.

---

## 📊 Machine Learning Pipeline

1. Load Dataset
2. Data Cleaning
3. Text Preprocessing

   * Lowercase conversion
   * Remove punctuation
   * Remove numbers
   * Stopword removal
   * Stemming
4. TF-IDF Vectorization
5. Train-Test Split
6. Model Training using Linear SVM
7. Hyperparameter Tuning using GridSearchCV
8. Model Evaluation
9. Save Model
10. Deploy with Flask

---

## 📈 Model Performance

| Model       | Accuracy   |
| ----------- | ---------- |
| Naive Bayes | 51.96%     |
| Linear SVM  | **59.56%** |

Linear SVM provided the best performance and was selected for deployment.

---

## 📁 Project Structure

```text
Movie-Genre-Classification/
│
├── app.py
├── preprocess.py
├── requirements.txt
├── movie_genre_model.pkl
├── tfidf_vectorizer.pkl
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── notebook.ipynb
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/prathameshb4321/Movie-Genre-Classification.git
```

Move into the project folder

```bash
cd Movie-Genre-Classification
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 💡 Example Prediction

**Input**

```
A detective investigates a mysterious murder in a small town while uncovering hidden secrets.
```

**Predicted Genre**

```
Drama
```

---

## 📸 Screenshots



* Home Page
* Genre Prediction
* Result Page

---

## 🔮 Future Improvements

* Improve model accuracy using Transformer models (BERT, RoBERTa).
* Add confidence score for predictions.
* Predict Top-3 probable genres.
* Deploy using Docker.
* Add REST API support.

---



## ⭐ If you found this project useful, please give it a star!
