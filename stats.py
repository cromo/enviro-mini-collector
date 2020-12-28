#!/usr/bin/env python3

# PIL is version 4.0.0 on this install.
# Docs: https://pillow.readthedocs.io/en/4.0.x/index.html
from PIL import ImageFont
from fonts.ttf import RobotoMedium
import logging
import time

from display import Display
from proximity_light_detector import ProximityLightDetector
from temperature_pressure_humidity_sensor import TemperaturePressureHumiditySensor

from enviro import Enviro

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

# display = Display()
enviro = Enviro()
WIDTH, HEIGHT = enviro.display.width, enviro.display.height

message = 'Wapo!'
font = ImageFont.truetype(font=RobotoMedium, size=25)
size_x, size_y = enviro.display.canvas.textsize(message, font)

enviro.display.canvas.rectangle((0, 0, WIDTH, HEIGHT), (20, 15, 0))
enviro.display.canvas.text(((WIDTH - size_x) / 2, (HEIGHT / 2) - (size_y / 2)), message, font=font, fill=(255, 255, 255))
enviro.display.show_buffer()

try:
    while True:
        logging.info('prox: {:.0f}, lux: {}, temp: {:.1f}C, humidity: {:.0f}%, pressure: {:.0f}hPa'.format(enviro.proximity, enviro.lux, enviro.raw_temperature, enviro.humidity, enviro.pressure))
        time.sleep(1)
except KeyboardInterrupt:
    enviro.display.turn_off()