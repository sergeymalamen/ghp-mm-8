ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-pip py3-virtualenv

WORKDIR /usr/src/app

RUN python3 -m venv /usr/src/app/venv

COPY requirements.txt .

RUN /usr/src/app/venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

COPY rootfs/ /

RUN chmod +x /etc/services.d/ghp-mm-sniffer/run
