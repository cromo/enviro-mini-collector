#!/usr/bin/env python3

# PIL is version 4.0.0 on this install.
# Docs: https://pillow.readthedocs.io/en/4.0.x/index.html
from PIL import ImageFont
from fonts.ttf import RobotoMedium
import logging
import time

from display import Display
from proximity_light_detector import ProximityLightDetector

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

display = Display()
WIDTH, HEIGHT = display.width, display.height

message = 'Wapo!'
font = ImageFont.truetype(font=RobotoMedium, size=25)
size_x, size_y = display.canvas.textsize(message, font)

display.canvas.rectangle((0, 0, WIDTH, HEIGHT), (20, 15, 0))
display.canvas.text(((WIDTH - size_x) / 2, (HEIGHT / 2) - (size_y / 2)), message, font=font, fill=(255, 255, 255))
display.show_buffer()

light_sensor = ProximityLightDetector()

try:
    while True:
        logging.info('Proximity (raw): {:>4}, lux: {}'.format(light_sensor.raw_proximity, light_sensor.lux))
        time.sleep(1)
except KeyboardInterrupt:
    display.turn_off()