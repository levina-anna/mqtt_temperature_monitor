# MQTT Temperature Monitor

The "MQTT Temperature Monitor" program is a set of scripts for generating and monitoring temperature data using the MQTT protocol.

## Description

The program consists of three scripts::

- **mqtt_publish1.py**: Script for generating random internal temperature data and publishing it to the "TEMPERATURE" topic of the MQTT broker.
- **mqtt_publish2.py**: Script for generating random external temperature data and publishing it to the "TEMPERATURE" topic of the MQTT broker.
- **mqtt_subscribe.py**:  Script for subscribing to the "TEMPERATURE" topic of the MQTT broker and printing the received messages to the console.

## Usage

1. Install the necessary dependencies by running the command `pip install paho-mqtt`.
2. Run the `mqtt_publish1.py` script to generate and publish internal temperature data.
3. Run the `mqtt_publish2.py` script to generate and publish external temperature data.
4. Run the `mqtt_subscribe.py` script to subscribe to the "TEMPERATURE" topic and receive the data.

## Dependencies

- Python 3.x
- paho-mqtt library

