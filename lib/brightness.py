#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, time, subprocess


# get current brightness
current_brightness = int(float(subprocess.check_output('xbacklight', shell=True).strip()))


def set(percentage):

    global current_brightness

    if current_brightness == False or abs(current_brightness - percentage) > 5:
    
        if current_brightness == False:
            setWithXBacklight(percentage)
            current_brightness = percentage
        else:
        
            if current_brightness > percentage:
                inc = -1
            else:
                inc = 1
                
            while current_brightness != percentage:
                current_brightness += inc
                setWithXBacklight(current_brightness)
                time.sleep(0.01)


def setWithXBacklight(value):
    os.system('xbacklight -steps 1 -time 0 -set %i' % (value))
    #~ print 'xbacklight -steps 1 -time 0 -set %i' % (value)