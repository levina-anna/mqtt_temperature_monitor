import paho.mqtt.client as mqtt
from random import randrange, uniform
import time


# Create the broker
mqtt_broker = "mqtt.eclipseprojects.io"

# Create the client and give it the name "Temperature_Inside"
client = mqtt.Client("Temperature_Inside")

# Connect to the broker
client.connect(mqtt_broker)

# Continuously publish temperature readings to the broker
while True:
	# Generate a random number between 20 and 21 - inside temperature
	rand_number = uniform(20.0, 21.0)
	# Publish the random number
	client.publish("TEMPERATURE", rand_number)
	# Print the number to the console, in "TEMPERATURE" topic
	print(f"Just published {rand_number} to Topic TEMPERATURE")
	# Sleep for 1 second
	time.sleep(1)
