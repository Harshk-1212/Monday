import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
from dotenv import load_dotenv


def configure():
    load_dotenv()

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set API keys from environment variables
# newsapi = os.getenv("NEWSAPI_KEY")
# openai_api_key = os.getenv("OPENAI_API_KEY")



def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    client = OpenAI(api_key=os.getenv('openai_api'))

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Vision skilled in general tasks like Alexa and Google Cloud."},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message['content']

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "open netflix" in c:
        webbrowser.open("https://netflix.com")
    elif c.startswith("play"):
        song = c.split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found.")
    elif "news" in c:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={os.getenv('newsapi')}")
        if r.status_code == 200:
            data = r.json()
            for article in data['articles']:
                speak(article['title'])
        else:
            speak("Failed to retrieve news.")
    else:
        output = aiProcess(c)
        speak(output)

def main():
    configure()
    speak("Initializing Monday.....")
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                word = recognizer.recognize_google(audio)
                
                if word.lower() == "monday":
                    speak("Yes?")
                    with sr.Microphone() as source:
                        print("Vision Active...")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio.")
        except sr.RequestError:
            print("Sorry, there was an issue with the request.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
    
    
    
# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import musicLibrary
# import requests
# from openai import OpenAI
# from gtts import gTTS
# import pygame
# import os

# #pip install pocketshpinx

# #object that will recognize what someone is saying
# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# #Set API key from environment variable
# newsapi = os.getenv("NEWSAPI_KEY")



# # Set API key from environment variable
# # openai.api_key = os.getenv("OPENAI_API_KEY")

# # if not openai.api_key:
# #     raise ValueError("API key not found. Set the OPENAI_API_KEY environment variable.")


# #text to speech conversion using pyttsx
# def speak_old(text):
#     engine.say(text)
#     engine.runAndWait()
    
# def speak(text):
#     tts = gTTS(text)
#     tts.save('temp.mp3')   

#     # Initialize Pygame mixer
#     pygame.mixer.init()

#     # Load the MP3 file
#     pygame.mixer.music.load("temp.mp3")

#     # Play the MP3 file
#     pygame.mixer.music.play()

#     # Keep the program running while the music plays
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
        
        
#     pygame.mixer.music.unload()    
#     os.remove("temp.mp3")    
    

    
     
# def aiProcess(command):
  
#     #defaults to getting the key using os.environment.get("OPENAI_API_KEY")
#     #if you saved the key under a different envrironment variable name , you can do something like :
#     client = OpenAI()

#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a virtual assistant named vision skilled in general tasks like Alexa and Google cloud."},
#             {
#                 "role": "user",
#                 "content": command
#             }
#         ]
#     )

#     return(completion.choices[0].message)
    
    
    
# def processCommand(c):
#    if "open google" in c.lower():
#        webbrowser.open("https://google.com")
       
#    elif "open facebook" in c.lower():
#        webbrowser.open("https://facebook.com")
       
#    elif "open youtube" in c.lower():
#        webbrowser.open("https://youtube.com")
       
#    elif "open linkedin" in c.lower():
#        webbrowser.open("https://linkedin.com")
       
#    elif "open netflix" in c.lower():
#        webbrowser.open("https://netflix.com")
       
#    elif c.lower().startswith("play"):
#        song = c.lower().split(" ")[1]
#        link = musicLibrary.music[song]       
#        webbrowser.open(link)
       
#    elif "news" in c.lower():
#        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}") 
#        # Check if the request was successful
#        if r.status_code == 200:
#             # Parse the JSON response
#             data = r.json()

#             # Extract and speak the headlines
#             for article in data['articles']:
#                 speak(article['title'])
                
#    else:      
#        #let openAI handle the requests
#        output = aiProcess(c)
#        speak(output)
              
       

# #main function
# if __name__ =="__main__":
#     speak("Initialising Vision.....")
#     while True:
#         #Listen for the wake word "Vision"
#         # obtain audio from the microphone
#         r = sr.Recognizer()
        
        
        
#         print("recognizing...")
#         try:
#            with sr.Microphone() as source:
#               print("Listening...")
#               audio = r.listen(source , timeout= 2 , phrase_time_limit= 1) 
#               # only listens for 2 seconds then timeout , phase time limit is how much time you can take in between to speak
#            word = r.recognize_google(audio)
#            if(word.lower() == "brother"):
#                speak("Ya")
#                #listen for command
#                with sr.Microphone() as source:
#                   print("Vision Active...")
#                   audio = r.listen(source) 
#                   command = r.recognize_google(audio)
                  
                  
#                   processCommand(command)
               
        
#         except Exception as e:
#            print("Error; {0}".format(e))

