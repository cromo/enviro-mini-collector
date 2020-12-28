#!/usr/bin/env python3

import ST7735 as enviro_lcd
# PIL is version 4.0.0 on this install.
# Docs: https://pillow.readthedocs.io/en/4.0.x/index.html
from PIL import Image, ImageDraw, ImageFont
from fonts.ttf import RobotoMedium
import logging

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

MEGA = 1000 * 1000

class Display:
    def __init__(self, rotation=270):
        self.display = enviro_lcd.ST7735(
            port=0,
            cs=1,
            dc=9,
            backlight=12,
            rotation=270,
            spi_speed_hz=10 * MEGA
        )
        self.back_buffer = Image.new('RGB', self.size, color=(0, 0, 0))
        self.canvas = ImageDraw.Draw(self.back_buffer)

    def show_buffer(self):
        self.display.display(self.back_buffer)

    def turn_off(self):
        self.display.display(Image.new('RGB', self.size, color=(0, 0, 0)))
        self.display.set_backlight(0)

    @property
    def width(self):
        return self.display.width

    @property
    def height(self):
        return self.display.height

    @property
    def size(self):
        return self.width, self.height

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