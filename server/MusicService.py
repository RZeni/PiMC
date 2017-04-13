import pyaudio
import spotipy
from pygame import mixer
from urllib.request import urlretrieve
from Services import MusicServices
import pylast
import time
from Credentials import Credentials
from subprocess import call
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import youtube_dl

class MusicService:
    YouTube = None
    youtube_download_opts = None
    def __init__(self):
        self.network = None
        self.YouTube = build('youtube', 'v3', developerKey=Credentials.GOOGLE_API_KEY)

        self.youtube_download_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }


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
        voice_command = voice_command[5:]
        YouTube = build('youtube', 'v3', developerKey=Credentials.GOOGLE_API_KEY)
        search_response = YouTube.search().list(
            q=voice_command,
            part='id,snippet',
            maxResults=1
        ).execute()

        videos = []
        channels = []
        playlists = []

        # Add each result to the appropriate list, and then display the lists of
        # matching videos, channels, and playlists.
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                           search_result["id"]["videoId"]))
                return search_result;
            elif search_result["id"]["kind"] == "youtube#channel":
                channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                             search_result["id"]["channelId"]))
            elif search_result["id"]["kind"] == "youtube#playlist":
                playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                              search_result["id"]["playlistId"]))

        for vid in videos:
            print(vid)
        # for vid in channels:
        #     print(vid)
        # for vid in playlists:
        #     print(vid)
        return

    def play_youtube(self, voice_command):
        song = self.get_youtube_url(voice_command)
        with youtube_dl.YoutubeDL(self.youtube_download_opts) as ydl:
            ydl.download(['http://www.youtube.com/watch?v=' + song['id']['videoId']])
        mixer.quit()
        mixer.init()
        mixer.music.load(song['snippet']['title'])
        mixer.music.play()
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
