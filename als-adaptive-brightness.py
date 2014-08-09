#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import als, brightness

import argparse


parser = argparse.ArgumentParser(description='Adapts backlight to Ambient Light Sensor value')
parser.add_argument('--max-als-value', help='Value from ALS above which the screen brightness will be 100%%', default=300, type=int)
parser.add_argument('--min-brightness', help='The minimum brightness percentage', default=15, type=int)

results = parser.parse_args()

MAX_ALS_VALUE = results.max_als_value
MIN_BRIGHTNESS_VALUE = results.min_brightness

def aliValueToPercentage(ali_value):

    percentage = round(ali_value * 100 / MAX_ALS_VALUE)

    if percentage < MIN_BRIGHTNESS_VALUE:
        percentage = MIN_BRIGHTNESS_VALUE

    return percentage
    

def setBrightness(ali_value):
    percentage = aliValueToPercentage(ali_value)
    
    brightness.set(percentage)


if __name__ == '__main__':
    als.startReading(setBrightness)

