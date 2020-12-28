import ST7735 as enviro_lcd
from PIL import Image, ImageDraw

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
    def device_name(self):
        return 'ST7735'

    @property
    def width(self):
        return self.display.width

    @property
    def height(self):
        return self.display.height

    @property
    def size(self):
        return self.width, self.height