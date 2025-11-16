#!/usr/bin/with-contenv bashio

# Активация виртуального окружения
. /venv/bin/activate

echo "🔍 Проверка bashio:"
which bashio || echo "❌ bashio не найден"

# Проверка конфигурации
echo "📄 Проверка /data/options.json:"
cat /data/options.json || echo "❌ Файл не найден или пуст"

# Чтение параметров
SERIAL_PORT=$(bashio::config 'serial_port')
MQTT_BROKER=$(bashio::config 'mqtt_broker')
MQTT_PORT=$(bashio::config 'mqtt_port')
MQTT_USERNAME=$(bashio::config 'mqtt_username')
MQTT_PASSWORD=$(bashio::config 'mqtt_password')

export SERIAL_PORT MQTT_BROKER MQTT_PORT MQTT_USERNAME MQTT_PASSWORD

# Отладка
echo "Starting run.sh"
echo "Serial: $SERIAL_PORT"
echo "Broker: $MQTT_BROKER:$MQTT_PORT"
ls -la /usr/src/app
python3 --version
which python3

# Запуск скрипта
exec python3 /usr/src/app/ghp-mm2mqtt.py
