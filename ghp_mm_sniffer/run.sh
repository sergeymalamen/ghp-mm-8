#!/usr/bin/with-contenv bashio

# Активация виртуального окружения
. /venv/bin/activate

echo "✅ run.sh запущен как PID: $$"
echo "📄 Проверка /data/options.json:"
cat /data/options.json || echo "❌ Файл не найден или пуст"

# Чтение параметров конфигурации
SERIAL_PORT=$(bashio::config 'serial_port')
MQTT_BROKER=$(bashio::config 'mqtt_broker')
MQTT_PORT=$(bashio::config 'mqtt_port')
MQTT_USERNAME=$(bashio::config 'mqtt_username')
MQTT_PASSWORD=$(bashio::config 'mqtt_password')

# Экспорт переменных окружения
export SERIAL_PORT MQTT_BROKER MQTT_PORT MQTT_USERNAME MQTT_PASSWORD

# Отладочная информация
echo "🔧 Конфигурация:"
echo "Serial: $SERIAL_PORT"
echo "Broker: $MQTT_BROKER:$MQTT_PORT"
echo "User: $MQTT_USERNAME"

# Запуск основного скрипта
exec python3 /usr/src/app/ghp-mm2mqtt.py
