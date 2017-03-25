#!/usr/bin/env python3

from Globals import  *  # initializes globals first
import time
from RestAPI import *
from Commands import *
from _thread import start_new_thread
if __name__ == '__main__':
    start_new_thread(app.run,()) #start the rest api server on a new thread
    while True:
        listen()
