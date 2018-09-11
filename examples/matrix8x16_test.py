# Copyright (c) 2014 Adafruit Industries
# Author: Carter Nelson
# Modified from matrix8x8_test.py by Tony DiCola
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

from PIL import Image
from PIL import ImageDraw

from Adafruit_LED_Backpack import Matrix8x16


# Create display instance on default I2C address (0x70) and bus number.
display = Matrix8x16.Matrix8x16()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = Matrix8x16.Matrix8x16(address=0x74, busnum=1)

# On BeagleBone, try busnum=2 if IOError occurs with busnum=1
# display = Matrix8x16.Matrix8x16(address=0x74, busnum=2)

# Initialize the display. Must be called once before using the display.
display.begin()

# Run through each pixel individually and turn it on.
for x in range(8):
	for y in range(16):
		# Clear the display buffer.
		display.clear()
		# Set pixel at position i, j to on.  To turn off a pixel set
		# the last parameter to 0.
		display.set_pixel(x, y, 1)
		# Write the display buffer to the hardware.  This must be called to
		# update the actual display LEDs.
		display.write_display()
		# Delay for half a second.
		time.sleep(0.1)

# Draw some shapes using the Python Imaging Library.

# Clear the display buffer.
display.clear()

# First create an 8x16 1 bit color image.
image = Image.new('1', (8, 16))

# Then create a draw instance.
draw = ImageDraw.Draw(image)

# Draw a rectangle with colored outline
draw.rectangle((0,0,7,15), outline=255, fill=0)

# Draw an X with two lines.
draw.line((1,1,6,14), fill=255)
draw.line((1,14,6,1), fill=255)

# Draw the image on the display buffer.
display.set_image(image)

# Draw the buffer to the display hardware.
display.write_display()

# See the SSD1306 library for more examples of using the Python Imaging Library
# such as drawing text: https://github.com/adafruit/Adafruit_Python_SSD1306
