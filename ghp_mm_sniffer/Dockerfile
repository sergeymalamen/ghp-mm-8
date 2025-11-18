ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-addon-base:latest
FROM ${BUILD_FROM}


# Установка Python и окружения
RUN apk add --no-cache python3 py3-pip py3-virtualenv

WORKDIR /usr/src/app

# Создаем виртуальное окружение
RUN python3 -m venv /usr/src/app/venv

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN /usr/src/app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы
COPY . .

# Копируем rootfs (обязательно!)
COPY rootfs/ /

# Даём права на запуск скрипта службы
RUN chmod +x /rootfs/etc/services.d/ghp-mm-sniffer/run

# S6-overlay стартует сам, CMD/ENTRYPOINT не нужны
