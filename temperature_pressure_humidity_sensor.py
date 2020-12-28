from bme280 import BME280

class TemperaturePressureHumiditySensor:
    def __init__(self):
        self.sensor = BME280()

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
    def humidity(self):
        """Read the relative humidity sensor in precent"""
        return self.sensor.get_humidity()

    @property
    def pressure(self):
        """Reads the pressure sensor in hPa"""
        return self.sensor.get_pressure()