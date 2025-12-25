🛡️ AI-Powered Phishing Email Detector

An advanced cybersecurity machine learning project that detects phishing emails using Natural Language Processing (NLP), Machine Learning, and optional Large Language Model (LLM) analysis.

This system provides both fast probabilistic detection and context-aware reasoning, similar to real-world security tools.

📌 Project Overview

Phishing emails are one of the most common cyberattacks used to steal credentials, financial data, and personal information.
This project builds an intelligent phishing email detection system that:

Learns from real phishing email datasets

Analyzes email content using NLP techniques

Predicts phishing probability

Provides an optional LLM-based security explanation

Offers both CLI and Web UI interfaces

🚀 Features

✅ Machine Learning-based phishing detection

✅ TF-IDF text vectorization

✅ Logistic Regression classifier

✅ Confidence score & risk level

✅ Optional LLM (GPT) contextual analysis

✅ Interactive Streamlit Web UI

✅ Command Line Interface (CLI)

✅ Clean, professional, and interview-ready design

🧠 System Architecture
Email Text
   ↓
Text Preprocessing
   ↓
TF-IDF Vectorization
   ↓
Logistic Regression Model
   ↓
Phishing Probability
   ↓
(Optional) LLM Analysis
   ↓
Final Verdict + Reasoning

🛠️ Technologies Used
Category	Technology
Programming Language	Python
Machine Learning	Scikit-learn
NLP	TF-IDF
Model	Logistic Regression
Web UI	Streamlit
LLM (Optional)	OpenAI GPT
Serialization	Joblib
📂 Project Structure
phishing_email_detector/
│
├── data/
│   └── emails.csv
│
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── train_model.py
├── predict_cli.py
├── app.py
├── requirements.txt
└── README.md

📊 Dataset Information

Public phishing email dataset (Kaggle)

Emails labeled as:

1 → Phishing

0 → Safe

Dataset contains real-world phishing and legitimate email samples

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/phishing_email_detector.git
cd phishing_email_detector

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Train the Model
python train_model.py


This will generate:

model/model.pkl

model/vectorizer.pkl

🖥️ Usage
🔹 Command Line Interface (CLI)
python predict_cli.py


Paste email text → Get phishing result instantly.

🔹 Web Application (Streamlit)
streamlit run app.py


Open browser → Paste email → Analyze → Get result with confidence.

🧠 LLM Integration (Optional)

This project supports Large Language Model analysis for advanced reasoning.

Steps:

Create OpenAI account

Generate API key

Set environment variable:

setx OPENAI_API_KEY "your_api_key_here"


Enable “Use LLM (Advanced Analysis)” checkbox in UI

The LLM provides:

Phishing confirmation

Risk level

Short explanation

📈 Model Performance

Lightweight & fast

Suitable for real-time detection

Works offline (ML-only mode)

LLM enhances explainability and accuracy

🔐 Security & Ethics

No email data is stored

API keys are kept secure using environment variables

LLM analysis is optional

Intended for educational and awareness purposes

📚 Learning Outcomes

By completing this project, you gain hands-on experience with:

NLP and text classification

Machine learning pipelines

Cybersecurity threat detection

Model deployment

Hybrid ML + LLM systems

Professional UI development

🧑‍💻 Use Cases

Academic projects

Cybersecurity internships

Resume & GitHub portfolio

Email security awareness tools

⚠️ Disclaimer

This tool provides probabilistic analysis and assists detection.
It does not replace human judgment or professional security systems.

📌 Future Enhancements

URL reputation analysis

Phishing keyword highlighting

Email header analysis

Scan history & logging

Explainable AI (SHAP)

User authentication

📄 License

This project is developed for educational purposes.
You may modify and extend it as needed.

🙌 Author

Krunal
B.E. Computer Engineering
Cybersecurity & Machine Learning Enthusiast
