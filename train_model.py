import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv("data/emails.csv")

print("Columns:", data.columns)

# Combine subject + body (BEST PRACTICE)
data["text"] = data["subject"].fillna("") + " " + data["body"].fillna("")

X = data["text"]
y = data["label"]

# Convert text to numbers
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=6000,
    ngram_range=(1, 2)
)

X_tfidf = vectorizer.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model and vectorizer
joblib.dump(model, "model/model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Model trained and saved successfully")