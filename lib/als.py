#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, os, threading, time

ALI_PATH = '/sys/bus/iio/devices/iio:device0/in_illuminance_raw'

class ALSEventReader(threading.Thread):

    stop_flag = False

    def run(self):
        
        while self.stop_flag == False:
            self.callback(self._readFromALI())
            time.sleep(2)
    
    
    def setCallback(self, callback):
        self.callback = callback
    
    
    def _readFromALI(self):
        return int(open(ALI_PATH, 'r').read().strip())
    

    def stop(self):
        self.stop_flag = True


reader = ALSEventReader()

def start(callback):
    global reader
    reader.setCallback(callback)
    reader.start()


def stop():
    global reader
    reader.stop()


if __name__ == '__main__':
    
    def printB(value):
        print "ALI: %i" % value

    start(printB)
