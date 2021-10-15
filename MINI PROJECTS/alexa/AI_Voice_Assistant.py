import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os

engine = pyttsx3.init()  # initialize the pyttsx3
voices = engine.getProperty('voices')  # voice property
engine.setProperty('voice', voices[1].id)  # set male or female voice
newVoiceRate = 160  # voice speed
engine.setProperty('rate', newVoiceRate)


# method to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()  # run and wait till display out


def time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    speak(time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("current date is ")
    speak(day)
    speak(month)
    speak(year)


def wishme():
    speak("welcome back sir!")
    hour = datetime.datetime.now().hour

    if 6 >= hour <= 12:
        speak("Good morning")
    elif 12 >= hour <= 18:
        speak("Good afternoon")
    else:
        speak("Good Evening")
    speak("cat at your service. How I can help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:  # access microphone
        print("Listening...")  # message to display that AI is listening
        r.pause_threshold = 1  # pause for 1 sec when it get start
        audio = r.listen(source)  # listen user voice

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, 'en=US')  # user input in English (US language)
        print(query)  # display user command / query
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query


def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  # check the connection
    server.starttls()  # start
    server.login("test@gmail.com", "password")  # sender mail and password
    server.sendmail("xyz@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")  # replace the wikipedia with user command
            result = wikipedia.summary(query, sentence=2)  # summary with all the sentences
            speak(result)  # speak the result

        elif 'send email' in query:
            try:
                speak("What should i say")
                content = takeCommand()  # subject
                to = "xyz@gmail.com"  # receiver email
                sendMail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")

        elif 'search in chrome' in query:
            speak("what should i search")
            chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromePath).open_new_tab(search + ".com")

        elif "logout" in query:
            os.system("shutdown - 1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("restart /r /t 1")

        elif "offline" in query:
            quit()
