from collections import deque
from statistics import mean

from bme280 import BME280

class TemperaturePressureHumiditySensor:
    def __init__(self, cpu_temp_compensation_factor=2.25):
        self.sensor = BME280()
        self.cpu_temperature_compensation_factor = cpu_temp_compensation_factor
        self.cpu_temperatures = deque([self._cpu_temperature] * 5, 5)

    @property
    def device_name(self):
        return 'BME280'

    @property
    def raw_temperature(self):
        """Read the temperature off the sensor in degrees Celsius

        Does not bias for CPU temp, so this may be hotter than the surrounding
        environment.
        """
        return self.sensor.get_temperature()

    @property
    def temperature(self):
        """Temperature reading compensated for CPU temperature in degrees Celsius"""
        # Adopted from the enviroplus examples, which are adapted from this
        # article:
        # https://medium.com/@InitialState/tutorial-review-enviro-phat-for-raspberry-pi-4cd6d8c63441
        self.cpu_temperatures.append(self._cpu_temperature)
        raw_temperature = self.raw_temperature
        return raw_temperature - (mean(self.cpu_temperatures) - raw_temperature) / self.cpu_temperature_compensation_factor


    @property
    def humidity(self):
        """Read the relative humidity sensor in precent"""
        return self.sensor.get_humidity()

    @property
    def pressure(self):
        """Reads the pressure sensor in hPa"""
        return self.sensor.get_pressure()

    @property
    def _cpu_temperature(self):
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            return int(f.read()) / 1000.0
