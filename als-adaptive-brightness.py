#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from lib import als, brightness, trayicon


def checkPercentage(value):

    int_value = int(value)
    
    if int_value < 0 or int_value > 100:
        raise argparse.ArgumentTypeError('%s is an invalid percentage. Must be between 0 and 100.' % value)
        
    return int_value


parser = argparse.ArgumentParser(description='Adapts backlight to Ambient Light Sensor value')
parser.add_argument('--max-als-value', help='Value from ALS above which the screen brightness will be 100%%', default=300, type=int)
parser.add_argument('--min-brightness', help='The minimum brightness percentage', default=15, type=checkPercentage)

results = parser.parse_args()


MAX_ALS_VALUE = results.max_als_value
MIN_BRIGHTNESS_VALUE = results.min_brightness

def aliValueToPercentage(ali_value):

    percentage = round(ali_value * 100 / MAX_ALS_VALUE)

    if percentage < MIN_BRIGHTNESS_VALUE:
        percentage = MIN_BRIGHTNESS_VALUE
    elif percentage > 100:
        percentage = 100

    return percentage
    

def setBrightness(ali_value):
    percentage = aliValueToPercentage(ali_value)
    brightness.set(percentage)


if __name__ == '__main__':

    try:
        als.start(setBrightness)
        trayicon.start()
        als.stop()
        
    except KeyboardInterrupt:
        als.stop()
        print ''
        pass
    
