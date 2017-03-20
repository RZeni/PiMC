import unittest
import require
MusicService = require("../server/MusicService.py").MusicService


class TestSpotifyPlay(unittest.TestCase):
    @unittest.skip("Manually run this test")
    def testDetectSongAndArtist(self):
        voice_command = "play dab of ranch by migos"
        self.assertEqual("dab of ranch,migos", MusicService.parse_voice_command(MusicService, voice_command))

    @unittest.skip("Manually run this test")
    def testDetectSong(self):
        voice_command = "play dab of ranch"
        self.assertEqual("dab of ranch", MusicService.parse_voice_command(MusicService, voice_command))

    def testGetPreviewUrl(self):
        print(MusicService.get_preview_url(MusicService, "dab of ranch + migos"))

    def test_play_song(self):
        MusicService.play_song(MusicService, "play dab of ranch by migos")


def main():
    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()


