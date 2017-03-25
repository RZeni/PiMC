from Services import WeatherServices
import pywapi


class WeatherService:
    def __init__(self):
        return


    def get_todays_weather(self, weather_service):
        """
        Says today's weather forecast with the selected weather service
        :author Robert Zeni:
        :name get_todays_weather:
        :param weather_service - the service to use for weather retrieval
        :date March 19, 2017
        :return: void
        """
        if weather_service == WeatherServices.OpenWeatherMap.value:
            return "Weather retrieval using open weather map is not implemented yet."

        if weather_service == WeatherServices.Yahoo.value:
            yahoo_result = pywapi.get_weather_from_yahoo('10001')
            return "It is " + yahoo_result['condition']['text'] + " and " + yahoo_result['condition']['temp'] + "degrees celsius now in New York.\n\n"

        if weather_service == WeatherServices.Weather_com.value:
            weather_com_result = pywapi.get_weather_from_weather_com('10001')
            return "Weather.com says: It is " + weather_com_result['current_conditions']['text'] + " and " + weather_com_result['current_conditions']['temperature'] + "degrees celsius  now in New York.\n\n"

        if weather_service == WeatherServices.NOAA.value:
            noaa_result = pywapi.get_weather_from_noaa('KJFK')
            return "NOAA says it is, " + noaa_result['weather'] + " and " + noaa_result['temp_c'] + "degrees celsius right now.\n"


    def get_tomorrows_weather(selfself, weather_service):
        """

        :param weather_service:
        :return:
        """
        return "Searching for tomorrow's weather is not yet implemented"

