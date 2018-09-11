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

from Adafruit_LED_Backpack import SevenSegment


# Create display instance on default I2C address (0x70) and bus number.
display = SevenSegment.SevenSegment()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = SevenSegment.SevenSegment(address=0x74, busnum=1)

# On BeagleBone, try busnum=2 if IOError occurs with busnum=1
# display = SevenSegment.SevenSegment(address=0x74, busnum=2)

# Initialize the display. Must be called once before using the display.
display.begin()

# Keep track of the colon being turned on or off.
colon = False

# Run through different number printing examples.
print('Press Ctrl-C to quit.')
numbers = [0.0, 1.0, -1.0, 0.55, -0.55, 10.23, -10.2, 100.5, -100.5]
while True:
    # Print floating point values with default 2 digit precision.
    for i in numbers:
        # Clear the display buffer.
        display.clear()
        # Print a floating point number to the display.
        display.print_float(i)
        # Set the colon on or off (True/False).
        display.set_colon(colon)
        # Write the display buffer to the hardware.  This must be called to
        # update the actual display LEDs.
        display.write_display()
        # Delay for a second.
        time.sleep(1.0)
    # Print the same numbers with 1 digit precision.
    for i in numbers:
        display.clear()
        display.print_float(i, decimal_digits=1)
        display.set_colon(colon)
        display.write_display()
        time.sleep(1.0)
    # Print the same numbers with no decimal digits and left justified.
    for i in numbers:
        display.clear()
        display.print_float(i, decimal_digits=0, justify_right=False)
        display.set_colon(colon)
        display.write_display()
        time.sleep(1.0)
    # Run through some hex digits.
    for i in range(0xFF):
        display.clear()
        display.print_hex(i)
        display.set_colon(colon)
        display.write_display()
        time.sleep(0.25)
    # Run through hex digits with an inverted (flipped upside down)
    # display.
    display.set_invert(True)
    for i in range(0xFF):
        display.clear()
        display.print_hex(i)
        display.set_colon(colon)
        display.write_display()
        time.sleep(0.25)
    display.set_invert(False)
    # For the large 1.2" 7-segment display only there are extra functions to
    # turn on/off the left side colon and the fixed decimal point.  Uncomment
    # to try them out:
    # To turn on the left side colon:
    #display.set_left_colon(True)
    # To turn off the left side colon:
    #display.set_left_colon(False)
    # To turn on the fixed decimal point (in upper right in normal orientation):
    #display.set_fixed_decimal(True)
    # To turn off the fixed decimal point:
    #display.set_fixed_decimal(False)
    # Make sure to call write_display() to make the above visible!
    # Flip colon on or off.
    colon = not colon
