import configparser
import os

class ConfigService:
    def __init__(self):
        #print("config init")
        self.parser = configparser.ConfigParser()
        #print(os.path)
        self.config_file_name = 'settings.ini'
        self.parser.read(self.config_file_name)
        # default service settings
        if self.parser and self.parser.sections().__len__() != 0:
            self.keyword = self.parser['Settings']['keyword']
            self.sr_service = int(self.parser['Settings']['sr_service'])
            self.music_service = int(self.parser['Settings']['music_service'])
            self.weather_service = int(self.parser['Settings']['weather_service'])
        else:
            print("Failed to read config file, creating new one using factory defaults..")
            self.keyword = ""
            self.sr_service = 1
            self.music_service = 0
            self.weather_service = 3
        return

