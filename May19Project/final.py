#!/usr/bin/python
import time
import RPi.GPIO as GPIO
 
GPIO_BEGIN_PIN = 4
GPIO_END_PIN = 17
MAX_ALLOWED_SPEED=10
 
DISTANCE = 10.0 # (in cm) Anpassen, falls notwendig
TIMEOUT = 5 # sek
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
if __name__ == '__main__':
    GPIO.setup(GPIO_BEGIN_PIN, GPIO.IN)
    GPIO.setup(GPIO_END_PIN, GPIO.IN)
    while 1:
        start_time, end_time = 0, 0
        
        while GPIO.input(GPIO_BEGIN_PIN) == GPIO.LOW:
            time.sleep(0.001)
            start_time = time.time()
        end_time = 0
     
        while GPIO.input(GPIO_END_PIN) == GPIO.LOW and time.time()-start_time < TIMEOUT:
            time.sleep(0.001)
        else:
            end_time = time.time()
        if(start_time!=end_time and DISTANCE!=0):
            speed = DISTANCE / (end_time - start_time)
            print("Speed: %.20f cm/s" % speed)
            if(speed>MAX_ALLOWED_SPEED):
                print("Speed is going out of maximum allowed speed")
