import speech_recognition as sr
import pyttsx3
import subprocess
import webbrowser
import pyautogui
import psutil
import requests
from deep_translator import GoogleTranslator
from openai import OpenAI

from config import OPENAI_API_KEY

client = OpenAI(
    api_key=OPENAI_API_KEY
)

# ==============================
# TEXT TO SPEECH
# ==============================

engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# ==============================
# SPEECH RECOGNITION
# ==============================

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        return ""

# ==============================
# TRANSLATE TO ENGLISH
# ==============================

def translate_to_english(text):
    try:
        translated = GoogleTranslator(source='auto', target='en').translate(text)
        return translated
    except:
        return text

# ==============================
# ASK OPENAI
# ==============================

def ask_ai(question):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Jarvis, a helpful AI assistant."},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content

# ==============================
# PC CONTROL
# ==============================

def open_application(app):

    if "chrome" in app:
        subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif "notepad" in app:
        subprocess.Popen("notepad")

    elif "calculator" in app:
        subprocess.Popen("calc")

    else:
        speak("Application not found")

# ==============================
# COMMAND PROCESSOR
# ==============================

def process_command(command):

    command_en = translate_to_english(command)

    if "open youtube" in command_en:
        webbrowser.open("https://youtube.com")

    elif "open google" in command_en:
        webbrowser.open("https://google.com")

    elif "open chrome" in command_en:
        open_application("chrome")

    elif "open notepad" in command_en:
        open_application("notepad")

    elif "open calculator" in command_en:
        open_application("calculator")

    elif "shutdown computer" in command_en:
        speak("Shutting down")
        subprocess.call("shutdown /s /t 5")

    elif "restart computer" in command_en:
        speak("Restarting")
        subprocess.call("shutdown /r /t 5")

    elif "screenshot" in command_en:
        img = pyautogui.screenshot()
        img.save("screenshot.png")
        speak("Screenshot saved")

    else:
        answer = ask_ai(command)
        speak(answer)

# ==============================
# MAIN LOOP
# ==============================

def main():

    speak("Hello, I am Jarvis. How can I help you?")

    while True:

        command = listen()

        if command == "":
            continue

        if "exit" in command or "stop jarvis" in command:
            speak("Goodbye")
            break

        process_command(command)


if __name__ == "__main__":
    main()