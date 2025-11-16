# Используем базовый образ Home Assistant с s6-overlay
ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
FROM ${BUILD_FROM}

# Устанавливаем Python и зависимости
RUN apk add --no-cache python3 py3-pip

# Создаём рабочую директорию и копируем файлы
WORKDIR /usr/src/app
COPY . .

# Устанавливаем зависимости из requirements.txt
#RUN pip3 install --no-cache-dir -r requirements.txt

# Перемещаем run.sh в /usr/bin для s6-overlay
RUN chmod +x /usr/src/app/run.sh \
    && mv /usr/src/app/run.sh /usr/bin/run.sh

# Указываем, что запуск будет через s6-overlay (по умолчанию)
# Никакой CMD не нужен — s6 сам запустит /usr/bin/run.sh
