#!/bin/sh
echo "🚀 Запуск скрипта"
. /usr/src/app/venv/bin/activate
python3 /usr/src/app/ghp-mm2mqtt.py

#Конфигурирование

#CONFIG_PATH=/data/options.json

#MQTT_HOST=$(jq -r '.mqtt_host' $CONFIG_PATH)
#MQTT_PORT=$(jq -r '.mqtt_port' $CONFIG_PATH)
#MQTT_USER=$(jq -r '.mqtt_username' $CONFIG_PATH)
#MQTT_PASS=$(jq -r '.mqtt_password' $CONFIG_PATH)
#MQTT_PREFIX=$(jq -r '.mqtt_topic_prefix' $CONFIG_PATH)

#exec python3 /ghp-mm2mqtt.py \
#  --mqtt-host "$MQTT_HOST" \
#  --mqtt-port "$MQTT_PORT" \
#  --mqtt-user "$MQTT_USER" \
#  --mqtt-pass "$MQTT_PASS" \
#  --mqtt-prefix "$MQTT_PREFIX"
