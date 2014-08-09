#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess, re, os

READ_COMMAND = 'tail -n 0 -f /var/log/syslog'
ALI_PATH     = '/sys/bus/acpi/devices/ACPI0008:00/ali'

def startReading(callback):
    
    # read from als device
    callback(_readFirstValue())

    
    # start main loop
    pipe = subprocess.Popen(READ_COMMAND, shell = True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
    try:
        while True:
        
            light_level = _readValueFromNotification(pipe.stdout.readline().strip())
            
            if light_level > -1:
                callback(light_level);
            
                
    except KeyboardInterrupt:
        print ''
        pass

    
def _readFirstValue():
    return int(open(ALI_PATH, 'r').read().strip())
    

def _readValueFromNotification(line):
    match = re.search(r'als_notify\s([0-9]{1,2})\s([0-9a-fA-F]+)', line)
            
    if match:
        light_level = int('0x' + match.group(2), 0)
        return light_level        
    
    return -1


if __name__ == '__main__':
    
    def printB(value):
        print "ALI: %i" % value

    startReading(printB)
