# Author: Brandon Sheppard modified to a class by Robert Zeni
# Purpose: Enum classes for preferences
# Date: March 19, 2017
import os
from gtts import gTTS
from pygame import mixer
from tempfile import NamedTemporaryFile


class TTS:
    resource_path = ""
    os.chdir("..")
    temp_path = ""
    speech_list = ""

    def __init__(self):
        self.resource_path = ""
        os.chdir("..")
        self.resource_path = (os.path.abspath(os.curdir) + "\\resources\\")
        self.temp_path = (os.path.abspath(os.curdir) + "\\temp\\")
        self.speech_list = ["hello", "goodbye"]

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

    def open_speech_file(self, file_name):
        """
        :author Brandon Sheppard:
        :name open_speech_file:
        :param file_name:
        :date March 19, 2017
        :return: void
        """
        path_to_file = self.resource_path + file_name + ".mp3"
        mixer.init()
        mixer.music.load(path_to_file)
        mixer.music.play()
        while mixer.music.get_busy() == True:
            continue
        print("Done playing " + path_to_file)
        mixer.quit()

    def create_speech_files(self):
        """
        :author Brandon Sheppard:
        :name create_speech_files:
        :date March 19, 2017
        :return: void
        """
        list_length = len(self.speech_list)
        for i in range(0, list_length):
            text_to_save = self.speech_list[i]
            if not os.path.exists(self.resource_path + text_to_save + ".mp3"):
                self.save_speech_file(self, text_to_save)

    def save_speech_file(self, text_to_say):
        """
        :author Brandon Sheppard:
        :name save_speech_file:
        :param text_to_say:
        :date March 19, 2017
        :return: void
        """
        file_name = text_to_say + ".mp3"
        full_file_path = self.resource_path + file_name
        if not os.path.exists(full_file_path):
            tts = gTTS(text=text_to_say, lang='en-us')
            tts.save(full_file_path)

    def create_temp_file(self, text_to_say):
        """
        :author: Brandon Sheppard:
        :name create_temp_file:
        :param text_to_say:
        :return: temp file
        """
        tts = gTTS(text=text_to_say, lang='en')
        f = NamedTemporaryFile(dir=self.temp_path, prefix="", suffix=".mp3", delete=False)
        tts.write_to_fp(f)
        f.close()
        return f

    def say(self, text):
        """
        :author Brandon Sheppard:
        :name say:
        :param text:
        :date March 19, 2017
        :return: void
        """
        temp_file = self.create_temp_file(self, text)
        self.open_temp_speech_file(temp_file.name)
        os.remove(temp_file.name)
