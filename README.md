# Language Translator with Voice Assistant

This project is a language translator tool built using Python and Tkinter. It allows users to translate text from one language to another using the Google Translate API. Additionally, the project supports speech-to-text and text-to-speech functionalities, enabling users to input text by speaking and hear the translation through a voice assistant.

## Features
- **Text Translation**: Translates text from one language to another using the Google Translate API.
- **Voice Input**: Users can speak and have their speech automatically converted to text.
- **Voice Output**: After translation, the result is read out loud using a voice assistant.
- **Language Selection**: Dropdown to choose from a wide range of available languages for translation.

## Technologies Used
- **Python**: The core programming language used to build the project.
- **Tkinter**: A Python library for creating the graphical user interface (GUI).
- **Googletrans**: A free Python library that uses Google Translate API for translating text.
- **SpeechRecognition**: A Python library to recognize speech and convert it to text.
- **pyttsx3**: A text-to-speech conversion library in Python.

## Prerequisites

To run this project, you will need to have the following Python libraries installed:

```bash
pip install googletrans==4.0.0-rc1
pip install speechrecognition
pip install pyttsx3
