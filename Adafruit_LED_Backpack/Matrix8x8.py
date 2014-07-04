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
import HT16K33


class Matrix8x8(HT16K33.HT16K33):
	"""Single color 8x8 matrix LED backpack display."""

	def __init__(self, **kwargs):
		"""Initialize display.  All arguments will be passed to the HT16K33 class
		initializer, including optional I2C address and bus number parameters.
		"""
		super(Matrix8x8, self).__init__(**kwargs)

	def set_pixel(self, x, y, value):
		"""Set pixel at position x, y to the given value.  X and Y should be values
		of 0 to 8.  Value should be 0 for off and non-zero for on.
		"""
		if x < 0 or x > 7 or y < 0 or y > 7:
			# Ignore out of bounds pixels.
			return
		self.set_led(y*16+((x+7)%8), value)

	def set_image(self, image):
		"""Set display buffer to Python Image Library image.  Image will be converted
		to 1 bit color and non-zero color values will light the LEDs.
		"""
		imwidth, imheight = image.size
		if imwidth != 8 or imheight != 8:
			raise ValueError('Image must be an 8x8 pixels in size.')
		# Convert image to 1 bit color and grab all the pixels.
		pix = image.convert('1').load()
		# Loop through each pixel and write the display buffer pixel.
		for x in [0, 1, 2, 3, 4, 5, 6, 7]:
			for y in [0, 1, 2, 3, 4, 5, 6, 7]:
				color = pix[(x, y)]
				# Handle the color of the pixel, off or on.
				if color == 0:
					self.set_pixel(x, y, 0)
				else:
					self.set_pixel(x, y, 1)
