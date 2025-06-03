# 🤖 Jarvis – AI Virtual Assistant in Python

Welcome to **Jarvis**, a Python-based AI voice assistant developed as a final year project. This assistant performs a variety of intelligent tasks triggered by your **voice commands**, including speaking responses, opening applications, fetching weather updates, generating passwords, and even interacting with WhatsApp.

---

## 🚀 Features

- 🗣️ **Text to Speech (TTS)** using `pyttsx3`
- 🎙️ **Custom Voice Selection** (Male/Female)
- ⏰ **Date & Time Announcement**
- 👋 **Personalized Greeting & Wishing**
- 📲 **Send WhatsApp Messages** via browser automation
- 🔍 **Search on Wikipedia & Google**
- 📺 **Play YouTube Videos** via `pywhatkit`
- 🌦️ **Get Live Weather Updates** using OpenWeatherMap API
- 📰 **Fetch News Headlines** using NewsAPI
- 📋 **Read Selected Text** from clipboard (`clipboard`)
- 📂 **Open Applications & Folders** (e.g., VS Code, Downloads)
- 😂 **Tell Random Jokes** using `pyjokes`
- 🖼️ **Take Screenshots** using `pyautogui`
- 🧠 **Remember Information** (Save & Recall Notes)
- 🔐 **Password Generator** (Randomized secure password)
- 🎲 **Flip a Coin / Roll a Dice**
- ⚡ **CPU & Battery Status Monitor** using `psutil`
- 💤 **Wake Word Detection** using `nltk`

---

## 🛠️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Jarvis-AI-Assistant.git
cd Jarvis-AI-Assistant
```

### 2. Install Dependencies

Install all required libraries:

```bash
pip install -r requirements.txt
```

Or install manually if `requirements.txt` is not provided:

```bash
pip install pyttsx3 pyautogui wikipedia pywhatkit requests clipboard newsapi-python pyjokes psutil nltk
```

### 3. Setup API Keys

- 🔑 **[OpenWeatherMap API](https://openweathermap.org/)**
- 🔑 **[News API](https://newsapi.org/)**

Update the keys in the script wherever applicable.

### 4. Run the Assistant

```bash
python Jarvis.py
```

---

## 📁 Folder Structure

```text
Jarvis-AI-Assistant/
├── Jarvis.py                # Main voice assistant logic
├── data.txt                 # Memory file for 'remember' feature
├── /screenshots             # Folder to store captured screenshots
├── requirements.txt         # List of dependencies
├── README.md                # Project documentation (this file)
└── ...
```

---

## 🧰 Tools & Technologies

- **Python 3.x**
- **Visual Studio Code**
- **Wallpaper Engine** (for UI simulation)

---

## 🔮 Future Enhancements

- 📡 Integration with **IoT Devices** (Smart Home control)
- 🖥️ GUI support using **Tkinter** or **PyQt5**
- 🤖 Improved NLP using **Transformers**
- 📈 Real-time **Sentiment Analysis**

---

## 👨‍💻 Developed By

**Rajesh Kumar Jogi**

Final Year Project for B.Tech/B.Sc in Computer Science

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 🙌 Feedback & Contributions

Have suggestions or want to improve Jarvis?  
You're welcome to **fork**, **submit pull requests**, or **open issues** in this repository.

Let's build the future together! 💡
