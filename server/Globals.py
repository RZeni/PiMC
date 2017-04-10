from ConfigService import ConfigService
from Credentials import Credentials
from MusicService import MusicService
from WeatherService import WeatherService
from LocaleService import LocaleService
from Services import *

configuration = ConfigService()
credentials = Credentials()
musicService = MusicService(configuration.music_service)
weatherService = WeatherService()
localeService =LocaleService()