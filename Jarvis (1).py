import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    
    elif hour>=12 and hour <= 18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")

    speak("I am voice assistant of Computer Department. How may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 20000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en-in")
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    speak("Welcome to KKW")
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on queries
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("Acoording to Wikipedia")
            speak(results)

        elif 'marks' in query or 'rank' in query and 'open' in query:
            speak('Recalling the rank...')
            results = "The rank required is 12800 and below and percentile are 95 and above"
            speak(results)
        
        elif 'marks' in query or 'rank' in query and 'obc' in query:
            speak('Recalling the rank...')
            results = "The rank required is 15000 and below and percentile are 94 and above"
            speak(results)

        elif 'marks' in query or 'rank' in query and 'sc' in query:
            speak('Recalling the rank...')
            results = "The percentile are 88 and above"
            speak(results)

        elif 'marks' in query or 'rank' in query and 'st' in query:
            speak('Recalling the rank...')
            results = "The percentile are 84 and above"
            speak(results)

        elif 'marks' in query or 'rank' in query and 'tfws' in query:
            speak('Recalling the rank...')
            results = "The percentile are 98 and above"
            speak(results)

        elif 'marks' in query or 'rank' in query and 'ews' in query:
            speak('Recalling the rank...')
            results = "The percentile are 95 and above"
            speak(results)
    
        elif 'intake' in query or 'capacity' in query:
            speak('Recalling the capacity ...')
            results = "The Intake of Computer Department is 120"
            speak(results)

        elif 'documents required' in query and 'obc' in query:
            speak('This are the documents required for admission')
            results = '''Mht CET Score Card, Allotment Letter, SSC and HSC Result,
            Domicile Certificate, Non-Creamy layer, Leaving Certificate, Caste Certificate, Caste Validity'''
            speak(results)

        elif 'documents required' in query and 'sc' in query:
            speak('This are the documents required for admission')
            results = '''Mht CET Score Card, Allotment Letter, SSC and HSC Result,
            Domicile Certificate, Leaving Certificate, Caste Certificate, Caste Validity'''
            speak(results)

        elif 'documents required' in query and 'st' in query:
            speak('This are the documents required for admission')
            results = '''Mht CET Score Card, Allotment Letter, SSC and HSC Result,
            Domicile Certificate, Leaving Certificate, Caste Certificate, Caste Validity'''
            speak(results)

        elif 'documents required' in query and 'nt' in query:
            speak('This are the documents required for admission')
            results = '''Mht CET Score Card,Allotment Letter, SSC and HSC Result,
            Domicile Certificate,Non-Creamy layer,Leaving Certificate, Caste Certificate, Caste Validity'''
            speak(results)

        elif 'admission fee' in query and 'open' in query:
            speak('Calculating the fees')
            results = "148000"
            speak(results)

        elif 'admission fee' in query and ('obc' in query or 'ews' in query or 'ebc' in query):
            speak('Calculating the fees')
            results="Total fees for OBC or EWS or EBC is 80 thousand"
            speak(results)

        elif 'admission fee' in query and ('sc' in query or 'st' in query):
            speak('Calculating the fees')
            results="Total fees for SC and ST is 0 rupees"
            speak(results)

        elif 'admission fee' in query and 'tfws' in query:
            speak('Calculating the fees')
            results="Total fees for TFWS category is 18 thousand"
            speak(results)

        elif 'admission fee' in query and ('vjnt' in query or 'sbc' in query):
            speak('Calculating the fees')
            results="Total fees for VJNT is 18 thousand"
            speak(results)

        elif "why you came to the world" in query:
            speak("Thanks to Gayatri. further It's a secret")

        else:
            speak("Sorry, I'm still learning. I don't know that yet.")