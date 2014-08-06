import subprocess
import re
import os

pipe = subprocess.Popen('tail -n 0 -f /var/log/syslog', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

max_value = 332


# initial value
current_brightness = int(float(os.popen('xbacklight').read().strip()))

light_level = int(open('/sys/bus/acpi/devices/ACPI0008:00/ali', 'r').read().strip())
brightness = round(light_level * 100 / max_value)

os.system('xbacklight -set ' + str(brightness))

current_brightness = brightness

print 'initial value ' + str(current_brightness) + '%'

try:
    while True:
        line = pipe.stdout.readline().strip()
        
        match = re.search(r'als_notify\s([0-9]{1,2})\s([0-9a-fA-F]+)', line)
        
        if match:
            
            print line
            
            light_level = int('0x' + match.group(2), 0)
            
            if light_level > max_value:
                print 'new max value: ' + light_level
                brightness = 100
            else:
            
                brightness = round(light_level * 100 / max_value)
                
                if brightness < 10:
                    brightness = 10
                
                if brightness != current_brightness:
                    print 'setting to %s' % brightness
                    os.system('xbacklight -set ' + str(brightness))
                    current_brightness = brightness
            
            
            
except KeyboardInterrupt:
    print ''
    pass
    
