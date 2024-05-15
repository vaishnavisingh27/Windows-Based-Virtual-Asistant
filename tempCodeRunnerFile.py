import subprocess
from typing import Self
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import google
import googlesearch
import os
import ctypes
import bs4
from googlesearch import search
import pywhatkit
import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
import time
from PIL import Image, ImageTk
from googletrans import Translator


engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')  # Get the current speaking rate
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


recognizer = sr.Recognizer()


listening = False

def speak(audio):
    response_text.insert(tk.END, "Assistant: " + audio + "\n\n")
    engine.say(audio)
    engine.runAndWait()

def translate_to_english(text):
    translator = Translator()
    translated_text = translator.translate(text, src='hi', dest='en').text
    return translated_text

def take_command():
    global listening
    with sr.Microphone() as source:
        response_text.insert(tk.END, "Assistant: Listening...\n")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        listening = False

    try:
        response_text.insert(tk.END, "Assistant: Recognizing...\n")
        query = recognizer.recognize_google(audio, language='en-in')

        if 'en' not in recognizer.recognize_google(audio, language='en-in', show_all=True):
            query = translate_to_english(query)

        response_text.insert(tk.END, "You: " + query + "\n")
        return query
    except Exception as e:
        print(e)
        response_text.insert(tk.END, "Assistant: Unable to Recognize your voice\n")
        return "None"


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning, sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon, sir!")
    else:
        speak("Good evening, sir!")

    speak("I am Edith. How may I help you, sir?")

def process_query():

    while True:
        global listening
        if listening:
            query = take_command().lower()
            
            if 'exit' in query or 'bye' in query or 'goodbye' in query:
                speak("See you later, Have a nice day")
                root.destroy()
                exit()
                break

            elif 'wikipedia' in query:
                speak('Searching Wikipedia....')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'google' in query:
                import wikipedia as googleScrap
                query=query.replace("Edith","")
                query=query.replace("google", "")
                speak("This is what i found on the web!")
                pywhatkit.search(query)

                try:
                    result=googleScrap.summary(query,2)
                    speak(result)
                    print(result)

                except:
                    speak("no data found")
                    print("No Data Found")
#Webbrowser Query
      
            elif 'open youtube' in query or 'youtube' in query:
                speak("Here you go to Youtube\n")
                webbrowser.open("youtube.com")
 
            elif 'open google' in query or 'goggle' in query:
                speak("Here you go to Google\n")
                webbrowser.open("google.com")

            elif 'open gmail' in query or 'gmail' in query:
                speak("Here you go to Gmail\n")
                webbrowser.open("gmail.com")

            elif 'open map' in query or 'map' in query:
                speak("here you go to map\n")
                webbrowser.open("googlemaps.com")

            elif 'weather forecasting' in query or 'weather' in query:
                speak("here you go to weather forecasting")
                webbrowser.open("weather.com")

            elif 'play music' in query or 'open music' in query or 'music' in query:
                speak("here you go!!")
                webbrowser.open('www.spotify.com')

            elif 'open whatsapp' in query or 'whatsapp' in query:
                speak("here you go to whatsapp\n")
                webbrowser.open("web.whatsapp.com")

#Application Queries

            elif 'open chrome' in query or 'chrome' in query:
                chrome ="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chrome)

            elif 'open edge' in query or 'edge' in query:
                notepad ="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(notepad)

            elif 'open vlc' in query or 'media player' in query or 'vlc' in query or 'media player' in query:
                paint ="C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
                os.startfile(paint)

            elif 'open word' in query or 'word' in query:
                word ="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(word)

            elif 'open excel' in query or 'excel' in query:
                excel ="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(excel)

            elif 'open powerpoint' in query or 'powerpoint' in query:
                powerpoint ="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(powerpoint)
        
            elif 'open code' in query or 'code' in query:
                code ="C:\\Users\\kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code)

            elif 'open command prompt' in query or 'cmd' in query or 'command prompt' in query:
                cmd="%windir%\\system32\\cmd.exe"
                os.startfile(cmd)

#Basic Queries

            elif "hi" in query or 'hello' in query or 'hey' in query:
                print("Hi, I am Edith your bot assistant")
                speak("Hi, I am Edith your bot assistant")

            elif "thanks" in query or 'thank you' in query or 'thanks for the help' in query:
                print("You're most welcome!")
                speak("You're most welcome!")

            elif "who are you" in query or 'what are you' in query or 'about' in query or 'tell me about yourself' in query or 'who r u' in query:
                print("I am your virtual assistant created by Team Squad")
                speak("I am your virtual assistant created by Team Squad")

            elif 'how are you' in query or 'how r u' in query:
                print("I am fine, Thank you")
                print("How are you, Sir")
                speak("I am fine, Thank you")
                speak("How are you, Sir")
 
            elif 'fine' in query or 'good' in query or 'ok' in query:
                print("It's good to know that your fine")
                speak("It's good to know that your fine")

            elif "what's your name" in query or "What is your name" in query:
                print("My friends call me Edith")
                speak("My friends call me Edith")

            elif "who i am" in query:
                print("If you talk then definitely your human.")
                speak("If you talk then definitely your human.")
 
            elif "why you came to world" in query:
                print("Thanks to Team Squad. further It's a secret")
                speak("Thanks to Team Squad. further It's a secret")

            elif 'is love' in query:
                print("It is 7th sense that destroy all other senses")
                speak("It is 7th sense that destroy all other senses")
 
            elif 'reason for you' in query:
                print("I was created as a Minor project by Team Squad")
                speak("I was created as a Minor project by Team Squad")

            elif "Good Morning" in query:
                print("A warm" +query)
                print("How are you Master")
                speak("A warm" +query)
                speak("How are you Master")
        
            elif "Good Afternoon" in query:
                print(query)
                print("How are you Master")
                speak(query)
                speak("How are you Master")

            elif "Good evening" in query:
                print(query)
                print("How are you Master")
                speak(query)
                speak("How are you Master")

            elif "will you be my gf" in query or "will you be my bf" in query:  
                print("I'm not sure about, may be you should give me some time")
                speak("I'm not sure about, may be you should give me some time")

            elif "i love you" in query:
                print("It's hard to understand")
                speak("It's hard to understand")

#System Queries

            elif 'lock window' in query or 'lock the window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif 'shutdown system' in query or 'shut the system shutdown' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

            elif "restart" in query or 'restart the system' in query:
                subprocess.call(["shutdown", "/r"])

            elif "hibernate" in query or "sleep" in query:
                speak("Hibernating")
                subprocess.call("shutdown / h")

#collage query

            elif "tell me about avit" in query or "overview of avit" in query:
                speak("AARUPADAI VEEDU INSTITUTE OF TECHNOLOGY")
                print("AARUPADAI VEEDU INSTITUTE OF TECHNOLOGY")
                speak("AVIT is located on Rajiv Gandhi Salai(old Mahabalipuram Road) about 50 kms from Chennai in lush, sylvan surroundings, far from madding crowd.")
                print("AVIT is located on Rajiv Gandhi Salai(old Mahabalipuram Road) about 50 kms from Chennai in lush, sylvan surroundings, far from madding crowd.")

            elif "chancellor" in query:
                speak("Dr.A.SHANMUGASUNDARAM-FOUNDER CHANCELLOR")
                print("Dr.A.SHANMUGASUNDARAM-FOUNDER CHANCELLOR")
                speak("Dr.A.S GANESAN-CHANCELLOR")
                print("Dr.A.S GANESAN-CHANCELLOR")

        else:
            time.sleep(1)
            stop_listening()


def start_listening():
    global listening
    listening = True
    Thread(target=process_query).start()

def stop_listening():
    global listening
    listening = False


# GUI 


root = tk.Tk()
root.title("Voice Assistant")
root.geometry("800x600")

logo_image = Image.open("logo.png")
logo_image = logo_image.resize((50, 50), Image.BILINEAR)
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(root, image=logo_photo)
logo_label.grid(row=0, column=0, padx=20, pady=20, columnspan=3)

assistant_label = tk.Label(root, text="Assistant", font=("Helvetica", 14))
assistant_label.grid(row=1, column=0, columnspan=3)

response_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, padx=20, pady=20, font=("Helvetica", 12), fg="white", bg="#2e2e2e")
response_text.grid(row=2, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")

mic_image = Image.open("mic.jpeg")
mic_image = mic_image.resize((50, 50), Image.BILINEAR)
mic_photo = ImageTk.PhotoImage(mic_image)

start_button = tk.Button(root, image=mic_photo, command=start_listening, border="2px")
start_button.grid(row=3, column=0, columnspan=3, padx=20, pady=20, sticky="ns")

root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

Thread(target=wishMe).start()

root.mainloop()
