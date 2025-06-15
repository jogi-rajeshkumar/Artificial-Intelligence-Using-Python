
# 🤖 Jarvis - AI Virtual Assistant in Python

Jarvis is a beginner-friendly AI assistant created using Python. It interacts with users via voice commands and performs various tasks like reading news, sending WhatsApp messages, telling the weather, playing YouTube videos, and more. It uses Python libraries such as `pyttsx3`, `pyautogui`, `wikipedia`, and `pywhatkit` to deliver these features.

---

## 🎥 Demo

▶️ [Watch the Demo on YouTube](https://youtu.be/aX8kxh4e52k)  
  
---

## 🧠 Features

- ✅ Text-to-Speech
- ⏰ Tell Time and Date
- 👋 Greetings Based on Time of Day
- 💬 Send WhatsApp Messages
- 📖 Wikipedia Search
- 🔎 Google Search
- ▶️ YouTube Video Playback
- 🌤️ Live Weather Updates
- 🗞️ News Headlines via News API
- 📋 Read Clipboard Text
- 📁 Open Apps and Folders
- 😂 Jokes with PyJokes
- 📸 Take Screenshots
- 🧠 Remember Things for You
- 🔐 Password Generator
- 🎲 Flip Coin and Roll Dice
- 🔋 CPU and Battery Monitoring
- 🛎 Wake Word Detection (e.g., "Jarvis")

---

## 🛠 Setup Instructions

### 1. Prerequisites

- Python 3.x
- Visual Studio Code or any code editor
- Internet Connection for API access

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/Jarvis-AI-Assistant.git
cd Jarvis-AI-Assistant
```

### 3. Install Dependencies

```bash
pip install pyttsx3 pyautogui wikipedia pywhatkit clipboard newsapi-python pyjokes psutil nltk
```

Then run in Python shell:

```python
import nltk
nltk.download('punkt')
```

---

## 🔑 API Configuration

### OpenWeatherMap API

- Sign up at https://openweathermap.org
- Get your API key and replace it in the code where weather data is fetched

### NewsAPI

- Register at https://newsapi.org
- Replace the placeholder key in the `news()` function

---

## 🚀 How to Run

1. Replace API keys in the script
2. Run the script:

```bash
python Jarvis.py
```

Say commands like:

- "Jarvis, what's the weather in London?"
- "Jarvis, tell me a joke"
- "Jarvis, open VS Code"
- "Jarvis, search YouTube for relaxing music"

---

## 📂 Project Structure

```
Jarvis/
├── Jarvis.py
├── data.txt
├── README.md
└── requirements.txt (optional)
```

---

## 🗣️ Customization

- Change voice: Use `getvoices(1)` for male or `getvoices(2)` for female
- Modify `wakeword` from "Jarvis" to any keyword of your choice
- Add more voice commands using `elif` blocks
- Optional UI can be built using libraries like `tkinter` or `PyQt`

---

## 📜 License

This project is open for learning and personal use. Do not use it commercially without permission.

---

## 👨‍💻 Author

Built with ❤️ using Python.

---
