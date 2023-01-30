import time
import board
import digitalio
import analogio
import adafruit_dht

humidity_trigger = 55
relay_delay = 600

print("Intializing µPico")

relay = digitalio.DigitalInOut(board.GP19)
relay.direction = digitalio.Direction.OUTPUT
dht = adafruit_dht.DHT22(board.GP21)

relay.value = False

now = time.time()-relay_delay

while(True):
	time.sleep(1)
	try:
		#print(dht.temperature)
		#print(dht.humidity)
		if dht.humidity > humidity_trigger:
			if relay.value is False:
				if (now+relay_delay) < time.time():
					print("Toggled relay on")
					relay.value = True
					now = time.time()
				else:
					print("Waiting for ... ",now+600-time.time()," seconds")
		else:
			if relay.value is True:
				print("Toggled relay off")
				relay.value = False
				now = time.time()
	except RuntimeError as e:
		print("DHT Read err", e.arg)
