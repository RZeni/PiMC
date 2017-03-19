#!/usr/bin/env python3

#speech_recogonition is part of PyAudio, allows us to access Microphone class
#pygame allows us to play .mp3 files. We do not use wave files because gTTS saves as .mp3; We would need to use another library to convert mp3 to wave.
#gtts allows us to save text to speech files as mp3
#gmusicapi allows us to use Google Play Music API
#spotipy allows us to use spotify web api

import speech_recognition as sr
import time
import pygame
import random
import os
from gtts import gTTS
import spotipy


# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="AIzaSyC7AeLbq7r2YTLF91mQ5-sDKk8Hze7GM_o")`
            # instead of `r.recognize_google(audio)`
            text = r.recognize_google(audio)
            print("Google Speech Recognition thinks you said " + text)
            # Transcribe speech and save as a google doc, send link to email
            if text == "Transcribe":
                print("transcribing...")

            # searches for the audio to play using the selected service
            if text.startswith("play"):
                print("play")

            # searches for the audio to play using the selected service
            if text.startswith("Super hot fire"):
                print("Super hot fire")

            if text.startswith("shutdown"):
                stop_listening() # calling this function requests that the background listener stop listening

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source) # we only need to calibrate once, before we start listening

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# do some other computation for 5 seconds, then stop listening and keep doing other computations
for _ in range(50): time.sleep(0.1) # we're still listening even though the main thread is doing other things
#stop_listening() # calling this function requests that the background listener stop listening
while True: time.sleep(0.1)