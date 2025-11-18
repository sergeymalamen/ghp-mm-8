ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
FROM ${BUILD_FROM}

# Устанавливаем Python, pip и venv
RUN apk add --no-cache python3 py3-pip py3-virtualenv

# Рабочая директория
WORKDIR /usr/src/app

# Создаем виртуальное окружение
RUN python3 -m venv /usr/src/app/venv

# Копируем зависимости отдельно (ускоряет сборку)
COPY requirements.txt .

# Устанавливаем зависимости внутри venv
RUN /usr/src/app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Копируем весь аддон
COPY . .

# Права на run.sh
RUN chmod +x /usr/src/app/run.sh

# s6-overlay запускает все сам
ghp_mm_sniffer/rootfs/etc/services.d/ghp-mm-sniffer/run

