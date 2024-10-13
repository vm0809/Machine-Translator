from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the Translator
translator = Translator()

# Tkinter root setup
root = Tk()
root.geometry('1100x320')
root.resizable(0, 0)
root['bg'] = '#03fcf0'
root.title('Language translator by NLP IE')

# Title Label
Label(root, text="NLP IE", font="Arial 20 bold").pack()

# Input text label and entry field
Label(root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=165, y=90)
Input_text = Entry(root, width=60)
Input_text.place(x=30, y=130)

# Output text label and text area
Label(root, text="Output", font='arial 13 bold', bg='white smoke').place(x=780, y=90)
Output_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=50)
Output_text.place(x=600, y=130)

# Language selection dropdown
languge = list(LANGUAGES.values())
dest_langs = ttk.Combobox(root, values=languge, width=22)
dest_langs.place(x=130, y=160)
dest_langs.set('choose language')

# Function to convert speech to text
def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            Input_text.delete(0, END)
            Input_text.insert(END, text)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service")

# Translate function
def Translate():
    translator = Translator()
    translated = translator.translate(text=Input_text.get(), dest=dest_langs.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
    
    # Speak the translated text
    engine.say(translated.text)
    engine.runAndWait()

# Translate button
trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='orange', activebackground='green')
trans_btn.place(x=445, y=180)

# Voice input button
voice_btn = Button(root, text='Speak', font='arial 12 bold', pady=5, command=voice_input, bg='blue', activebackground='yellow')
voice_btn.place(x=320, y=180)

# Start the Tkinter main loop
root.mainloop()
