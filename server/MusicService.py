import pyaudio
import spotipy
from pygame import mixer
from urllib.request import urlretrieve
from Services import MusicServices
import pylast
import time
from Globals import credentials
from Globals import configuration
from subprocess import call
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import youtube_dl

class MusicService:
    def __init__(self):
        network = None
        if configuration.music_service == MusicServices.Last_FM.value:
            #music services requires authentication
            if credentials.LAST_FM_USERNAME != "" and credentials.LAST_FM_PASSWORD != "":
                #login
                return
            else:
                # raise tts error
                return
        if configuration.music_service == MusicService.Youtube.Value:
            self.youtube_download_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        return


    def parse_voice_command(self, voice_command):
        """
        :Author: Brandon Sheppard
        :param voice_command:
        :return: string "song title" or "song title, author"
        """
        command_split = voice_command.split(" ")
        song_title = ""
        artist = ""
        split_length = len(command_split)
        for i in range(1, split_length):
            if (not command_split[i] == "by"):
                song_title += command_split[i] + " "
            else:
                while (i < split_length - 1):
                    i += 1
                    artist += command_split[i] + " "
                break

        if (artist == ""):
            return (song_title.strip())
        else:
            return (song_title.strip() + " + " + artist.strip())


    def get_preview_url(self, voice_command):
        """

        :Author: Brandon Sheppard
        :param query:
        :return:
        """
        query = self.parse_voice_command(voice_command)
        spotify = spotipy.Spotify()
        results = spotify.search(q=query, limit=1)
        trackTemp = results['tracks']
        preview_url = trackTemp["items"]
        if len(preview_url) == 0:
            return None

        preview_url = trackTemp["items"][0]['preview_url']
        return preview_url


    def get_youtube_url(self, voice_command):
        voice_command = voice_command[5:];
        query = self.parse_voice_command(voice_command)
        var results = YouTube.Search.list('id,snippet', {q: query, maxResults: 1});
        return


    def play_song(self, voice_command, music_service):
        """

        :Author: Robert Zeni
        :param query:
        :return:
        """
        if music_service == MusicServices.Spotify.value:
            # if session active
            # play song

            # if credentials exists and login passes
            # if config['Spotify'] AND config['Spotify']['username'] != "" AND config['Spotify']['password'] != "" AND musicService.loginSpotify(config['Spotify']['username'], config['Spotify']['password']):
            # play song
            # else
            # tts "Failed to log in, I will attempt to play a preview instead
            if(voice_command.strip() == "play"):
                return

            url = self.get_preview_url(voice_command)
            if url == None:
                print("unable to find song")
                return

            try:
                mixer.quit()
                urlretrieve(url, "temp.mp3")
                mixer.init()
                mixer.music.load("temp.mp3")
                mixer.music.play()
            except Exception as e:
                return "Failed to retrieve url, or lacks access to temp file{0}",e
            return

        if music_service == MusicServices.Last_FM.value:
            print("Use google play")
            return

        if music_service == MusicServices.Youtube.value:
            with youtube_dl.YoutubeDL(self.youtube_download_opts) as ydl:
                ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])

            return

        print('Music Service Not Set')


    def pause_song(self):
        """

        :Author: Robert Zeni
        :param query:
        :return:
        """
        mixer.music.pause()


    def stop_song(self):
        """

        :Author: Robert Zeni
        :param query:
        :return:
        """
        mixer.music.stop()


    def resume_song(self):
        """

        :Author: Robert Zeni
        :param query:
        :return:
        """
        mixer.music.play()


    def rewind_song(self):
        """

        :Author: Robert Zeni
        :param query:
        :return:
        """
        mixer.music.rewind()


    def fastforward_song(self):
        """

        :Author: Robert Zeni
        :param query:
        :return:
        """
        mixer.music.rewind()
