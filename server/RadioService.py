import pyaudio
import spotipy
from pygame import mixer
from urllib.request import urlretrieve
from Services import RadioServices
import pylast
import time
from Globals import credentials
from Globals import configuration

class RadioService:
    def __init__(self):
        self.network = None
        if configuration.music_service == RadioServices.Last_FM.value:
            if credentials.LAST_FM_USERNAME != "" and credentials.LAST_FM_PASSWORD != "":
                #radio services do not require authentication
                self.network =  pylast.LastFMNetwork(credentials.LAST_FM_API_KEY, credentials.LAST_FM_API_SECRET)
            else:
                # raise tts error
                return
        return

    def play_radio(self):
        return