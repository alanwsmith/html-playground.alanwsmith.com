#!/usr/bin/env python3

import json

import requests 

from random import randint
from string import Template

url_ = Template('https://res.cloudinary.com/awsimages/image/upload/c_fill,w_$w,h_$h/co_white,l_text:Oswald_${f}_bold:${w}x${h}/fl_layer_apply/l_sample,w_$w,h_$h,e_colorize,co_rgb:$c,o_60/fl_layer_apply/responsive-image-test/blank_noise.jpg')


def save_image_from_url(url, path):
	res = requests.get(url, stream=True)
	if res.status_code == 200:
		with open(path, 'wb') as _f:
			for chunk in res:
				_f.write(chunk)
	else:
		print("ERROR")


widths = [2000, 1250, 1000, 750, 500, 400, 300, 200, 100]

ratios = [
	[1, 2], 
	[2, 1], 
	[1, 3], 
	[3, 1], 
	[1, 4], 
	[4, 1],
	[2, 3], 
	[2, 5], 
	[2, 7], 
	[3, 2],
	[5, 2], 
	[7, 2], 
	[3, 4],
	[3, 5],
	[3, 7], 
	[3, 8],
	[4, 3],
	[5, 3],
	[7, 3],
	[8, 3]
]


for indx, ratio in enumerate(ratios):	
	for w in widths:
		r = lambda: randint(0,255)
		c = '%02X%02X%02X' % (r(),r(),r())
		h = int(w / ratio[0] * ratio[1])
		f = int(w / 6)
		url = url_.substitute({"w": w, "h": h, "f": f, "c": c})
		path = f"images/{ratio[0]}x{ratio[1]}_at_{w}x{h}.jpg"
		print(path)
		save_image_from_url(url, path)

