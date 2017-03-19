# Author: Robert Zeni
# Purpose: Rest API to change preferences and log into accounts
# Date: March 19, 2017
from flask import Flask
from flask import request
from Commands import *

app = Flask(__name__)


@app.route("/getPreferences")
def get_preferences():
    """

    :return: a string of all preferences in JSON format
    """
    return "{" \
             "\"srService\" : %d, " \
             "\"musicService\" : %d, " \
             "\"weatherService\" : %d " \
           "}" % (sr_service, music_service, weather_service)


@app.route("/setPreferences", methods=['POST'])
def set_preferences():
    print(request)