# 🧑‍🌾 Farmer Bot – Backend

This is the backend logic for the **Farmer Chatbot** that helps farmers with answers about agriculture, fertilizers, animal care, and government schemes. It supports multiple languages like Telugu, Hindi, and English.

---

## 🌐 Tech Stack

- **Python** + **Flask** – Web server
- **Flask-CORS** – Enable frontend-backend communication
- **RapidFuzz** – Fuzzy keyword matching
- **LangDetect** – Language detection
- **Deep Translator** – Multilingual translation

---

## 📁 File Structure

farmer-bot-backend/
│
├── app.py # Flask app and routing
├── chatbot_logic.py # Main chatbot logic
├── faq_data.json # Question-answer dataset
├── requirements.txt # All dependencies
└── README.md # This file

---
bash
git clone https://github.com/YOUR_USERNAME/farmer-bot-backend.git
cd farmer-bot-backend
## 🚀 How to Run Locally

### Step 1: Clone the Repo
     
Step 2: Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On Linux/Mac
Step 3: Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
Step 4: Run the App
bash
Copy
Edit
python app.py
App runs on: http://127.0.0.1:5000

🌍 API Endpoint
/get?msg=YOUR_MESSAGE → Returns JSON with chatbot reply

Example:

bash
Copy
Edit
curl http://127.0.0.1:5000/get?msg=What is best fertilizer for tomatoes
🌐 Deployment
This backend is ready to deploy on:

✅ Render.com

✅ Railway.app

✅ Any Flask-compatible hosting

Make sure requirements.txt is up-to-date and port 5000 is exposed.

👨‍🌾 Sample Questions
"When should I plant rice?"

"Pests control for cotton?"

"ఎరువుల సమాచారం ఇవ్వండి"

"सरकार की योजना क्या है?"

Supports English, తెలుగు, हिन्दी!

📞 Contact
Created by Dhanush Srinivasulu
📧 srinivasuludhanush2006@gmail.com
🌱 Built with ❤️ for Indian farmers.

yaml
Copy
Edit

---

Let me know if you want me to generate:
- ✅ `.gitignore`
- ✅ `Procfile`
- ✅ `requirements.txt`

For easy deployment on Render or Railway.

