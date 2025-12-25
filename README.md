# 🛡️ AI-Powered Phishing Email Detector

An advanced **cybersecurity machine learning project** that detects phishing emails using **Natural Language Processing (NLP)**, **Machine Learning**, and optional **Large Language Model (LLM)** analysis.

This system combines **fast probabilistic detection** with **context-aware reasoning**, similar to modern real-world email security tools.

---

## 📌 Project Overview

Phishing emails are one of the most common cyberattacks used to steal credentials, financial data, and personal information.

This project builds an **intelligent phishing email detection system** that:

- Learns from real-world phishing email datasets  
- Analyzes email content using NLP techniques  
- Predicts phishing probability with confidence score  
- Provides optional LLM-based security explanations  
- Offers both **Command Line Interface (CLI)** and **Web UI**  

---

## 🚀 Features

- ✅ Machine Learning–based phishing detection  
- ✅ TF-IDF text vectorization  
- ✅ Logistic Regression classifier  
- ✅ Confidence score & risk level  
- ✅ Optional LLM (GPT) contextual analysis  
- ✅ Interactive Streamlit Web UI  
- ✅ Command Line Interface (CLI)  
- ✅ Clean, professional, and interview-ready design  

---

## 🧠 System Architecture

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

yaml
Copy code

---

## 🛠️ Technologies Used

| Category | Technology |
|--------|-----------|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| NLP | TF-IDF |
| Model | Logistic Regression |
| Web UI | Streamlit |
| LLM (Optional) | OpenAI GPT |
| Serialization | Joblib |

---

## 📂 Project Structure

phishing_email_detector/
│
├── data/
│ └── emails.csv
│
├── model/
│ ├── model.pkl
│ └── vectorizer.pkl
│
├── train_model.py
├── predict_cli.py
├── app.py
├── requirements.txt
└── README.md

yaml
Copy code

---

## 📊 Dataset Information

- Public phishing email dataset (Kaggle)
- Email labels:
  - `1` → Phishing
  - `0` → Safe
- Contains real-world phishing and legitimate email samples

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
git clone https://github.com/your-username/phishing_email_detector.git
cd phishing_email_detector
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Train the Model
bash
Copy code
python train_model.py
This will generate:

model/model.pkl

model/vectorizer.pkl

🖥️ Usage
🔹 Command Line Interface (CLI)
bash
Copy code
python predict_cli.py
Paste email text → Get phishing result instantly.

🔹 Web Application (Streamlit)
bash
Copy code
python -m streamlit run app.py
Open browser → Paste email → Analyze → Get result with confidence.

🧠 LLM Integration (Optional)
This project supports Large Language Model (LLM) analysis for advanced reasoning and explainability.

Steps:
Create an OpenAI account

Generate an API key

Set environment variable (Windows):

powershell
Copy code
setx OPENAI_API_KEY "your_api_key_here"
Enable “Use LLM (Advanced Analysis)” checkbox in the UI

LLM Provides:
Phishing confirmation

Risk level

Short security explanation

📈 Model Performance
Lightweight and fast

Suitable for real-time detection

Works offline (ML-only mode)

LLM enhances explainability and decision quality

🔐 Security & Ethics
No email data is stored

API keys are secured via environment variables

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
