import speech_recognition as sr
import pyttsx3

#voice recognition using python 
#speech to voice 

def recognize_and_respond():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()

    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

            # Modify the response as needed
            response = f"You said: {text}. I here to give this hallo text may you like it thanks my broo."

            # Convert the response to speech
            engine.say(response)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
        except sr.RequestError as e:
            print(f"Error connecting to Google API: {e}")

if __name__ == "__main__":
    recognize_and_respond()
