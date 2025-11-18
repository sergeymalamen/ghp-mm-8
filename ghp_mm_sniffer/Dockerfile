ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
FROM ${BUILD_FROM}

# Устанавливаем Python, pip, venv
RUN apk add --no-cache python3 py3-pip py3-virtualenv

# Рабочая директория
WORKDIR /usr/src/app

# Создаём виртуальное окружение
RUN python3 -m venv /usr/src/app/venv

# Копируем зависимости отдельно
COPY requirements.txt .

# Устанавливаем зависимости в venv
RUN /usr/src/app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Копируем весь аддон
COPY . .

# Делаем run исполняемым
RUN chmod +x /etc/services.d/ghp-mm-sniffer/run

# Стартуем s6-overlay
CMD [ "/init" ]
