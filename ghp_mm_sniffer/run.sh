#!/usr/bin/with-contenv bashio

# Чтение параметров
SERIAL_PORT=$(bashio::config 'serial_port')
MQTT_BROKER=$(bashio::config 'mqtt_broker')
MQTT_PORT=$(bashio::config 'mqtt_port')
MQTT_USERNAME=$(bashio::config 'mqtt_username')
MQTT_PASSWORD=$(bashio::config 'mqtt_password')

# Экспортируем переменные
export SERIAL_PORT MQTT_BROKER MQTT_PORT MQTT_USERNAME MQTT_PASSWORD

# Запускаем скрипт
exec python3 /usr/src/app/ghp-mm2mqtt.py

echo "Starting run.sh"
echo "Serial: $SERIAL_PORT"
echo "Broker: $MQTT_BROKER:$MQTT_PORT"
ls -la /usr/src/app
python3 --version
which python3

