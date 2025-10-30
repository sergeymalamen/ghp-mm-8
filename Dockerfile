FROM ghcr.io/home-assistant/aarch64-base:latest

RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-serial \
    py3-paho-mqtt

WORKDIR /usr/src/app

COPY run.sh .
COPY ghp-mm2mqtt.py .
COPY ghp_config.py .
COPY hass-sensors.txt .

RUN chmod +x run.sh
CMD ["sh", "./run.sh"]
