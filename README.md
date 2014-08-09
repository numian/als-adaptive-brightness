als-adaptive-brightness
===================

Hopefully, it will change the screen backlight according to the ambient light sensor value (ALS)


Requires:
    - this kernel module [https://github.com/victorenator/als](https://github.com/victorenator/als)
    - xbacklight (on Debian derivatives: apt-get install xbacklight)
    - Python GTK (python-gtk2; for the tray icon)

Works on my laptop :) (Samsung NP900X3C)


```bash
usage: als-adaptive-brightness.py [-h] [--max-als-value MAX_ALS_VALUE]
                                  [--min-brightness MIN_BRIGHTNESS]

Adapts backlight to Ambient Light Sensor value

optional arguments:
  -h, --help            show this help message and exit
  --max-als-value MAX_ALS_VALUE
                        Value from ALS above which the screen brightness will
                        be 100%
  --min-brightness MIN_BRIGHTNESS
                        The minimum brightness percentage
```



<small>Icon made by [Elegant Themes](http://www.elegantthemes.com/) from [http://www.flaticon.com/](http://www.flaticon.com/)</small>
