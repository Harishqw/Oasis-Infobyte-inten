import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    current_hour = int(datetime.datetime.now().hour)
    if 0 <= current_hour < 12:
        speak("Good morning!")
    elif 12 <= current_hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant. How can I help you?")

def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Error: ", e)
        return get_command()

    return query

def respond_to_query(query):
    query = query.lower()

    if 'hello' in query:
        greet()

    elif 'time' in query:
        speak(f"The time is {datetime.datetime.now().strftime('%I:%M %p')}")

    elif 'date' in query:
        speak(f"The date is {datetime.datetime.now().strftime('%B %d, %Y')}")

    elif 'search' in query:
        try:
            speak('Searching...')
            query = query.replace('search', '')
            results = wikipedia.summary(query, sentences=2)
            speak(results)
        except Exception as e:
            print(e)
            speak('Sorry, I could not find any information on that.')

    elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
            speak(ex_exit)
            exit()

    else:
        speak("Sorry, I did not understand your query.")

if __name__ == "__main__":
    engine = pyttsx3.init()
    greet()

    while True:
        query = get_command()
        respond_to_query(query)