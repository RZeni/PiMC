#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import subprocess
import io
import os
from Globals import  *  # initializes globals first
from RestAPI import *
from Commands import *
from _thread import start_new_thread

if __name__ == '__main__':
    #start the rest api server on a new thread
    start_new_thread(app.run,())

    #setup voice command server on current thread
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    recording = False
    elapsed_time = 0
    start_time = 0
    recording_process = None
    #turn on green light turn off others
    GPIO.output(18, True)
    GPIO.output(23, False)
    GPIO.output(24, False)

    try:
        #keep checking if button was pressed
        while True:
            #update elapsed time
            elapsed_time = time.time() - start_time
                
            #if currently recoring but not for 5s do nothing
            if recording and elapsed_time < 3.5:
                #print("still recording but not 5 s yet")
                    
                #If button is pressed stop recording else do nothing
                if GPIO.input(25) == 0:
                    print('thinks button is pressed')
                    #recording = False
                    #cmd_kill = "pkill -9 arecord"
                    #subprocess.Popen(cmd_kill.split()).wait()
                    #os.kill(recording_process.pid, signal.SIGINT)
                    #processcommand()
                    #time.sleep(1)
                    continue
                else:
                    #time.sleep(1)
                    continue
                    
            #if recording and greater than 5s stop recording
            if recording:
                recording = False
                cmd_kill = "pkill -9 arecord"
                subprocess.Popen(cmd_kill.split()).wait()
                os.kill(recording_process.pid, signal.SIGINT)
                process_command()
                GPIO.output(18, True)
                GPIO.output(23, False)
                GPIO.output(24, False)
                continue
                
            #we are not recording so check if button was pressed to start
            if GPIO.input(25) == 0:
                #start recoring and turn on yellow light
                GPIO.output(18, False)
                GPIO.output(23, True)
                GPIO.output(24, False)
                recording = True
                start_time = time.time()
                print('lights changed now record')
                cmd = "arecord --device=plughw:0,0 --format S16_LE --rate 44100 recording_audio.wav"
                recording_process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    except Exception as e:
       print ("Exception: {0}".format(e))
       GPIO.cleanup()
       
