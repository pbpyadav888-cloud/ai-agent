import tkinter as tk
from tkinter import scrolledtext, messagebox

from deep_translator import GoogleTranslator
from openai import OpenAI
import pyttsx3

from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

try:
    engine = pyttsx3.init()
except Exception:
    engine = None


def translate_to_english(text: str) -> str:
    try:
        return GoogleTranslator(source="auto", target="en").translate(text)
    except Exception:
        return text


def ask_ai(question: str) -> str:
    translated = translate_to_english(question)
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful AI assistant."},
                {"role": "user", "content": translated},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error contacting OpenAI: {e}"


def speak(text: str) -> None:
    if engine:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception:
            pass


def on_ask():
    user_text = input_box.get("1.0", tk.END).strip()
    if not user_text:
        messagebox.showinfo("Jarvis", "Please type something to ask.")
        return

    ask_button.config(state=tk.DISABLED)
    root.update_idletasks()

    answer = ask_ai(user_text)
    output_box.configure(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, answer)
    output_box.configure(state=tk.DISABLED)

    # Optional: also speak the answer
    speak(answer)

    ask_button.config(state=tk.NORMAL)


root = tk.Tk()
root.title("Jarvis Assistant")
root.geometry("700x500")

input_label = tk.Label(root, text="Ask Jarvis (any language):")
input_label.pack(anchor="w", padx=10, pady=(10, 0))

input_box = scrolledtext.ScrolledText(root, height=5, wrap=tk.WORD)
input_box.pack(fill="both", expand=False, padx=10, pady=5)

ask_button = tk.Button(root, text="Ask", command=on_ask)
ask_button.pack(pady=5)

output_label = tk.Label(root, text="Jarvis answer:")
output_label.pack(anchor="w", padx=10, pady=(10, 0))

output_box = scrolledtext.ScrolledText(root, height=10, wrap=tk.WORD, state=tk.DISABLED)
output_box.pack(fill="both", expand=True, padx=10, pady=5)

root.mainloop()

