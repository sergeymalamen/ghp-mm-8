ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
FROM ${BUILD_FROM}

# Устанавливаем Python и venv
RUN apk add --no-cache python3 py3-pip py3-virtualenv

# Создаём рабочую директорию
WORKDIR /usr/src/app
COPY . .

# Создаём виртуальное окружение и активируем его
RUN python3 -m venv /venv \
    && . /venv/bin/activate \
    && pip install --no-cache-dir -r requirements.txt

# Перемещаем run.sh в /usr/bin
RUN chmod +x /usr/src/app/run.sh \
    && mv /usr/src/app/run.sh /usr/bin/run.sh
