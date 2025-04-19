# Ai Link to Deployment https://cuzw6obmhuehxa6bpk4pnw.streamlit.app/
## 🧠 AI Resume Analyzer with Gemini & Streamlit

This project allows you to **analyze resumes** (PDF or DOCX) and compare them against a **Job Description (JD)** using **Google's Gemini AI**, with results including:

- JD-CV Match Score
- AI-related Experience Summary
- Resume Quality Score
- Strengths & Weaknesses Feedback
- Optional Email Feedback Delivery

Built with **Streamlit** for an easy-to-use web interface.

---

### 🚀 Features
- 🔍 Extracts text from PDF/DOCX resumes
- 🤖 Uses Gemini AI to analyze resumes based on a given JD
- 📊 Returns detailed insights (match score, batch year, resume quality, etc.)
- 📧 Sends feedback via email (optional)
- 🧾 Clean and simple Streamlit UI

---

### 🛠️ Tech Stack
- Python
- Streamlit
- Google Generative AI (`google-generativeai`)
- PyPDF2 / python-docx
- Gmail SMTP (optional email sending)

---

### 📂 Folder Structure
```
├── app.py                   # Main Streamlit app
├── requirements.txt         # All dependencies
├── /resumes                 # Folder to upload resumes (PDF/DOCX)
└── README.md                # You're here!
```

---

### ✅ Setup Instructions

#### 1. Clone the Repo
```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

#### 2. Install Requirements
```bash
pip install -r requirements.txt
```

#### 3. Add Streamlit Secrets

Create a file called `.streamlit/secrets.toml` with:

```toml
GEMINI_API_KEY = "your_gemini_api_key"
EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_email_app_password"
```

---

### ▶️ Run the App
```bash
streamlit run app.py
```

---

### 🌐 Deployment on Streamlit Cloud

1. Push code to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and connect your GitHub repo
3. Add the same secrets in **Settings > Secrets**
4. Deploy and share your app URL!

---

### 📬 Sample Output

```
**Name:** [Masked]
**Email:** [Masked]

**Match Score:** 85
**Resume Score:** 78
**AI Summary:** Hands-on with NLP, LLM, OpenCV, Watson, etc.
**Strengths:** Projects, IIT background, learning mindset
**Weaknesses:** Minor formatting & grammar issues
```

---

### 🙌 Credits

Made with ❤️ by Rahul Raj Singh
Powered by Google Gemini & Streamlit
