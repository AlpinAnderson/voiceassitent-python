import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

MASTER = "Alpin"

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    greeting = ""

    if hour < 12:
        greeting = "Selamat Pagi"
    elif hour < 18:
        greeting = "Selamat Siang"
    else:
        greeting = "Selamat Malam"

    talk(f"{greeting} Boss {MASTER}")

def take_command():
    try:
        with sr.Microphone() as source:
            print("Mendengarkan...")
            voice = mendengarkan.listen(source)
            command = mendengarkan.recognize_google(voice)
            command = command.lower()
            if "putri" in command:
                command = command.replace("putri", "")
                print(command)
                talk(command)
    except sr.UnknownValueError:
        pass

    return command

def run_putri():
    command = take_command()
    if 'play' in command:
        song = command.replace("play", "")
        talk("Memutar" + song)
        print("Memutar" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Sekarang pukul" + time)
    elif "wikipedia" in command:
        src = command.replace("wikipedia", "")
        info = wikipedia.summary(src, sentences=1)
        talk("Mencari di Wikipedia")
        print(info)
        talk(info)
    else:
        talk("Instruksi tidak ditemukan")
        print(command)

engine = pyttsx3.init()
voices = engine.getProperty('voices')

male_voice = None
for voice in voices:
    if voice.gender == 'male':
        male_voice = voice
        break

if male_voice is not None:
    engine.setProperty('voice', male_voice.id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 125)

wishMe()

while True:
    mendengarkan = sr.Recognizer()
    talk("Saya adalah putri. apakah yang bisa saya bantu boss Nainggolan?")
    run_putri()