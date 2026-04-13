# 📌 Django Text-to-Speech Web App

## 🚀 Project Overview
This is a web-based Text-to-Speech application built using the Django framework.  
It converts user input text into speech and generates an audio file that can be played in the browser.

---

## ✨ Features
- Convert text into speech in real time
- Audio playback in browser
- Generates and stores MP3 audio file
- Simple and user-friendly interface
- Fast and lightweight processing

---

## 🛠️ Tech Stack
- Backend: Django (Python)
- Speech Engine: gTTS (Google Text-to-Speech)
- Frontend: HTML
- Database: SQLite (default Django DB)

---

## 📁 Project Structure
Django_TextToSpeech_Project/
│
├── tts_project/
├── tts_app/
│   ├── templates/
│   ├── views.py
│   └── urls.py
│
├── manage.py
├── requirements.txt
└── media/

---

## ⚙️ Installation & Setup

### 1. Clone repository
git clone https://github.com/your-username/Django_Text_to_Speech.git
cd Django_Text_to_Speech

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run migrations
python manage.py migrate

### 5. Start server
python manage.py runserver

### 6. Open in browser
http://127.0.0.1:8000/

---

## 📌 How it Works
- User enters text in input box
- Django processes the request
- gTTS converts text into speech
- MP3 file is generated and saved
- Audio is played in browser

---

## 🔮 Future Improvements
- Multi-language support (Hindi, Maithili)
- Voice speed control
- Download button for audio
- Better UI using Bootstrap or React
- User login system

---

## 👨‍💻 Author
Pushpak Pranav  
GitHub: https://github.com/PushpakPranav  

---

## 📜 License
This project is for educational purposes only.
