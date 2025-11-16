ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
FROM ${BUILD_FROM}

# Устанавливаем Python и pip
RUN apk add --no-cache python3 py3-pip

# Рабочая директория
WORKDIR /usr/src/app

# Копируем файлы аддона
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# Делаем скрипт запуска исполняемым
RUN chmod +x /usr/src/app/run.sh

# ВАЖНО: указываем обычный CMD, без venv
CMD ["/usr/src/app/run.sh"]
