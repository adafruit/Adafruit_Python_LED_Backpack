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

from Adafruit_LED_Backpack import AlphaNum4


# Create display instance on default I2C address (0x70) and bus number.
display = AlphaNum4.AlphaNum4()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = AlphaNum4.AlphaNum4(address=0x74, busnum=1)

# On BeagleBone, try busnum=2 if IOError occurs with busnum=1
# display = AlphaNum4.AlphaNum4(address=0x74, busnum=2)

# Initialize the display. Must be called once before using the display.
display.begin()

# Scroll a message across the display
message = 'This is an example of the 4 character alpha-numeric display. THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG? the quick brown fox jumps over the lazy dog!'
pos = 0
print('Press Ctrl-C to quit.')
while True:
    # Clear the display buffer.
    display.clear()
    # Print a 4 character string to the display buffer.
    display.print_str(message[pos:pos+4])
    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
    display.write_display()
    # Increment position. Wrap back to 0 when the end is reached.
    pos += 1
    if pos > len(message)-4:
        pos = 0
    # Delay for half a second.
    time.sleep(0.5)

# Note that the alphanumeric display has the same number printing functions
# as the 7 segment display.  See the sevensegment_test.py example for good
# examples of these functions.
