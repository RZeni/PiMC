import unittest
import os
from gtts import gTTS
import random
from pygame import mixer
from TestDate import *
from tempfile import NamedTemporaryFile
from platform import system

resource_path = ""
os.chdir("..")
resource_path = (os.path.abspath(os.curdir) + "\\resources\\")
temp_path = (os.path.abspath(os.curdir) + "\\temp\\")
speech_list = ["hello", "goodbye"]


def open_temp_speech_file(file):
    """
    :author Brandon Sheppard:
    :name open_temp_speech_file:
    :param file_name:
    :date March 19, 2017
    :return: void
    """
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while mixer.music.get_busy():
        continue
    print("Done playing")
    mixer.quit()

def open_speech_file(file_name):
    """
    :author Brandon Sheppard:
    :name open_speech_file:
    :param file_name:
    :date March 19, 2017
    :return: void
    """
    path_to_file = resource_path + file_name + ".mp3"
    mixer.init()
    mixer.music.load(path_to_file)
    mixer.music.play()
    while mixer.music.get_busy() == True:
        continue
    print("Done playing " + pathToFile)
    mixer.quit()


def create_speech_files():
    """
    :author Brandon Sheppard:
    :name create_speech_files:
    :date March 19, 2017
    :return: void
    """
    list_length = len(speech_list)
    for i in range(0, list_length):
        text_to_save = speech_list[i]
        if not os.path.exists(resource_path + text_to_save + ".mp3"):
            save_speech_file(text_to_save)


def save_speech_file(text_to_say):
    """
    :author Brandon Sheppard:
    :name save_speech_file:
    :param text_to_say:
    :date March 19, 2017
    :return: void
    """
    file_name = text_to_say + ".mp3"
    full_file_path = resource_path + file_name
    if not os.path.exists(full_file_path):
        tts = gTTS(text=text_to_say, lang='en-us')
        tts.save(fullFilePath)


def create_temp_file(text_to_say):
    """
    :author: Brandon Sheppard:
    :name create_temp_file:
    :param text_to_say:
    :return: temp file
    """
    tts = gTTS(text=text_to_say, lang='en')
    f = NamedTemporaryFile(dir=temp_path, prefix="", suffix=".mp3", delete=False)
    tts.write_to_fp(f)
    f.close()
    return f

def say(text):
    """
    :author Brandon Sheppard:
    :name say:
    :param text:
    :date March 19, 2017
    :return: void
    """
    temp_file = create_temp_file(text)
    open_temp_speech_file(temp_file.name)
    os.remove(temp_file.name)


class TestCreateMp3Files(unittest.TestCase):
    @unittest.skip("Manually run this test")
    def testSaveFile(self):
        speech_file_name = "test file name"
        if not os.path.exists(resource_path+speech_file_name+ ".mp3"):
            save_speech_file(speech_file_name)

    @unittest.skip("Manually run this test")
    def testCreateAllFiles(self):
        listLength = len(speech_list)
        for i in range(0, listLength):
            save_speech_file(speech_list[i])

    @unittest.skip("Manually run this test")
    def testPlayRandomVoiceFile(self):
        voice_to_play = random.choice(speech_list)
        open_speech_file(voice_to_play)

    def testSpeechDate(self):
        #today = get_todays_date()
        #say(today)
        say("The quick brown fox")


def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
