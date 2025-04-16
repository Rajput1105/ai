import streamlit as st
import os
import re
import google.generativeai as genai
from docx import Document
from PyPDF2 import PdfReader
import smtplib
from email.message import EmailMessage

# ---- CONFIG ----
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
EMAIL_SENDER = st.secrets["EMAIL_SENDER"]
EMAIL_PASSWORD = st.secrets["EMAIL_PASSWORD"]

RESUME_FOLDER = "uploaded_resumes"

# ---- FUNCTIONS ----
def extract_text(file):
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    elif file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join([p.text for p in doc.paragraphs])
    return ""

def analyze_resume(text, job_description):
    prompt = f"""
You're an AI resume reviewer.

Job Description:
{job_description}

Resume:
{text}

Extract the following:
1. Masked Name and Email
2. JD-CV Match Score (0-100)
3. Batch Year
4. AI-related experience summary
5. Resume Quality Score (0-100)
6. Feedback (strengths & weaknesses)
"""
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(prompt)
    return response.text

def extract_email(text):
    match = re.search(r"Email:\s*([^\s\n]+)", text)
    return match.group(1) if match else None

def extract_name(text):
    match = re.search(r"Name:\s*([^\n]+)", text)
    return match.group(1).split()[0] if match else "Candidate"

def send_email(to_email, subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = to_email
    msg.set_content(body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(msg)

# ---- STREAMLIT UI ----
st.title("📄 AI Resume Analyzer")

job_description = st.text_area("Enter Job Description", "Looking for candidates with experience in AI, ML, Python, and NLP.")

uploaded_files = st.file_uploader("Upload Resumes (.pdf or .docx)", type=["pdf", "docx"], accept_multiple_files=True)

send_email_option = st.checkbox("Send email feedback to candidate")

if uploaded_files:
    for file in uploaded_files:
        file_path = os.path.join(RESUME_FOLDER, file.name)
        os.makedirs(RESUME_FOLDER, exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(file.read())

        st.markdown(f"### Analysis for `{file.name}`")
        resume_text = extract_text(file)
        analysis = analyze_resume(resume_text, job_description)

        st.text_area("Resume Feedback", analysis, height=300)

        if send_email_option:
            candidate_email = extract_email(analysis)
            candidate_name = extract_name(analysis)
            if candidate_email:
                send_email(candidate_email, "Your Resume Feedback", f"Hi {candidate_name},\n\n{analysis}\n\nBest of luck!")
                st.success(f"✅ Email sent to {candidate_email}")
            else:
                st.error("❌ Email not found in analysis.")
