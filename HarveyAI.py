import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say("Hello, I am Harvey.")
engine.say("What can I do for you?")
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():    
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'harvey' in command:
                command = command.replace('harvey', '')
                print(command) 
    except:
        pass
    return command

def run_harvey():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing the song' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %M %p')
        talk('The current time is' + time)
    elif 'search' in command:
        search = command.replace('search', '')
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'thank' in command:
        talk('I hope I helped you, Good bye.')
        exit()
    else:
        talk('Please say that again.')

while True:
    run_harvey()        