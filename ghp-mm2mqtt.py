#!/usr/bin/env python3

import sys
import serial
import paho.mqtt.client as mqtt
import struct
import json
import time
import logging
from ghp_config import *

#logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
_logger = logging.getLogger(__name__)

#modbus message to write, it's emptied upon writing and can be set
#by mqtt MQTT_TOPIC_PREFIX/set topic in on_message()
#turn off 
#writemsg=b'\xF0\x06\x07\xd1\x00\x00'
writemsg=''



# Function to calculate Modbus CRC16
def modbus_crc16(data: bytes) -> int:
    crc = 0xFFFF
    for pos in data:
        crc ^= pos
        for _ in range(8):
            if (crc & 0x0001) != 0:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc

# Function to verify the CRC of a Modbus message
def verify_modbus_crc(data: bytes) -> bool:
    if len(data) < 4:  # Minimal Modbus frame size with CRC
        return False
    received_crc = struct.unpack('<H', data[-2:])[0]  # Last 2 bytes are the CRC
    calculated_crc = modbus_crc16(data[:-2])  # CRC of the data without the last 2 CRC bytes
    _logger.debug(f"received crc: {received_crc} = calculated_crc {calculated_crc}");
    return received_crc == calculated_crc

def publish(slave, op, addr, data):
    data_json = json.dumps(data)
    retain = 2100 <= addr < 2200
    MQTT_TOPIC = f"{MQTT_TOPIC_PREFIX}/{op}/{slave}/{addr}"

    print(f"📤 MQTT: topic={MQTT_TOPIC}, payload={data_json}, retain={retain}")  # ← отладочный вывод

    _logger.info(f"{MQTT_TOPIC}: {data_json}")
    mqtt_client.publish(MQTT_TOPIC, data_json, retain=retain)


def decodeModbus():
    global buffer
    global readAddr
    global writemsg
    global ser
    
    _logger.debug(f"buffer={buffer}")
    buflen=len(buffer)
    if buflen < 8:
        return
    index = buffer.find(240) #find slave 240
    if index < 0 or buflen-index < 8:
        return
    buffer = buffer[index:] #discard all data before
    _logger.debug(f"found on position {index}\nbuffer={buffer}\n")
    if buffer[1] == 3:  # 0x3 read command
     if verify_modbus_crc(buffer[0:8]): #test Read Request (fixed sized)
      readAddr=struct.unpack('>h',buffer[2:4])[0] # valid ReadRequest, save target address
      buffer = buffer[8:]
     else:  #Read response
      psize=buffer[2]+5 # id + 03 + size + data + crc1 +crc2
      if verify_modbus_crc(buffer[0:psize]):
        numshorts=int((psize-5)/2)
        publish(buffer[0],3,readAddr,struct.unpack(f'>{numshorts}h',buffer[3:psize-2]))
        if len(writemsg) > 5: 
          writemsg=writemsg+modbus_crc16(writemsg).to_bytes(2,'little');
          _logger.info(f"WRITE {writemsg}\n")
          ser.write(writemsg)  
          writemsg='';
        buffer = buffer[psize:]
      else:
       buffer = buffer[1:]  #no valid crc, could be xf0x03 sequence in data, skip 1st byte
    elif buffer[1] == 16: # 0x10 write command
      psize=buffer[6]+9 # id + 03 + size + data + crc1 +crc2
      _logger.debug(f"psize={psize} packet={buffer[0:psize]}")
      if buflen > psize and verify_modbus_crc(buffer[0:psize]):
       readAddr=struct.unpack('>h',buffer[2:4])[0]
       numshorts=int((psize-9)/2)
       publish(buffer[0],10,readAddr,struct.unpack(f">{numshorts}h",buffer[7:psize-2]))
       buffer = buffer[psize:]
      else:
       buffer = buffer[1:] #no valid crc, could be xf0x10 sequence in data, skip 1st byte
    else: #not 0x03 or 0x10 skip
     buffer = buffer[1:]
 
    decodeModbus()

def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_TOPIC_PREFIX+"/set/#")

def on_message(client, userdata, msg):
    global writemsg
    _logger.info(f"MQTT received msg.topic={msg.topic} msg.payload={msg.payload}")
    addr= msg.topic.split('/')
    if ( int(addr[3]) >= 2000 and int(addr[3]) <= 2006 ):
     newm=struct.pack(">BBhh",int(addr[2]),6,int(addr[3]),int(msg.payload))
     writemsg=newm
    else:
     _logger.error(f"Write request outside safe range(0x2000-0x2006) msg.topic={msg.topic} msg.payload={msg.payload}")

# Initialize and connect to the MQTT broker with authentication
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)  # Set username and password
# mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
MQTT_BROKER = "192.168.1.220"
MQTT_PORT = 1883
MQTT_USERNAME = "celiv"
MQTT_PASSWORD = "230960"

mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)


mqtt_client.loop_start()
time.sleep(1)




# Вставляем здесь: публикация discovery-сенсоров
# Подключение к MQTT
mqtt_client = mqtt.Client()
mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.loop_start()
time.sleep(1)

# 🔽 Вставь сюда ↓↓↓
import os
import json
import re

def sanitize_topic(topic):
    return topic.replace("/", "_").replace("+", "_").replace("#", "_")

def is_valid_sensor_line(parts):
    if len(parts) < 4:
        return False
    topic, name, unit, device_class = parts[:4]
    if "+" in topic or "#" in topic:
        print(f"⚠️ Пропущено: недопустимый символ в topic → {topic}")
        return False
    if not topic or not name or not unit or not device_class:
        print(f"⚠️ Пропущено: неполная строка → {' '.join(parts)}")
        return False
    return True

def publish_discovery(client, topic, name, unit, device_class):
    sensor_id = sanitize_topic(topic)
    discovery_topic = f"homeassistant/sensor/{sensor_id}/config"
    payload = {
        "name": name,
        "state_topic": topic,
        "unit_of_measurement": unit,
        "value_template": "{{ value_json[0] }}",
        "unique_id": sensor_id,
        "device_class": device_class,
        "device": {
            "identifiers": ["ghp_device"],
            "name": "GHP System"
        }
    }
    client.publish(discovery_topic, json.dumps(payload), retain=True)
    print(f"📤 Discovery опубликован: {discovery_topic}")

# Поиск файла в двух местах
sensor_file = "/usr/src/app/hass-sensors.txt"
if not os.path.exists(sensor_file):
    sensor_file = "/addons/local/ghp-mm2mqtt/hass-sensors.txt"

try:
    with open(sensor_file) as f:
        for line in f:
            parts = line.strip().split()
            if is_valid_sensor_line(parts):
                topic, name, unit, device_class = parts[:4]
                publish_discovery(mqtt_client, topic, name, unit, device_class)
            else:
                print(f"⚠️ Строка пропущена: {line.strip()}")
except FileNotFoundError:
    print(f"❌ Файл не найден: {sensor_file}")



# Далее — основной цикл обработки данных

buffer=bytearray(0)
readAddr=0


# Open serial port
ser = serial.Serial(
    port=SERIAL_PORT,
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=0  # blocking read
)

# Check if the port is open
if ser.is_open:
    _logger.info(f"Serial port {ser.port} opened successfully!")
    ser.reset_input_buffer()
    print(f"✅ Последовательный порт {ser.port} открыт успешно!")
try:
    print("🚀 Скрипт запущен. Ожидаю данные от порта...")
    while True:
        data = ser.read(1)
        data += ser.read(ser.inWaiting())
        if data:
            print(f"📥 Принято: {data.hex()}")
            buffer+=data
            decodeModbus()                
        else:
            print("⏳ Нет данных.")
            _logger.warning("No data received.")
        time.sleep(0.3)             

except KeyboardInterrupt:
    print("🛑 Прерывание: выход из программы...")
    _logger.info("Exiting program...")

finally:
    print("🔌 Порт и MQTT-соединение закрыты.")
    ser.close()
    mqtt_client.disconnect()
    _logger.info("Serial port and MQTT connection closed.")
