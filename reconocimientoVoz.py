from email.mime import audio

from pkg_resources import UnknownExtra
import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()

while True:

    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.8)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio, language="es")
            text = text.lower()

            print(f"Usted dijo:  {text}")

    except speech_recognition.UnknownValueError():

        recognizer = speech_recognition.Recognizer()
        continue
