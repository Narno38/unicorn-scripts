#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys
import numpy as np
import random
import psutil

unicorn.brightness(0.4)
unicorn.rotation(270)

def make_gaussian(fwhm, x0, y0):
		x = np.arange(0, 8, 1, float)
		y = x[:, np.newaxis]
		fwhm = fwhm
		if fwhm == 0:
				fwhm = 0.000000000001
		gauss = np.exp(-4 * np.log(2) * ((x - x0) ** 2 + (y - y0) ** 2) / fwhm ** 2)
		return gauss

while True:
		cpu = psutil.cpu_percent()
		speed = max ( 1.2 - cpu, 0.1 )
		x0, y0 = 3.5, 3.5
		for z in range(1, 5)[::-1] + range(1, 10):
				fwhm = 5/z
				gauss = make_gaussian(fwhm, x0, y0)
				for y in range(8):
						for x in range(8):
								h = 0.8
								s = 0.8
								v = gauss[x,y]
								rgb = colorsys.hsv_to_rgb(h, s, v)
								r = int(rgb[0] * 255.0)
								g = int(rgb[1] * 255.0)
								b = int(rgb[2] * 255.0)
								unicorn.set_pixel(x, y, r, g, b)
				unicorn.show()
				time.sleep(speed/10)
