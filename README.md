# 🧠 AI Feedback Generator for Academic Projects

Ever wished you had a mentor who could instantly review your project report, suggest improvements, and prepare you for viva questions?  
This tool does exactly that — powered by Generative AI.

---

## 🚀 What is This?

**AI Feedback Generator** is a Streamlit-based web app that takes in your project document — PDF, DOCX, or PPTX — and gives back:

- ✅ Clear, structured feedback on your project  
- 💡 Smart improvement suggestions and upgrade ideas  
- 🎯 Auto-generated viva questions  
- 🌐 Multilingual support (English, Tamil, Hindi)  
- 📄 Downloadable reports in PDF and PowerPoint formats  

---

## ✨ Why I Built This

As an AI enthusiast and engineering student, I noticed that many students (including myself) struggle to get timely, quality feedback on their projects.  
So I thought — what if we could use GenAI not just to write code, but to think like a teacher?

---

## 🖼️ Preview
![Screenshot_19-6-2025_21642_localhost](https://github.com/user-attachments/assets/724d1f75-9a2d-4348-bfd1-c2a9e2f3c56d)



---

## 🔧 Features at a Glance

| Feature                  | Description                                                 |
|--------------------------|-------------------------------------------------------------|
| 📁 Upload Projects        | Accepts `.pdf`, `.docx`, `.pptx` files                     |
| 🎭 Tone Customization     | Choose feedback tone: formal, friendly, or critical         |
| 🌍 Multilingual Output    | Output in English, Tamil, or Hindi                          |
| 📄 Export Options         | Download as PDF or well-formatted PowerPoint slides         |
| 🎓 Viva Ready             | Auto-suggested viva questions based on your content         |
| ⚡ Powered by Groq        | Uses LLaMA 3 on Groq for fast and smart feedback            |

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **AI Backend:** Groq API (LLaMA 3)  
- **Document Parsing:** pdfplumber, python-docx, python-pptx  
- **Report Generation:** FPDF & python-pptx  
- **Languages:** Python 🐍  

---

## 📂 Folder Structure

ai-feedback-generator/
├── app.py
├── requirements.txt
├── prompts/
│ └── feedback_prompt.txt
├── utils/
│ ├── extractors.py
│ └── slide_generator.py
├── assets/
│ └── screenshot.png
└── .streamlit/
└── secrets.toml
