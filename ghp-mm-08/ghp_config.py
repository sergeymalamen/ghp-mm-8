#serial port
#SERIAL_PORT = '/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_BG009VVA-if00-port0'

# MQTT broker settings
#MQTT_BROKER = "localhost"  # Replace with your broker address
#MQTT_PORT = 1883  # Default MQTT port
#MQTT_TOPIC_PREFIX= "GHP"
#MQTT_USERNAME = "celiv"  # Replace with your MQTT username
#MQTT_PASSWORD = "230960"  # Replace with your MQTT password


import json

with open('/data/options.json') as f:
    opts = json.load(f)

SERIAL_PORT = opts.get("serial_port")
MQTT_BROKER = opts.get("mqtt_broker")
MQTT_PORT = opts.get("mqtt_port")
MQTT_USERNAME = opts.get("mqtt_username")
MQTT_PASSWORD = opts.get("mqtt_password")
