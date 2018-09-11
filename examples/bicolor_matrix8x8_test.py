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
from PIL import Image
from PIL import ImageDraw

from Adafruit_LED_Backpack import BicolorMatrix8x8


# Create display instance on default I2C address (0x70) and bus number.
display = BicolorMatrix8x8.BicolorMatrix8x8()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = BicolorMatrix8x8.BicolorMatrix8x8(address=0x74, busnum=1)

# On BeagleBone, try busnum=2 if IOError occurs with busnum=1
# display = BicolorMatrix8x8.BicolorMatrix8x8(address=0x74, busnum=2)

# Initialize the display. Must be called once before using the display.
display.begin()

# Run through each color and pixel.
# Iterate through all colors.
for c in [BicolorMatrix8x8.RED, BicolorMatrix8x8.GREEN, BicolorMatrix8x8.YELLOW]:
    # Iterate through all positions x and y.
    for x in range(8):
        for y in range(8):
            # Clear the display buffer.
            display.clear()
            # Set pixel at position i, j to appropriate color.
            display.set_pixel(x, y, c)
            # Write the display buffer to the hardware.  This must be called to
            # update the actual display LEDs.
            display.write_display()
            # Delay for a quarter second.
            time.sleep(0.25)

# Draw some colored shapes using the Python Imaging Library.

# Clear the display buffer.
display.clear()

# First create an 8x8 RGB image.
image = Image.new('RGB', (8, 8))

# Then create a draw instance.
draw = ImageDraw.Draw(image)

# Draw a filled yellow rectangle with red outline.
draw.rectangle((0, 0, 7, 7), outline=(255, 0, 0), fill=(255, 255, 0))

# Draw an X with two green lines.
draw.line((1, 1, 6, 6), fill=(0, 255, 0))
draw.line((1, 6, 6, 1), fill=(0, 255, 0))

# Draw the image on the display buffer.
display.set_image(image)

# Draw the buffer to the display hardware.
display.write_display()

# Pause for 5 seconds
time.sleep(5)

# Clear the screen again.
display.clear()
display.set_image(display.create_blank_image())

# Make the same image scrollable
scrollable = display.horizontal_scroll(image)

# Animate the scrollable image
display.animate(scrollable)


# See the SSD1306 library for more examples of using the Python Imaging Library
# such as drawing text: https://github.com/adafruit/Adafruit_Python_SSD1306
