import speech_recognition as sr
import pyttsx3
import openai
import webbrowser
import os

openai.api_key = "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" 

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")
        return ""

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  
        prompt=prompt,
        max_tokens=150  
    )
    return response.choices[0].text.strip()

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "goodbye" in command:
        speak("Goodbye! Have a great day.")
        exit()
    elif "your name" in command:
        speak("My name is Max.")
    elif "open website" in command:
        speak("Sure, opening a website. Please provide the URL.")
        url = listen()
        if url:
            webbrowser.open(url)
        else:
            speak("Sorry, I didn't get the URL.")
    else:
        prompt = f"User command: {command}"
        response = generate_response(prompt)
        speak(response)

if __name__ == "__main__":
    speak("Hello! I'm Max, your voice assistant. How can I assist you today?")

    while True:
        command = listen()
        process_command(command)






        