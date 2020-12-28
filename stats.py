#!/usr/bin/env python3

# PIL is version 4.0.0 on this install.
# Docs: https://pillow.readthedocs.io/en/4.0.x/index.html
from PIL import ImageFont
from fonts.ttf import RobotoMedium
import logging

from display import Display

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

try:
    while True:
        pass
except KeyboardInterrupt:
    display.turn_off()