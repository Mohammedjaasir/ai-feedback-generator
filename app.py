import streamlit as st
import os
from utils.extractors import extract_text_from_pdf, extract_text_from_docx, extract_text_from_pptx
from utils.slide_generator import create_feedback_slides
import requests
from fpdf import FPDF
from random import choice
import json

# Load prompt template
def load_prompt():
    with open("prompts/feedback_prompt.txt", "r", encoding="utf-8") as file:
        return file.read()

# Query Groq with feedback tone + language
def query_groq(text, tone="formal", language="English"):
    prompt_template = load_prompt()
    base_prompt = prompt_template.replace("{{TEXT}}", text[:3000]).replace("{{TONE}}", tone)
    language_instruction = f"Please write the entire response in {language} only. Do not use English if {language} is selected."

    headers = {
        "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": f"You are an expert evaluator who always replies in {language}."},
            {"role": "user", "content": base_prompt + "\n\n" + language_instruction}
        ]
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)

    try:
        result = response.json()
        if "choices" in result:
            return result["choices"][0]["message"]["content"]
        else:
            st.error("❌ Groq API returned an error:\n" + json.dumps(result, indent=2))
            return "Groq API error: Check your model name or input."
    except Exception as e:
        st.error("⚠️ Failed to read response from Groq.")
        st.text(response.text)
        return "Something went wrong."

# Export feedback to PDF
def export_to_pdf(text, filename="AI_Feedback.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)
    pdf.output(filename)
    return filename

# Streamlit UI
st.set_page_config("AI Feedback Generator")
st.title("📊 AI Feedback Generator")
st.write("Upload your project file to get feedback, viva questions, and improvement ideas — now in English, Tamil, or Hindi!")

uploaded_files = st.file_uploader("📂 Upload your project file(s)", type=["pdf", "docx", "pptx"], accept_multiple_files=True)
feedback_tone = st.selectbox("🗣️ Choose feedback tone", ["formal", "friendly", "critical"])
feedback_language = st.selectbox("🌐 Choose language", ["English", "Tamil", "Hindi"])

if uploaded_files:
    all_text = ""
    for uploaded_file in uploaded_files:
        if uploaded_file.name.endswith(".pdf"):
            content = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.name.endswith(".docx"):
            content = extract_text_from_docx(uploaded_file)
        elif uploaded_file.name.endswith(".pptx"):
            content = extract_text_from_pptx(uploaded_file)
        else:
            st.error(f"Unsupported file type: {uploaded_file.name}")
            continue
        all_text += content + "\n"

    with st.spinner("🔍 Generating feedback using Groq..."):
        feedback = query_groq(all_text, tone=feedback_tone, language=feedback_language)

    st.subheader("📝 AI Feedback")
    st.text_area("Full Feedback", feedback, height=400)

    # Smart improvement prompts
    improvement_prompts = [
        f"Here is a project: \n---\n{all_text[:3000]}\n---\nSuggest three advanced features that make it real-world ready.",
        f"Here is a project: \n---\n{all_text[:3000]}\n---\nHow can it be scaled for enterprise use?",
        f"Here is a project: \n---\n{all_text[:3000]}\n---\nSuggest how to integrate AI or ML into it.",
        f"Here is a project: \n---\n{all_text[:3000]}\n---\nPropose a startup idea based on this project.",
        f"Here is a project: \n---\n{all_text[:3000]}\n---\nRecommend smart sensors, APIs or tools to improve it."
    ]
    random_prompt = choice(improvement_prompts)

    with st.spinner("💡 Generating improvement ideas..."):
        improvement_ideas = query_groq(random_prompt, tone=feedback_tone, language=feedback_language)

    st.subheader("💡 Project Improvement Ideas")
    st.text_area("Development Suggestions", improvement_ideas, height=300)

    if st.button("📄 Export as PDF"):
        pdf_name = export_to_pdf(feedback + "\n\nProject Improvement Ideas:\n" + improvement_ideas)
        with open(pdf_name, "rb") as f:
            st.download_button("📥 Download PDF", f, file_name=pdf_name)

    if st.button("📽️ Generate PPT Slides"):
        with st.spinner("🎞️ Creating PowerPoint..."):
            pptx_file = create_feedback_slides(feedback, improvement_ideas)
            with open(pptx_file, "rb") as f:
                st.download_button("📥 Download PPTX", f, file_name=pptx_file)
