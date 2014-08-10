#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk, os

TRAY_ICON = os.path.dirname(os.path.realpath(__file__)) + '/../img/trayicon.svg'

class TrayIcon:
    def __init__(self, thread):
        self.tray = gtk.StatusIcon()
        self.tray.set_from_file(TRAY_ICON) 
        self.tray.connect('popup-menu', self.on_right_click)
        self.tray.set_tooltip(('ALS Adaptive Brightness'))
        
        self.thread = thread

    def on_right_click(self, icon, event_button, event_time):
        self.make_menu(event_button, event_time)

    def make_menu(self, event_button, event_time):
        menu = gtk.Menu()

        # add quit item
        quit = gtk.MenuItem("Quit")
        quit.show()
        menu.append(quit)
        quit.connect('activate', self.tquit)

        menu.popup(None, None, gtk.status_icon_position_menu,
                   event_button, event_time, self.tray)
                   
    def tquit(self, a):
        gtk.main_quit()
        self.thread._Thread__stop()
        


def start(thread):
    TrayIcon(thread)
    gtk.main()


if __name__ == '__main__':
    start()