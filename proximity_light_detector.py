from ltr559 import LTR559

class ProximityLightDetector:
    def __init__(self, proximity_scale=100):
        self.sensor = LTR559()
        self.proximity_scale = proximity_scale

    @property
    def device_name(self):
        return 'LTR559'

    @property
    def raw_proximity(self):
        return self.sensor.get_proximity()

    @property
    def proximity(self):
        return (2047 - self.raw_proximity) / 2047.0 * self.proximity_scale

    @property
    def lux(self):
        return self.sensor.get_lux()