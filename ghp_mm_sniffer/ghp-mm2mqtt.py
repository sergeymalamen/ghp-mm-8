import os
import time
import serial
import paho.mqtt.client as mqtt

MQTT_BROKER = os.getenv("MQTT_BROKER")
MQTT_PORT = int(os.getenv("MQTT_PORT"))
MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")
SERIAL_PORT = os.getenv("SERIAL_PORT")

print("Starting GHP-MM Sniffer")
print("Serial port:", SERIAL_PORT)

client = mqtt.Client()

if MQTT_USERNAME:
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

ser = serial.Serial(SERIAL_PORT, 9600, timeout=1)

while True:
    line = ser.readline().decode(errors='ignore').strip()
    if line:
        print("RX:", line)
        client.publish("ghp_mm/raw", line)
    time.sleep(0.1)
