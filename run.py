"""
PYTHON PERSONAL ASSISTANCE USING PYTHON
STILL IN DEV
AUTHOR : Oussama
FACEBOOK:https://www.facebook.com/unknownkid.18
INSTAGRAM:https://www.instagram.com/o.u.s.s._.a.m.a
"""
import os
import sys
import time
import datetime
import re
import urllib.parse
import urllib.request
import requests
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import wikipedia
from lib.wallpaper import pick_wall

def initiating(recognizer,microphone):

    """
    This Function is Just Used to Listen For Incoming Voice
    """

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # Seting Up Some Values
    voice={
    "text":None,
    "error":None,
    "success":True
    }
    try: # Store speech in a Dictionary Key("text") Value
        voice['text']=recognizer.recognize_google(audio)

    except sr.RequestError:
        # API is unreachable
        voice["success"] = False
        voice["error"] = "API unavailable"

    except sr.UnknownValueError:
        # Unvalid Speech Input
        voice["error"] = "Unable to recognize speech"

	# Return Final Result of the Values After Trying To Listen For Incoming Voices
    return voice

def speak(text):

    """
    This Function Used to Save The Recorded Audio To a File For Convert it To Speech Later
    """

    speech = gTTS(text = text,lang = 'en')
    speech.save('start.mp3')
    playsound('start.mp3')
    os.remove('start.mp3')

def play(video):

    """
    Search For Video Full URL in Youtube By Video Name And Return The Full URL
    """

    query_string = urllib.parse.urlencode({"search_query": video})
    format_url = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", format_url.read().decode())
    clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
    if clip:
        youtube_video = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

    else:
        return False

    return youtube_video

if __name__ == "__main__":

    try:
        r=sr.Recognizer()
        m=sr.Microphone()
        os.system('clear')
        time.sleep(0.5)
        speak("HI Osama So What Do You Need Today") #The Start
        print('''
        PYTHON ASSISTANCE v1.0

        play        speak   (SONG or VIDEO NAME ON YOUTUBE)
        search      speak   (ANYTHING ON GOOGLE)
        wikipedia   speak   (ANYTHING ON WIKIPEDIA)
        wallpaper   speak   (TYPE OF WALLAPERS YOU WANT TO DOWNLOAD AND APPLY)
        time                (FOR CURRENT TIME)
        can you hear me     (CHECK FOR ASSISTANCE)
        exit/quit           (EXIT THE PROGRAM)
        
        SOCIAL :
            FACEBOOK    :   https://www.facebook.com/unknownkid.18
            INSTAGRAM   :   https://www.instagram.com/o.u.s.s._.a.m.a
        ''')
        while 1: #To Not Stop The Porgram After Just 1 Run

            sound=initiating(r,m)

            if str(sound['text'])=="time":
                date = datetime.datetime.now()
                print(date)
                speak('time is')
                speak(str(date))

            if "search" in str(sound['text']).lower():
                SEARCH_FOR=str(sound['text']).lower()[7:]
                os.system(f"firefox http://www.google.com/search?q='{SEARCH_FOR}' 2>/dev/null")
                speak(f'Searching For {SEARCH_FOR}')

            if "play" in str(sound['text']).lower():
                SONG_NAME=str(sound['text']).lower()[4:]
                os.system(f'firefox {play(SONG_NAME)} 2> /dev/null')
                speak(f'playing {SONG_NAME}')

            if "wallpaper" in str(sound['text']).lower():
                WALL_NAME=str(sound['text']).lower()[10:]
                try:
                    pick_wall(WALL_NAME)
                    speak(f'searching for {WALL_NAME} wallpapers')
                except:
                    speak('Sorry Wallpaper Did Not Change Succefuly Please Try Again')

            if "wikipedia" in str(sound['text']).lower():
                WIKIPEDIA=str(sound['text']).lower()[10:]
                result = wikipedia.summary(WIKIPEDIA, sentences = 2)
                print(result)
                speak(result)

            if "can you hear me" in str(sound['text']).lower():
                speak("Yeah But Your Internet Sucks Dude ")

            if sound['error']:
                print(str(sound['error']))

            else:
                print(sound['text'])

            if 'quit' in str(sound['text']).lower() or 'exit' in str(sound['text']).lower():
                speak('i Love You Bye Bye') # Hahahahaha Just Joking Around
                break

    except KeyboardInterrupt:
        print("[ ! ] EXITING")
        sys.exit(2)
