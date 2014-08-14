#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, time, subprocess

# get current brightness
current_brightness = int(float(subprocess.check_output('xbacklight', shell=True).strip()))

def set(percentage):

    global current_brightness

    if current_brightness == False or abs(current_brightness - percentage) > 5:
        os.system('xbacklight -set %i' % (percentage))
        current_brightness = percentage
