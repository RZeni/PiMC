# Author: Robert Zeni
# Purpose: Rest API to change preferences and log into accounts
# Date: March 19, 2017

from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from Globals import  *
import json
from threading import Thread
app = Flask(__name__)
CORS(app)


@app.route("/getPreferences")
@cross_origin()
def get_preferences():
    """
    sends the service preferences to the client when requested
    Author: Robert Zeni
    Date: March 19, 2017
    :return: a string of all preferences in JSON format
    """
    print("{" \
             "\"keyword\" : \"\", " \
             "\"srService\" : %d, " \
             "\"musicService\" : %d, " \
             "\"weatherService\" : %d " \
           "}" % (configuration.sr_service, configuration.music_service, configuration.weather_service))
    return "{" \
             "\"keyword\" : \"hfg\", " \
             "\"srService\" : %d, " \
             "\"musicService\" : %d, " \
             "\"weatherService\" : %d " \
           "}" % (configuration.sr_service, configuration.music_service, configuration.weather_service)


@app.route("/setPreferences", methods=['POST'])
@cross_origin()
def set_preferences():
    """
    sets the service preferences with the provided data
    Author: Robert Zeni
    Date: March 23, 2017
    :return:
    """
    returnString = "{"
    requestPreferences = json.loads(request.args.get('preferences'))
    print(requestPreferences)

    cfgfile = open(configuration.config_file_name, 'w')

    if requestPreferences.get('keyword') != None:
        keyword = requestPreferences.get('keyword')
        configuration.parser.set('Settings', 'keyword', requestPreferences.get('keyword'))

    if requestPreferences.get('srService') != None:
        sr_service = requestPreferences.get('srService')
        configuration.parser.set('Settings', 'sr_service', str(requestPreferences.get('srService')))
        returnString += "\"srService\" : \"%s\"",str(requestPreferences.get('srService'))

    if requestPreferences.get('musicService') != None:
        music_service = requestPreferences.get('musicService')
        configuration.parser.set('Settings', 'music_service', str(requestPreferences.get('musicService')))
        returnString += "\"musicService\" : \"%s\"",str(requestPreferences.get('musicService'))

    if requestPreferences.get('weatherService') != None:
        weather_service = requestPreferences.get('weatherService')
        configuration.parser.set('Settings', 'weather_service', str(requestPreferences.get('weatherService')))
        returnString += "\"weatherService\" : \"%s\"",str(requestPreferences.get('weatherService'))

    returnString += "}"
    configuration.config.write(cfgfile)
    cfgfile.close()

    return returnString



@app.route("/login", methods=['POST'])
@cross_origin()
def login():
    """
    sets the service preferences with the provided data
    Author: Robert Zeni
    Date: March 23, 2017
    :return:
    """
    return "j"
