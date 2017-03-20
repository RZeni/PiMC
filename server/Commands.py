# Author: Robert Zeni
# Purpose: The voice commands module
# Date: March 19, 2017
import speech_recognition as sr
import pywapi
import string
from MusicService import MusicService
from Services import *
from TTS import *
import datetime

# API Keys
GOOGLE_API_KEY = "AIzaSyC7AeLbq7r2YTLF91mQ5-sDKk8Hze7GM_o"
OPEN_WEATHER_API_KEY = 'dd63aff110fe859652a1eb5e2d555e82'

# default service settings
sr_service = 1
music_service = 0
weather_service = 3
stop_listening = ""


def transcribe():
    """
    beings continual listening until stop phrase is spoken, one stopped, transcribes the audio to a google doc
    """
    # return if google docs is not set up / not available

    # listen until end phrase

    # save as google doc


def play_music(command):
    """
    Plays the specified song if possible using the selected music service
    :param command: the command string that initiated the function
    """
    # command parsing
    if music_service == MusicServices.Spotify.value:
        MusicService.play_song(MusicService, command)
        return

    if music_service == MusicServices.Google_Play.value:
        print("Use google play")
        return

    if music_service == MusicServices.SoundCloud.value:
        print("Use soundcloud")
        return

    print('Music Service Not Set')


def get_todays_weather():
    """
    Says today's weather forecast with the selected weather service
    :author Robert Zeni:
    :name get_todays_weather:
    :date March 19, 2017
    :return: void
    """
    if weather_service == WeatherServices.OpenWeatherMap:
        return

    if weather_service == WeatherServices.Yahoo.value:
        yahoo_result = pywapi.get_weather_from_yahoo('10001')
        print("Yahoo says: It is " + string.lower(yahoo_result['condition']['text']) + " and " +
              yahoo_result['condition'][
                  'temp'] + "C now in New York.\n\n")
        return

    if weather_service == WeatherServices.Weather_com.value:
        weather_com_result = pywapi.get_weather_from_weather_com('10001')
        print("Weather.com says: It is " + string.lower(weather_com_result['current_conditions']['text']) + " and " +
              weather_com_result['current_conditions']['temperature'] + "C now in New York.\n\n")
        return

    if weather_service == WeatherServices.NOAA.value:
        noaa_result = pywapi.get_weather_from_noaa('KJFK')
        print("NOAA says: It is " + string.lower(noaa_result['weather']) + " and " + noaa_result[
            'temp_c'] + "C now in New York.\n")
        return


def get_todays_date():
    """
    uses tts to speak today's date
    """
    mylist = []
    today = datetime.date.today()
    mylist.append(today)
    print(today.strftime('Today is, %B, %d, %Y'))
    TTS.say(TTS, today.strftime('Today is, %B, %d, %Y'))


def get_time():
    """
    Uses tts to speak the time
    """
    print(get_todays_date())
    TTS.say(TTS, get_todays_date())


# this is called from the background listener thread
def processCommand(recognizer, audio):
    """
    The function to execute upon speech detection. Determines what was said and runs the appropriate function
    :param recognizer: the recognizer to use
    :param audio: the audio to decode
    """
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="AIzaSyC7AeLbq7r2YTLF91mQ5-sDKk8Hze7GM_o")`
            # instead of `r.recognize_google(audio)`
            text = ""
            if sr_service == SRServices.Shpynx.value:
                text = recognizer.recognize_sphinx(audio)

            if sr_service == SRServices.Google.value:
                text = recognizer.recognize_google(audio)

            if sr_service == SRServices.Cloud.value:
                text = recognizer.recognize_google_cloud(audio)

            if sr_service == SRServices.Bing.value:
                text = recognizer.recognize_bing(audio)

            print("Google Speech Recognition thinks you said " + text)

            # Transcribe speech and save as a google doc, send link to email
            if text == "Transcribe":
                transcribe()
                return

            # searches for the audio to play using the selected service
            if text.startswith("play"):
                play_music(text)
                return

            # searches for the audio to play using the selected service
            if text in "today's weather":
                get_todays_weather()
                return

            # searches for the audio to play using the selected service
            if text.startswith("What is today's date") or text.startswith("what's today's date"):
                get_todays_date()
                return

            # searches for the audio to play using the selected service
            if text.startswith("What is the time") or text.startswith("what's the time"):
                get_time()
                return

            # searches for the audio to play using the selected service
            if text.startswith("Super hot fire"):
                print("Super hot fire")
                return

            # Shutdown the server
            if text.startswith("shutdown"):
                stop_listening() # calling this function requests that the background listener stop listening
    except NameError:
        print("A variable not created, likely missing a default SR Service")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
print("Listening ...")
# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, processCommand)