import pyaudio
import spotipy
from pygame import mixer
from urllib.request import urlretrieve


class MusicService:
    def __init__(self):
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


    def get_preview_url(self, query):
        """

        :Author: Brandon Sheppard
        :param query:
        :return:
        """
        spotify = spotipy.Spotify()
        results = spotify.search(q=query, limit=1)
        trackTemp = results['tracks']
        preview_url = trackTemp["items"][0]['preview_url']
        return preview_url


    def play_song(self, voice_command):
        """

        :Author: Robert Zeni
        :param query:
        :return:
        """
        url = self.get_preview_url(self, self.parse_voice_command(self, voice_command))
        urlretrieve(url, "temp.mp3")

        mixer.init()
        mixer.music.load("temp.mp3")
        mixer.music.play()
        while mixer.music.get_busy() == True:
            continue
        print("Done playing ")
        mixer.quit()
