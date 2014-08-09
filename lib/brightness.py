#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


XB_TIME  = 1000
XB_STEPS = 50

def set(percentage):
    os.system('xbacklight -time %i -steps %i -set %i' % (XB_TIME, XB_STEPS, percentage) )

