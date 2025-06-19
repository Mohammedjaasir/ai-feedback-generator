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

'''
ai-feedback-generator/
├── app.py                      # Main Streamlit app
├── requirements.txt            # Python dependencies

├── prompts/
│   └── feedback_prompt.txt     # AI prompt template

├── utils/
│   ├── extractors.py           # Text extraction from PDF, DOCX, PPTX
│   └── slide_generator.py      # PowerPoint slide generation

├── assets/
│   └── screenshot.png          # UI screenshot for README

└── .streamlit/
    └── secrets.toml            # (Not pushed to GitHub) contains Groq API key
'''


---

## 🧑‍💻 Getting Started

### 1. Clone this repo

git clone https://github.com/yourusername/ai-feedback-generator.git
cd ai-feedback-generator

## 2. Install dependencies

pip install -r requirements.txt

##3. Add your Groq API Key

Create a .streamlit/secrets.toml file:
GROQ_API_KEY = "your_groq_api_key_here"

##4. Run the app

streamlit run app.py

💡 Future Upgrades
🎤 Add voice feedback in Tamil or Hindi

🧠 Let the AI grade the project (A/B/C)

📊 Track student submissions with history

🕵️‍♂️ Add plagiarism checker

🙋‍♂️ Author
Mohammed Jaasir
Engineering student at SNS College of Engineering
📫 Connect on LinkedIn | Email me


📜 License
This project is open-source under the MIT License.

“Don’t just build projects. Build tools that help others build better.”
## ✅ How It's Unique

- Speaks with your **voice** and purpose
- Shows your **intention** behind building it
- Lists **practical use cases** and **future ideas**
- Impresses anyone reviewing your GitHub or resume

