# Author: Robert Zeni
# Purpose: Enum classes for preferences
# Date: March 19, 2017
from enum import Enum

class SRServices(Enum):
    Shpynx = 0
    Google = 1
    Cloud = 2
    Bing = 3
    Houndify = 4
    IBM = 5
    WIT = 6

class MusicServices(Enum):
    Spotify = 0
    Last_FM = 1
    Youtube = 2
    AmazonPrimeMusic = 3

class WeatherServices(Enum):
    OpenWeatherMap = 0
    Yahoo = 1
    Weather_com = 2
    NOAA = 3

class RadioServices(Enum):
    Last_FM = 0
