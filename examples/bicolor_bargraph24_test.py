# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import time

from Adafruit_LED_Backpack import BicolorBargraph24


# Create display instance on default I2C address (0x70) and bus number.
display = BicolorBargraph24.BicolorBargraph24()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = BicolorBargraph24.BicolorBargraph24(address=0x74, busnum=1)

# On BeagleBone, try busnum=2 if IOError occurs with busnum=1
# display = BicolorBargraph24.BicolorBargraph24(address=0x74, busnum=2)

# Initialize the display. Must be called once before using the display.
display.begin()

# Run through all bars and colors at different brightness levels.
print('Press Ctrl-C to quit.')
brightness = 15
while True:
    # Set display brightness (15 is max, 0 is min).
    display.set_brightness(brightness)
    for i in range(24):
        # Clear the display buffer.
        display.clear()
        # Light up 3 bars, each a different color and position.
        display.set_bar(i,   BicolorBargraph24.RED)
        display.set_bar(i+1, BicolorBargraph24.GREEN)
        display.set_bar(i+2, BicolorBargraph24.YELLOW)
        # Write the display buffer to the hardware.  This must be called to
        # update the actual display LEDs.
        display.write_display()
        # Delay for half a second.
        time.sleep(0.5)
    # Decrease brightness, wrapping back to 15 if necessary.
    brightness -= 1
    if brightness == 0:
        brightness = 15
