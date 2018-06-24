from EmulatorGUI import GPIO
#!/usr/bin/python
import time
import signal
import sys
#import RPi.GPIO as GPIO
from datetime import datetime
from zeep import Client
 
GPIO_BEGIN_PIN = 4
GPIO_END_PIN = 17
MAX_ALLOWED_SPEED=40
 
DISTANCE = 10.0 # (in cm) Anpassen, falls notwendig
TIMEOUT = 5 # sek
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#sending SMS to the PCR
def informPCR():
    url = 'https://api2.onnorokomsms.com/sendsms.asmx?WSDL'
    client = Client(url)

    userName = '01676409085'
    password = '27968'
    recipientNumber = '01521418737'
    smsText = 'If this SMS reaches to you then congratulations! Our SMS system is working!!---hafiz031'
    smsType = 'TEXT'

    maskName = ''
    campaignName = ''

    client.service.OneToOne(userName,password,recipientNumber,smsText,smsType,maskName,campaignName)

 
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
        if(start_time!=end_time):
            speed = DISTANCE / (end_time - start_time)
            if(speed>5):
                    print("Speed: %.20f cm/s" % speed)
                    if(speed>MAX_ALLOWED_SPEED):
                        informPCR()
