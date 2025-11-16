#!/usr/bin/with-contenv bashio

# Чтение параметров из options.json
SERIAL_PORT=$(bashio::config 'serial_port')
MQTT_BROKER=$(bashio::config 'mqtt_broker')
MQTT_PORT=$(bashio::config 'mqtt_port')
MQTT_USERNAME=$(bashio::config 'mqtt_username')
MQTT_PASSWORD=$(bashio::config 'mqtt_password')

# Экспортируем переменные в окружение (если нужно)
export SERIAL_PORT MQTT_BROKER MQTT_PORT MQTT_USERNAME MQTT_PASSWORD

# Запускаем скрипт
exec python3 /usr/src/ghp-mm2mqtt.py

#echo "🚀 Запуск скрипта"
#. /usr/src/app/venv/bin/activate
#python3 /usr/src/app/ghp-mm2mqtt.py
