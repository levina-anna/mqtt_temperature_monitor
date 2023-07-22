import paho.mqtt.client as mqtt


# This function is called when the client successfully connects to the MQTT broker.
def on_connect(client, userdata, flags, rc):
    # Print a message indicating successful connection
    print(f"Connected with result code {rc}")
    # Subscribe to the "TEMPERATURE" topic
    client.subscribe("TEMPERATURE")


# This function is called when a message is received from a subscribed topic.
def on_message(client, userdata, msg):
    # Print the received message to the console
    print(f"Received message:  {msg.payload.decode('utf-8')})")


# Create the broker
mqtt_broker = "mqtt.eclipseprojects.io"

# Create the client (smartphone)
client = mqtt.Client("Smartphone")

# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(mqtt_broker)

# Start the MQTT event loop
# The client runs an infinite loop to process MQTT events,
# listening for new messages and invoking the corresponding
# callback functions when necessary.
client.loop_forever()
