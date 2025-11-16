import json

try:
    with open('/data/options.json') as f:
        opts = json.load(f)
        print("✅ Конфигурация загружена:", opts)
except Exception as e:
    print("❌ Ошибка при чтении /data/options.json:", e)
    opts = {}

# Проверка обязательных параметров
required_keys = ["serial_port", "mqtt_broker", "mqtt_port"]
for key in required_keys:
    if key not in opts or not opts[key]:
        print(f"⚠️ Отсутствует обязательный параметр: {key}")

# Присваиваем переменные
SERIAL_PORT = opts.get("serial_port")
MQTT_BROKER = opts.get("mqtt_broker")
MQTT_PORT = opts.get("mqtt_port")
MQTT_USERNAME = opts.get("mqtt_username")
MQTT_PASSWORD = opts.get("mqtt_password")
