#!/usr/bin/env python3

import argparse, logging, socket, time
import requests
from enviro import Enviro

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

def main(server, sampling_interval_seconds=60):
    enviro = Enviro()
    # In the future the screen might be used to show recent readings and network
    # connectivity. For now, turn it off to save some heat and avoid damaging
    # the screen.
    enviro.display.turn_off()

    host = socket.gethostname()
    samplers = [
        sampler(host, enviro.optical_sensor.device_name, "12-bit ADC", lambda: enviro.optical_sensor.raw_proximity),
        sampler(host, enviro.optical_sensor.device_name, "lx", lambda: enviro.optical_sensor.lux),
        sampler(host, enviro.weather_sensor.device_name, "C (raw)", lambda: enviro.weather_sensor.raw_temperature),
        sampler(host, enviro.weather_sensor.device_name, "C (adjusted)", lambda: enviro.weather_sensor.temperature),
        sampler(host, enviro.weather_sensor.device_name, "%", lambda: enviro.weather_sensor.humidity),
        sampler(host, enviro.weather_sensor.device_name, "hPa", lambda: enviro.weather_sensor.pressure),
    ]

    try:
        while True:
            samples = [sample() for sample in samplers]
            request = requests.post('{}/sensors/readings'.format(server), json=samples)
            logging.info('Got {} sending {}'.format(request.status_code, samples))
            time.sleep(sampling_interval_seconds)
    except KeyboardInterrupt:
        # End the script without a backtrace if interrupted.
        pass

def unix_time_millis():
    return int(time.time() * 1000)

def sampler(host, sensor, unit, read_sample):
    def sample():
        measurement = read_sample()
        return {
            'timestamp': unix_time_millis(),
            'host': host,
            'sensor': sensor,
            'measurement': measurement,
            'unit': unit
        }
    return sample

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Collects data from an enviro pHAT')
    parser.add_argument('--server', required=True, help='The server to post results to, including protocol and port')
    parser.add_argument('--sample-period', type=float, default=60, help='The time between sample reads in seconds')
    args = parser.parse_args()
    main(args.server, args.sample_period)