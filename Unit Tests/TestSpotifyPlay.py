import unittest

# Here's our "unit".
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


# Here's our "unit tests".

class TestSpotifyPlay(unittest.TestCase):
    def testDetectSongAndArtist(self):
        voice_command = "play dab of ranch by migos"
        self.assertEqual("dab of ranch,migos", parse_voice_command(voice_command))

    def testDetectSong(self):
        voice_command = "play dab of ranch"
        self.assertEqual("dab of ranch", parse_voice_command(voice_command))


def main():
    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()


#Work in progress - gets the preview_url in order to play 30 second demo
#def play_spotify(song, artistName):
#    spotify = spotipy.Spotify()
#    results = spotify.search(q=song, limit=10)
#    for i, t in enumerate(results['tracks']['items']):
#        print (' ', i, t['name'],'preview url: ', t['preview_url'])

    #print(results)

