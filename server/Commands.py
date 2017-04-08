# Author: Robert Zeni
# Purpose: The voice commands module
# Date: March 19, 2017
import speech_recognition as sr
from TTS import *
from Globals import  *
from _thread import start_new_thread

r = sr.Recognizer()
m = sr.Microphone()
stop_listening = None


def listen():
    print("Listening ...")
    r.dynamic_energy_threshold = True
    #r.operation_timeout = 5
    try:
        with m as source:
            r.adjust_for_ambient_noise(source)  # we only need to calibrate once before we start listening, then dynamic takes over
            audio = r.listen(source, 4)
        processCommand(r, audio)
    except sr.WaitTimeoutError as e:
        print("No Command Given")
    # start listening in the background (note that we don't have to do this inside a `with` statement)
    #stop_listening = r.listen_in_background(m, processCommand)


def processCommand(recognizer, audio):
    print("processing...")
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
        voice_command = ""
        if configuration.sr_service == SRServices.Shpynx.value:
            voice_command = recognizer.recognize_sphinx(audio)

        elif configuration.sr_service == SRServices.Google.value:
            voice_command = recognizer.recognize_google(audio)

        elif configuration.sr_service == SRServices.Cloud.value:
            voice_command = recognizer.recognize_google_cloud(audio)

        elif configuration.sr_service == SRServices.Bing.value:
            voice_command = recognizer.recognize_bing(audio)

        print("Google Speech Recognition thinks you said " + voice_command)

        if not voice_command.startswith(configuration.keyword):
            return

        # Transcribe speech and save as a google doc, send link to email
        if voice_command == "Transcribe":
            print("attempting transcribe...")
            #transcribe()
            return

        # searches for the audio to play using the selected service
        elif voice_command.startswith("play"):
            print("attempting play...")
            musicService.play_song(voice_command, configuration.music_service)
            return

        # # searches for the audio to play using the selected service
        # elif voice_command.startswith("preview"):
        #     print("attempting play...")
        #     musicService.play_song(voice_command, configuration.music_service)
        #     return

        # searches for the audio to play using the selected service
        elif voice_command.startswith("stop this"):
            print("attempting to stop song...")
            musicService.stop_song()
            return

        # searches for the audio to play using the selected service
        elif voice_command.startswith("pause this"):
            print("attempting to pause song...")
            musicService.pause_song()
            return

        # searches for the audio to play using the selected service
        elif voice_command.startswith("resume this"):
            print("attempting to resume song...")
            musicService.resume_song()
            return

        # searches for the audio to play using the selected service
        elif voice_command.startswith("rewind this"):
            print("attempting to rewind song...")
            musicService.rewind_song()
            return

        # searches for the audio to play using the selected service
        elif voice_command.startswith("fast forward this"):
            print("attempting to fast forward song...")
            musicService.fastforward_song()
            return

        # searches for the audio to play using the selected service
        elif voice_command.startswith("what is today's weather") or voice_command.startswith("what's today's weather") \
            or voice_command.startswith("how's the weather today") or voice_command.startswith("how is the weather today") \
            or voice_command.startswith("how's today's weather") or voice_command.startswith("how is today's weather"):
            print("retrieving today's weather...")
            TTS.say(TTS, weatherService.get_todays_weather(configuration.weather_service) )
            return

        # searches for the audio to play using the selected service
        elif voice_command.startswith("What is today's date") or voice_command.startswith("what's today's date"):
            print("retrieving today's date...")
            TTS.say(TTS, localeService.get_todays_date())
            return

        # searches for the audio to play using the selected service
        elif voice_command.startswith("What is the time") or voice_command.startswith("what's the time"):
            print("retrieving the time...")
            TTS.say(TTS, localeService.get_time())
            return

        # searches for the audio to play using the selected service
        elif voice_command.startswith("Super hot fire"):
            print("Super hot fire")
            return

        # Shutdown the server
        elif voice_command.startswith("shut down"):
            print("shutdown")
            #stop_listening() # calling this function requests that the background listener stop listening
            shutdown = 1

    except TimeoutError:
        print("Took too long to process audio")
    except NameError:
        print("A variable was not created, likely missing a default SR Service")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from selected service; {0}".format(e))
