# Jarvis Voice & GUI Assistant

This project is a simple desktop assistant called **Jarvis**. It can:

- Listen to your voice through the microphone
- Understand commands in **any language** and translate them to English
- Open common websites and Windows apps
- Take screenshots
- Ask DeepSeek AI (`deepseek-chat`) for answers and speak them back
- (Optional frontend) Let you type questions in a small GUI and see/speak the answers

---

## 1. Setup

### 1.1. Install Python

Make sure you have **Python 3.9+** installed and added to PATH.

### 1.2. Create/activate a virtual environment (recommended)

On Windows PowerShell:

```powershell
cd "c:\Users\p.bhanu prasad yadav\OneDrive\Desktop\own ai"
python -m venv .venv
.venv\Scripts\activate
```

### 1.3. Install dependencies

```powershell
pip install -r requirements.txt
```

You may need additional audio backends on Windows (e.g. microphone drivers). If `PyAudio` fails to install from source, you can install a prebuilt wheel.

---

## 2. Configure DeepSeek API key

Open `AI.py` and set:

```python
DEEPSEEK_API_KEY = "YOUR_REAL_API_KEY_HERE"
```

You must replace the placeholder string; otherwise the AI chat calls will fail.

---

## 3. Running Jarvis (voice mode)

From the project folder:

```powershell
cd "c:\Users\p.bhanu prasad yadav\OneDrive\Desktop\own ai"
.venv\Scripts\activate  # if using venv
python AI.py
```

Jarvis will:

1. Say: **"Hello, I am Jarvis. How can I help you?"**
2. Listen for your voice.
3. Execute commands such as:
   - **"open youtube"** → opens YouTube in your browser
   - **"open google"** → opens Google
   - **"open chrome"**, **"open notepad"**, **"open calculator"**
   - **"screenshot"** → saves `screenshot.png` in this folder
   - **"shutdown computer"**, **"restart computer"** (be careful)
4. If your request doesn’t match a built-in command, it will send it to **DeepSeek AI** and **speak the answer**.

To stop Jarvis, say:

- **"exit"** or
- **"stop jarvis"**

---

## 4. GUI Frontend (text mode)

This project also includes a small optional GUI (if you choose to use it) that:

- Lets you type questions/commands instead of speaking
- Shows Jarvis’s answer in a text box
- Uses the same DeepSeek backend as the voice mode

To run the GUI (after installing requirements and setting the API key):

```powershell
python gui.py
```

The window will open. Type a question (any language) and press **Ask**. Jarvis will:

1. Translate your text to English
2. Call DeepSeek
3. Display the answer (and optionally speak it)

---

## 5. Notes and safety

- **System commands** like shutdown and restart are powerful. Only use them when you really intend to.
- Microphone quality and background noise will affect recognition accuracy.
- DeepSeek usage is subject to your API quota and network connectivity.

---

## 6. Files overview

- `AI.py` – main voice-based Jarvis assistant.
- `gui.py` – simple GUI frontend for text interaction with Jarvis.
- `requirements.txt` – Python dependencies.
- `README.md` – this documentation.

