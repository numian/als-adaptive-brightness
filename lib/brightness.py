#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

XB_TIME  = 1000
XB_STEPS = 50

current_brightness = False

def set(percentage):

    global current_brightness

    if current_brightness == False or current_brightness != percentage:
        os.system('xbacklight -time %i -steps %i -set %i &' % (XB_TIME, XB_STEPS, percentage) )
        current_brightness = percentage

