from ltr559 import LTR559

class ProximityLightDetector:
    def __init__(self):
        self.sensor = LTR559()

    @property
    def device_name(self):
        return 'LTR559'

    @property
    def raw_proximity(self):
        return self.sensor.get_proximity()

    @property
    def lux(self):
        return self.sensor.get_lux()