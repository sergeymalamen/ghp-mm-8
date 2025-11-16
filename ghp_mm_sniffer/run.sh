#!/usr/bin/with-contenv bashio

echo "Starting run.sh"
ls -la /usr/src/app
cat /data/options.json
exec python3 /usr/src/app/ghp-mm2mqtt.py

