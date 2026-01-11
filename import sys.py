import sys
import wave
import threading
import time
import speech_recognition as sr
import matplotlib.pyplot as plt
import pyaudio

stop = threading.Event()

def wait():
  input("Press Enter to stop... \n")
  stop.set()

def recognize_speech():
  recognizer = sr.Recognizer()

  with sr.Microphone() as source:
    print("Adjusting noise... Please wait")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Listening...")

    audio = recognizer.listen(source)

  try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
  except sr.UnknownValueError:
    print("Sorry, could not understand the audio")
  except sr.RequestError as e:
    print("could not request results; {0}".format(e))

threading.Thread(target=wait).start()

recognize_speech()
