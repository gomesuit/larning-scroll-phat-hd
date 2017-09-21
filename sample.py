#!/usr/bin/env python

import time
import signal

import scrollphathd
from scrollphathd.fonts import font5x7

text = '      Hello World!'

scrollphathd.clear()
scrollphathd.show()

scrollphathd.write_string(text, font=font5x7, brightness=0.1)
length = scrollphathd.write_string(text, x=0, y=0, font=font5x7, brightness=0.1)
time.sleep(0.25)

while length > 0:
    scrollphathd.show()
    scrollphathd.scroll(1)
    length -= 1
    time.sleep(0.02)

scrollphathd.clear()
scrollphathd.show()
