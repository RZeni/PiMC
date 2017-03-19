#!/usr/bin/env python3

# speech_recogonition is part of PyAudio, allows us to access Microphone class
# pygame allows us to play .mp3 files. We do not use wave files because gTTS saves as .mp3;
# flask allows http server
# gtts allows us to save text to speech files as mp3
# gmusicapi allows us to use Google Play Music API
# spotipy allows us to use spotify web api

import time
from RestAPI import *

if __name__ == '__main__':
    for _ in range(50): time.sleep(0.1) # we're still listening even though the main thread is doing other things
    app.run()
    while True: time.sleep(0.1)