# ai-feedback-generator
# 🤖 AI Feedback Generator for Projects

Give your project report a smart review using Generative AI! This app analyzes PDF, DOCX, or PPTX files and provides:

- ✅ Strengths & Weaknesses
- ✅ Suggestions for Improvement
- ✅ Possible Viva Questions
- ✅ Multilingual Support: English, Tamil, Hindi
- ✅ Export options: PDF & PowerPoint Slides

Built using [Streamlit](https://streamlit.io), [Groq](https://groq.com), and LLMs.

---

## 📸 Demo

![App Screenshot](https://github.com/yourusername/ai-feedback-generator/assets/screenshot.gif)
![Uploading Screenshot_19-6-2025_21642_localhost.jpeg…]()

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| 📂 Upload Project File | Accepts `.pdf`, `.docx`, `.pptx` |
| 🗣️ Choose Tone | Friendly, Formal, or Critical feedback |
| 🌐 Language Options | English, Tamil, Hindi |
| 📝 Feedback & Viva | Instant AI-generated suggestions |
| 📥 Export | Download as PDF or PPTX presentation |

---

## 🛠 Tech Stack

- Python 🐍
- Streamlit 🧠
- Groq API (LLaMA 3 model)
- FPDF (PDF export)
- python-pptx (PowerPoint export)

---

## 🧑‍💻 Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/ai-feedback-generator.git
   cd ai-feedback-generator

2.Install dependencies:

pip install -r requirements.txt

3.Add your Groq API Key:
Create a .streamlit/secrets.toml file:

[default]
GROQ_API_KEY = "your_groq_api_key_here"

4.Run the app:

streamlit run app.py


📂 Project Structure
markdown
Copy
Edit
ai-feedback-generator/
├── app.py
├── requirements.txt
├── prompts/
│   └── feedback_prompt.txt
├── utils/
│   ├── extractors.py
│   └── slide_generator.py
└── .streamlit/
    └── secrets.toml
✨ Future Ideas
Text-to-speech feedback (in Tamil/Hindi)

Add more file types (images, code files)

Feedback accuracy grading

Shareable report links

📬 Contact
Built by Mohammed Jaasir
📧 jaasir@example.com
📍 SNS College of Engineering
🧠 Passionate about AI, Mobility, and Education!

📄 License
MIT License — free to use, adapt, and share.

Let me know if you want:
- A sample screenshot for the `![App Screenshot]` section
- This README saved as a file and zipped with your project
- Auto-deployment workflow (GitHub Actions + Streamlit)

You're building something truly useful — let’s make it shine!








