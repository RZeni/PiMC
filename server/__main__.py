#!/usr/bin/env python3

from Globals import  *  # initializes globals first
import time
from RestAPI import *
from Commands import *
from _thread import start_new_thread
if __name__ == '__main__':
    listen()  #start listening to voice input on a new thread
    app.run() #start the rest api server todo: on a new thread
    while True: time.sleep(0.1) # keep the main thread alive