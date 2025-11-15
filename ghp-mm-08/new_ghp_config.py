import json

with open('/data/options.json') as f:
    opts = json.load(f)

SERIAL_PORT = opts.get("serial_port")
MQTT_BROKER = opts.get("mqtt_broker")
MQTT_PORT = opts.get("mqtt_port")
MQTT_USERNAME = opts.get("mqtt_username")
MQTT_PASSWORD = opts.get("mqtt_password")
