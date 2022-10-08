#Programa para crear un audiolibro

import pyttsx3
import PyPDF2 # pip install PyPDF2

with open('firstAudioBookV.0.1.pdf','rb') as book:

    full_text = ""

    reader = PyPDF2.PdfFileReader(book)

    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate",200)
    volume = audio_reader.getProperty("volume")
    audio_reader.setProperty("volume",1)

    for page in range(reader.numPages):
        next_page = reader.getPage(page)
        content = next_page.extractText()
        full_text += content
    
    audio_reader.save_to_file(full_text, "myfirstaudiobook.mp3")
    audio_reader.runAndWait()
