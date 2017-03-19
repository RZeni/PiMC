import unittest
import spotipy
from gTTS import gtts
# Function
# Author: Brandon Sheppard
# Function Name: parse_voice_command
# Parameters:  1 - the voice command as string
# Date: March 19, 2017
# Returns: string "song title" or "song title, author"
def parse_voice_command(voice_command):
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
        return (song_title.strip() + "," + artist.strip())

# Function
# Author: Brandon Sheppard
# Function Name: get_preview_url
# Parameters:  2 - song title, artist name
# Date: March 19, 2017
# Returns: string url for spotify 30 second preview
def get_preview_url(song_title, artist_name):
    spotify = spotipy.Spotify()
    results = spotify.search(q=song_title, limit=1)
    trackTemp = results['tracks']['items']
    preview_url = trackTemp[0]['preview_url']
    return preview_url
    #track_name = trackTemp[0]['name']
    #for i, t in enumerate(results['tracks']['items']):
        #print (' ', i, t['name'],'preview url: ', t['preview_url'])

class TestSpotifyPlay(unittest.TestCase):
    def testDetectSongAndArtist(self):
        voice_command = "play dab of ranch by migos"
        self.assertEqual("dab of ranch,migos", parse_voice_command(voice_command))

    def testDetectSong(self):
        voice_command = "play dab of ranch"
        self.assertEqual("dab of ranch", parse_voice_command(voice_command))

    def testGetPreviewUrl(self):
        get_preview_url("dab of ranch", "migos")



def main():
    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()


