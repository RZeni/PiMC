#!/usr/bin/env python3
import RPi.GPIO as GPIO
import subprocess
import time
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
    
    #turn on green light turn off others
    GPIO.output(18, LED_on)
    GPIO.output(23, LED_off)
    GPIO.output(24, LED_off)

    try:
        #keep checking if button was pressed
        while True:
            #update elapsed time
            elapsed_time = time.time() - start_time
            
            #if currently recoring but not for 5s do nothing
            if recording and elapsed_time < 5:
                #If button is pressed stop recording else do nothing
                if GPIO.input(25) == 0:
                    recording = False
                    cmd_kill = "pkill -9 arecord"
                    subprocess.Popen(cmd_kill.split()).wait()
                    os.kill(recording_process.pid, signal.SIGINT)
                    processcommand()
                    continue
                else:
                    continue
                
            #if recording and greater than 5s stop recording
            if recording:
                recording = False
                cmd_kill = "pkill -9 arecord"
                subprocess.Popen(cmd_kill.split()).wait()
                os.kill(recording_process.pid, signal.SIGINT)
                processcommand()
                continue
                 
            #we are not recording so check if button was pressed to start
            if GPIO.input(25) == 0:
                #start recoring and turn on yellow light
                GPIO.output(18, LED_off)
                GPIO.output(23, LED_on)
                GPIO.output(24, LED_off)
                time.sleep(0.25)
                recording = True
                start_time = time.time()
                record_voice_command()
    except:
       print ("Exception")
       GPIO.cleanup()
