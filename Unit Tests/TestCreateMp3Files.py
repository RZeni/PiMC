import unittest
import os
from gtts import gTTS
import random
import pygame
resourcePath = ""
os.chdir("..")
resourcePath = (os.path.abspath(os.curdir) + "\\resources\\")
speechList = ["hello", "goodbye"]

# Function
# Author: Brandon Sheppard
# Function Name: open_speech_file
# Parameters:  1 - the name of the file to open
# Date: March 19, 2017
# Returns: void
def open_speech_file(fileName):
    pathToFile = resourcePath + fileName + ".mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(pathToFile)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    print("Done playing " + pathToFile)
    pygame.quit()

#Function
# Author: Brandon Sheppard
# Function Name: create_speech_files
# Parameters:  0
# Date: March 19, 2017
# Returns: void
def create_speech_files():
    listLength = len(speechList)
    for i in range(0, listLength):
        textToSave = speechList[i]
        if (not os.path.exists(resourcePath + textToSave + ".mp3")):
            save_speech_file(textToSave)

#Function
#Author: Brandon Sheppard
#Function Name: save_speech_file
#Parameters:  1 - the text to convert to to audio .mp3 file
#Date: March 19, 2017
#Returns: void
def save_speech_file(textToSpeech):
    fileName = textToSpeech + ".mp3"
    fullFilePath = resourcePath + fileName
    if (not os.path.exists(fullFilePath)):
        tts = gTTS(text=textToSpeech, lang='en-us')
        tts.save(fullFilePath)

class TestCreateMp3Files(unittest.TestCase):
    @unittest.skip("Manually run this test")
    def testSaveFile(self):
        speechFileName = "test file name"
        if (not os.path.exists(resourcePath+speechFileName+".mp3")):
            save_speech_file(speechFileName)

    @unittest.skip("Manually run this test")
    def testCreateAllFiles(self):
        listLength = len(speechList)
        for i in range(0, listLength):
            save_speech_file(speechList[i])

    def testPlayRandomVoiceFile(self):
        voice_to_play = random.choice(speechList)
        open_speech_file(voice_to_play)

def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
