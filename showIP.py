#!/usr/bin/python
# -*- coding: utf-8 -*-

# This script will show the Pi's IP address on the LCD screen. Refreshes every 30 seconds.
# Add this script to the rc.local to enable at boot.

import Adafruit_CharLCD as LCD
import subprocess
import time

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)

# Turn backlight on
lcd.set_backlight(0)

while True:
    ip_addr = str(subprocess.check_output(['hostname', '-I'])).split(' ')[0].replace("b'", "")
    lcd.message('IP Address:\n') 
    lcd.message(ip_addr + '\n')
    time.sleep(30)
    lcd.clear()

