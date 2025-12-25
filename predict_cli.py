import joblib
import sys

model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

email_text = input("Paste email text:\n")

features = vectorizer.transform([email_text])
prediction = model.predict(features)[0]

if prediction == 1:
    print("\n⚠️ Result: Suspicious (Phishing)")
else:
    print("\n✅ Result: Likely Safe")