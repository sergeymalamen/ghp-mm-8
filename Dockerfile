FROM ghcr.io/home-assistant/aarch64-base:latest

RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-pyserial \
    py3-paho-mqtt

COPY run.sh /run.sh
COPY ghp-mm2mqtt.py /ghp-mm2mqtt.py
COPY ghp_config.py /ghp_config.py

CMD ["/run.sh"]
