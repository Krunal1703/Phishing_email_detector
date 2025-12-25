import streamlit as st
import joblib
import os
from openai import OpenAI

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Phishing Email Detector",
    page_icon="🛡️",
    layout="centered"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

# ---------------- LOAD OPENAI CLIENT ----------------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def llm_phishing_check(email_text):
    """
    Uses LLM to analyze phishing risk with reasoning
    """
    prompt = f"""
You are a cybersecurity expert.

Analyze the email below and answer clearly:
1. Is it phishing? (Yes or No)
2. Risk Level (Low / Medium / High)
3. Short reason (1–2 lines)

Email:
{email_text}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a cybersecurity analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content

# ---------------- SIDEBAR ----------------
st.sidebar.title("🛡️ Navigation")
page = st.sidebar.radio(
    "Select Page",
    ["Email Analyzer", "About Project"]
)

# ==================================================
#                  EMAIL ANALYZER
# ==================================================
if page == "Email Analyzer":

    st.title("AI-Powered Phishing Email Detector")
    st.write(
        "Analyze email content using **Machine Learning** and optional **LLM-based security analysis**."
    )

    email_text = st.text_area(
        "📧 Paste Email Content",
        height=220,
        placeholder="Paste the complete email message here..."
    )

    use_llm = st.checkbox("🧠 Use LLM (Advanced Analysis)")

    col1, col2 = st.columns(2)
    with col1:
        analyze = st.button("🔍 Analyze Email")
    with col2:
        clear = st.button("🧹 Clear")

    if clear:
        st.rerun()

    if analyze:
        if email_text.strip() == "":
            st.warning("Please paste email content before analyzing.")
        else:
            # ---------- ML ANALYSIS ----------
            features = vectorizer.transform([email_text])
            prediction = model.predict(features)[0]
            probability = model.predict_proba(features)[0]

            phishing_prob = probability[1] * 100
            safe_prob = probability[0] * 100

            st.markdown("---")
            st.subheader("🧪 Machine Learning Result")

            if prediction == 1:
                st.error("⚠️ Suspicious Email Detected (Phishing)")
                if phishing_prob > 80:
                    risk = "HIGH"
                elif phishing_prob > 50:
                    risk = "MEDIUM"
                else:
                    risk = "LOW"

                st.write(f"**Risk Level:** {risk}")
                st.write(f"**Phishing Confidence:** {phishing_prob:.2f}%")
            else:
                st.success("✅ Email Looks Safe")
                st.write(f"**Safety Confidence:** {safe_prob:.2f}%")

            # ---------- LLM ANALYSIS ----------
            if use_llm:
                st.markdown("---")
                st.subheader("🧠 LLM Security Analysis")
                with st.spinner("LLM is analyzing the email..."):
                    try:
                        llm_result = llm_phishing_check(email_text)
                        st.info(llm_result)
                    except Exception as e:
                        st.error("LLM analysis failed. Check API key or internet.")

            st.markdown("---")
            st.caption(
                "⚠️ This system provides probabilistic analysis. Always verify suspicious emails manually."
            )

# ================= ABOUT PROJECT =================
elif page == "About Project":
    st.title("📘 About This Project")

    st.markdown("""
### AI-Powered Phishing Email Detector

**Objective**  
Detect phishing emails using Machine Learning and Large Language Models.

**Technologies Used**
- Python
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Streamlit
- OpenAI GPT

**How It Works**
1. Email text preprocessing
2. TF-IDF feature extraction
3. ML-based phishing prediction
4. Optional LLM reasoning
5. Final verdict with confidence

**Use Cases**
- Cybersecurity awareness
- Email filtering
- Academic & internship projects

**Disclaimer**
This tool assists detection and does not replace human judgment.
""")


    st.info("Developed as an advanced cybersecurity ML + LLM project.")
