import time
import signal
import sys
import RPi.GPIO as GPIO
from datetime import datetime
import smbus
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
GPIO_BEGIN_PIN = 4
GPIO_END_PIN = 17
MAX_ALLOWED_SPEED=40
 
DISTANCE = 10.0 # (in cm) Anpassen, falls notwendig
TIMEOUT = 5 # sek
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def sendMessage1(helpMessage):
   fromaddr = "hafiz031@yandex.com"
   toaddr = "hafiz6036046@gmail.com"
   msg = MIMEMultipart()
   msg['From'] = fromaddr
   msg['To'] = toaddr
   msg['Subject'] = "Help Message"
   body = helpMessage
   msg.attach(MIMEText(body, 'plain'))
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.ehlo()
   server.starttls()
   server.ehlo()
   server.login("hafiz031@yandex.com", "Abcde123")
   text = msg.as_string()
   server.sendmail(fromaddr, toaddr, text)
   server.quit()
   
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
                        sendMessage1("Overspeed Detected")
