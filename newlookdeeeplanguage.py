from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
from langdetect import detect
import pyttsx3

# Text-to-Speech Engine
engine = pyttsx3.init()

# Translation History
history = []


def translate():
    try:
        text = input_text.get("1.0", END).strip()

        if not text:
            messagebox.showerror("Error", "Please enter text")
            return

        # Detect language
        detected = detect(text)
        detected_label.config(text=f"Detected Language: {detected}")

        src_code = languages[source_lang.get()]
        dest_code = languages[target_lang.get()]

        translated = GoogleTranslator(
            source=src_code,
            target=dest_code
        ).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

        # Save History
        record = f"{source_lang.get()} → {target_lang.get()} : {translated}"
        history.append(record)
        history_box.insert(END, record)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def speak():
    text = output_text.get("1.0", END).strip()

    if text:
        engine.say(text)
        engine.runAndWait()


def copy_text():
    text = output_text.get("1.0", END).strip()

    root.clipboard_clear()
    root.clipboard_append(text)

    messagebox.showinfo("Copied", "Translated text copied!")


# Main Window
root = Tk()
root.title("Advanced Language Translation Tool")
root.geometry("850x700")
root.configure(bg="#1e1e1e")

# Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}

# Title
Label(
    root,
    text="🌍 Advanced Language Translation Tool",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 20, "bold")
).pack(pady=10)

# Input
Label(
    root,
    text="Enter Text",
    bg="#1e1e1e",
    fg="white"
).pack()

input_text = Text(root, height=6, width=80)
input_text.pack(pady=5)

# Language Selection
frame = Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

Label(
    frame,
    text="Source Language",
    bg="#1e1e1e",
    fg="white"
).grid(row=0, column=0, padx=20)

source_lang = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    width=15
)
source_lang.current(0)
source_lang.grid(row=1, column=0)

Label(
    frame,
    text="Target Language",
    bg="#1e1e1e",
    fg="white"
).grid(row=0, column=1, padx=20)

target_lang = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    width=15
)
target_lang.current(1)
target_lang.grid(row=1, column=1)

# Translate Button
Button(
    root,
    text="Translate",
    command=translate,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold")
).pack(pady=10)

# Detected Language
detected_label = Label(
    root,
    text="Detected Language: ",
    bg="#1e1e1e",
    fg="cyan",
    font=("Arial", 10, "bold")
)
detected_label.pack()

# Output
Label(
    root,
    text="Translated Text",
    bg="#1e1e1e",
    fg="white"
).pack()

output_text = Text(root, height=6, width=80)
output_text.pack(pady=5)

# Buttons Frame
btn_frame = Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=10)

Button(
    btn_frame,
    text="🔊 Speak",
    command=speak,
    bg="#2196F3",
    fg="white"
).grid(row=0, column=0, padx=10)

Button(
    btn_frame,
    text="📋 Copy",
    command=copy_text,
    bg="#FF9800",
    fg="white"
).grid(row=0, column=1, padx=10)

# History
Label(
    root,
    text="Translation History",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 12, "bold")
).pack(pady=5)

history_box = Listbox(
    root,
    width=100,
    height=10
)
history_box.pack(pady=5)

root.mainloop()