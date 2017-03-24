# Author: Robert Zeni
# Purpose: Rest API to change preferences and log into accounts
# Date: March 19, 2017

from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from Commands import *
import json

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
           "}" % (sr_service, music_service, weather_service))
    return "{" \
             "\"keyword\" : \"\", " \
             "\"srService\" : %d, " \
             "\"musicService\" : %d, " \
             "\"weatherService\" : %d " \
           "}" % (sr_service, music_service, weather_service)


@app.route("/setPreferences", methods=['POST'])
@cross_origin()
def set_preferences():
    """
    sets the service preferences with the provided data
    Author: Robert Zeni
    Date: March 23, 2017
    :return:
    """
    preferences = json.loads(request.args.get('preferences'))
    print(preferences)
    cfgfile = open(config_file_name, 'w')

    if preferences.get('keyword') != None:
        keyword = preferences.get('keyword')
        config.set('Settings', 'keyword', preferences.get('keyword'))

    if preferences.get('srService') != None:
        sr_service = preferences.get('srService')
        config.set('Settings', 'sr_service', str(preferences.get('srService')))

    if preferences.get('musicService') != None:
        music_service = preferences.get('musicService')
        config.set('Settings', 'music_service', str(preferences.get('musicService')))

    if preferences.get('weatherService') != None:
        weather_service = preferences.get('weatherService')
        config.set('Settings', 'weather_service', str(preferences.get('weatherService')))

    config.write(cfgfile)
    cfgfile.close()

    # attampt login
    # return result
    return "j"


@app.route("/login", methods=['POST'])
@cross_origin()
def login():
    return "j"
