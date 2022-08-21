import PyPDF2
import pyttsx3

with open('file.pdf', 'rb') as file:
    pdfReader = PyPDF2.PdfFileReader(file)
    page = pdfReader.getPage(7)
    text = page.extractText()
    speak = pyttsx3.init()
    voices = speak.getProperty('voices')
    speak.setProperty("rate", 178)
    speak.setProperty('voice', voices[3].id)
    speak.say(text)
    speak.runAndWait()

