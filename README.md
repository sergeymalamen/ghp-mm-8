# GHP mm2mqtt Add-on for Home Assistant

📡 **GHP mm2mqtt** — это локальный Add-on для Home Assistant, который считывает данные с USB-адаптера (Modbus/RS485) и публикует их в MQTT. Поддерживает автоматическое создание сенсоров через MQTT Discovery.

---

## 🚀 Возможности

- Подключение к последовательному порту (FTDI, RS485)
- Приём и разбор бинарных пакетов
- Публикация данных в MQTT-брокер
- Автоматическое создание сенсоров из `hass-sensors.txt`
- Поддержка MQTT Discovery
- Логирование событий и ошибок

---

## 🛠 Установка

1. Поместите папку `ghp-mm2mqtt` в `/addons/local/`
2. Перейдите в **Настройки → Add-ons → ⋮ → Reload**
3. Найдите Add-on в категории **Локальные Add-on'ы**
4. Нажмите **Install → Start**

---

## 📁 Структура

ghp-mm2mqtt/ 
├── Dockerfile 
├── config.json 
├── run.sh 
├── ghp-mm2mqtt.py 
├── ghp_config.py 
├── hass-sensors.txt 
├── icon.png (опционально) 
├── logo.png (опционально) 
├── README.md


---

## 📄 Формат `hass-sensors.txt`

Каждая строка — один сенсор

<topic> <name> <unit> <device_class>


Пример:


GHP/10/240/300 Temperature °C temperature 
GHP/10/240/400 Pressure Pa pressure 
GHP/10/240/500 Humidity % humidity


---

## ⚙️ Настройки

Пока Add-on не имеет UI-настроек. Все параметры задаются в коде:

- MQTT_HOST
- MQTT_PORT
- MQTT_USERNAME
- MQTT_PASSWORD
- SERIAL_PORT

---

## 📞 Обратная связь

Если вы хотите расширить функциональность или нашли ошибку — пишите прямо в чат 😉

---

Хочешь, я помогу с созданием `icon.png` и `logo.png`, чтобы Add-on красиво отображался в магазине?
