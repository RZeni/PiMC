import unittest
import os
import require
import random
from TestDate import *
TTS = require('../server/TTS.py').TTS


class TestCreateMp3Files(unittest.TestCase):
    @unittest.skip("Manually run this test")
    def testSaveFile(self):
        speech_file_name = "test file name"
        if not os.path.exists(TTS.resource_path+speech_file_name+ ".mp3"):
            TTS.save_speech_file(speech_file_name)

    @unittest.skip("Manually run this test")
    def testCreateAllFiles(self):
        listLength = len(TTS.speech_list)
        for i in range(0, listLength):
            TTS.save_speech_file(TTS.speech_list[i])

    @unittest.skip("Manually run this test")
    def testPlayRandomVoiceFile(self):
        voice_to_play = random.choice(TTS.speech_list)
        TTS.open_speech_file(voice_to_play)

    def testSpeechDate(self):
        #today = get_todays_date()
        #say(today)
        TTS.say(TTS, "The quick brown fox")


def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
