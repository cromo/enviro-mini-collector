from display import Display
from proximity_light_detector import ProximityLightDetector
from temperature_pressure_humidity_sensor import TemperaturePressureHumiditySensor

class Enviro:
    def __init__(self, display_rotation=270):
        self.display = Display(rotation=display_rotation)
        self.optical_sensor = ProximityLightDetector()
        self.weather_sensor = TemperaturePressureHumiditySensor()

    @property
    def raw_proximity(self):
        return self.optical_sensor.raw_proximity

    @property
    def proximity(self):
        return self.optical_sensor.proximity

    @property
    def lux(self):
        return self.optical_sensor.lux

    @property
    def raw_temperature(self):
        return self.weather_sensor.raw_temperature

    @property
    def temperature(self):
        return self.weather_sensor.temperature

    @property
    def humidity(self):
        return self.weather_sensor.humidity

    @property
    def pressure(self):
        return self.weather_sensor.pressure