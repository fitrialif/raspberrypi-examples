#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
this script demos the graphic character LCD with 4 Buttons.
it requires the RPLCD module. install with:
sudo pip install RPLCD

"""

from __future__ import print_function, division, absolute_import, unicode_literals

import sys

from RPLCD import CharLCD
from RPLCD import Alignment, CursorMode, ShiftMode
from RPLCD import cursor, cleared
import RPi.GPIO as GPIO
import time


try:
    input = raw_input
except NameError:
    pass

try:
    unichr = unichr
except NameError:
    unichr = chr


def initButtons():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def checkSwitch():
	v0 = not GPIO.input(4)
	v1 = not GPIO.input(23)
	v2 = not GPIO.input(10)
	v3 = not GPIO.input(9)
	return v3, v0, v1, v2
	#return v0, v1, v2, v3



#lcd = CharLCD(cols=16, rows=2)
#lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24], numbering_mode=GPIO.BOARD, cols=20, rows=4, dotsize=8)
lcd = CharLCD(pin_rs=7, pin_e=8, pins_data=[17, 18, 27, 22], numbering_mode=GPIO.BCM, cols=16, rows=2, dotsize=8)

lcd.write_string('Hi :)')
lcd.home()


initButtons()

while (True):
	#print(checkSwitch())
	v = checkSwitch()
	time.sleep(0.5)
	lcd.home()
	lcd.clear()
	lcd.write_string(str(v))
















"""
input('Display should be blank. ')

lcd.cursor_mode = CursorMode.blink
input('The cursor should now blink. ')

lcd.cursor_mode = CursorMode.line
input('The cursor should now be a line. ')

lcd.write_string('Hello world!')
input('"Hello world!" should be on the LCD. ')

assert lcd.cursor_pos == (0, 12), 'cursor_pos should now be (0, 12)'

lcd.cursor_pos = (0, 15)
lcd.write_string('1')
lcd.cursor_pos = (1, 15)
lcd.write_string('2')
assert lcd.cursor_pos == (0, 0), 'cursor_pos should now be (0, 0)'
input('Lines 1 and 2 should now be labelled with the right numbers on the right side. ')

lcd.clear()
input('Display should now be clear, cursor should be at initial position. ')

lcd.cursor_pos = (0, 5)
lcd.write_string('12345')
input('The string should have a left offset of 5 characters. ')

lcd.write_shift_mode = ShiftMode.display
lcd.cursor_pos = (1, 5)
lcd.write_string('12345')
input('Both strings should now be at column 0. ')

lcd.write_shift_mode = ShiftMode.cursor
lcd.cursor_pos = (1, 5)
lcd.write_string(lcd.write_shift_mode.name)
input('The string "cursor" should now be on the second row, column 0. ')

lcd.home()
input('Cursor should now be at initial position. Everything should be shifted to the right by 5 characters. ')

with cursor(lcd, 1, 15):
    lcd.write_string('X')
input('The last character on the LCD should now be an "X"')

lcd.display_enabled = False
input('Display should now be blank. ')

with cleared(lcd):
    lcd.write_string('Eggs, Ham\n\rand Spam')
lcd.display_enabled = True
input('Display should now show "Eggs, Ham and Spam" with a line break after "Ham". ')

lcd.shift_display(4)
input('Text should now be shifted to the right by 4 characters. ')
lcd.shift_display(-4)
input('Shift should now be undone. ')

lcd.text_align_mode = Alignment.right
lcd.write_string(' Spam')
input('The word "Spam" should now be inverted. ')

lcd.text_align_mode = Alignment.left
lcd.write_string(' Wurscht')
input('The word "mapS" should now be replaced with "Wurscht". ')

lcd.clear()
lcd.write_string('1\n')
lcd.write_string('2\n')
lcd.cursor_pos = (0, 2)
lcd.write_string('3\n')
lcd.write_string('4')
lcd.cursor_pos = (0, 4)
lcd.write_string('5\n')
lcd.write_string('6')
input('The numbers 1-6 should now be displayed in a zig zag line starting in the top left corner. ')

lcd.clear()
lcd.write_string('This will wrap around both lines')
input('Text should nicely wrap around lines. ')

lcd.clear()
lcd.cursor_mode = CursorMode.hide
lcd.write_string('Paris: 21{deg}C\n\rZ{uuml}rich: 18{deg}C'.format(deg=unichr(176), uuml=unichr(129)))
print('Text should now show "Paris: 21°C, Zürich: 18°C" without any encoding issues.', end='')
input()

# Test custom chars
lcd.clear()
happy = (0b00000, 0b01010, 0b01010, 0b00000, 0b10001, 0b10001, 0b01110, 0b00000)
sad = (0b00000, 0b01010, 0b01010, 0b00000, 0b01110, 0b10001, 0b10001, 0b00000)
lcd.create_char(0, sad)
lcd.write_string(unichr(0))
lcd.create_char(1, happy)
lcd.write_string(unichr(1))
input('You should now see a sad and a happy face next to each other. ')
lcd.create_char(0, happy)
lcd.home()
lcd.write_string(unichr(0))
input('Now both faces should be happy. ')
"""


print('done.')

