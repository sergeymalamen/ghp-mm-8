ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-pip py3-virtualenv

WORKDIR /usr/src/app

COPY requirements.txt .
RUN python3 -m venv /usr/src/app/venv
RUN /usr/src/app/venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /rootfs/etc/services.d/ghp-mm-sniffer/run
