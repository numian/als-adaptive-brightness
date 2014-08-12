#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, math

current_brightness = False

def set(percentage):

    global current_brightness

    if current_brightness == False or abs(current_brightness - percentage) > 5:
        os.system('xbacklight -steps 2 -set %i' % (percentage))
        current_brightness = percentage
