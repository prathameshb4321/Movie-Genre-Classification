from flask import Flask, render_template, request
import joblib
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

app = Flask(__name__)

# Load trained model
model = joblib.load("movie_genre_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()


def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)

    words = text.split()

    words = [
        stemmer.stem(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    plot = request.form["plot"]

    cleaned = preprocess(plot)

    vector = tfidf.transform([cleaned])

    prediction = model.predict(vector)[0]

    return render_template(
        "index.html",
        prediction=prediction,
        plot=plot
    )


if __name__ == "__main__":
    app.run(debug=True)