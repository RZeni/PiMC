import unittest
import os

resourcePath = ""
os.chdir("..")
resourcePath = (os.path.abspath(os.curdir) + "\\resources\\")
speechList = ["hello", "goodbye", "searching for music", "artist", "song title" ]

# Unit
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

#Unit
# Author: Brandon Sheppard
# Function Name: create_speech_files
# Parameters:  0
# Date: March 19, 2017
# Returns: void
def create_speech_files():
    listLength = len(speechList)
    for i in range(0, listLength):
        textToSave = speechList[i]
        if ((not os.path.exists(resourcePath + textToSave + ".mp3"))):
            save_speech_file(textToSave)

#Unit
#Author: Brandon Sheppard
#Function Name: save_speech_file
#Parameters:  1 - the text to convert to to audio .mp3 file
#Date: March 19, 2017
#Returns: void
def save_speech_file(textToSpeech):
    tts = gTTS(text=textToSpeech, lang='en-us')
    fileName = textToSpeech + ".mp3"
    fullFilePath = resourcePath+fileName
    print ("Saving: " + fullFilePath)
    tts.save(fullFilePath)

# Here's our "unit tests".
class TestCreateMp3Files(unittest.TestCase):
    def testSaveFile(self):
        self.assertFalse(0)

    def testCreateAllFiles(self):
        self.assertFalse(0)

    def testPlayVoiceFile(self):
        self.assertFalse(0)

def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
