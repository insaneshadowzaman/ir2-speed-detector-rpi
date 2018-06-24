import time
import RPi.GPIO as GPIO

GPIO_BEGIN_PIN=4
GPIO_END_PIN=17

DISTANCE=10.0
TIMEOUT=5

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

if __name__=='__main__':
	GPIO.setup(GPIO_BEGIN_PIN,GPIO.IN)
	GPIO.setup(GPIO_END_PIN,GPIO.IN)
	start_time,end_time=0,0

	while GPIO.input(GPIO_BEGIN_PIN)==GPIO.LOW:
		time.sleep(0.001)
		start_time=time.time()
	end_time=0

	while GPIO.input(GPIO_END_PIN)==GPIO.LOW and time.time()-start_time<TIMEOUT:
		time.sleep(0.001)
else:
	if time.time()-start_time>=TIMEOUT:
		print("Timeout")
		exit()
	else:
		end_time=time.time()
		speed=DISTANCE/(end_time-start_time)
		print("Geschwindigkeit: %.2f cm/s" % speed)


