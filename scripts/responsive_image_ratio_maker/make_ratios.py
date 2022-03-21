#!/usr/bin/env python3



# NOTE: Not using this. Ended up doing all this in the javascript directly


import json

from string import Template


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


data = { "ratios": [], "widths": [] }

for ratio in ratios:
	data[ratio].append(ratio)
	

print(f"const image_config = {json.dumps(data)}")
	





#
#ratio_data = {}
#
#
#for indx, ratio in enumerate(ratios):
#	ratio_key = f"{ratio[0]}x{ratio[1]}"
#	
#	ratio_widths = []
#	
#	for w in widths:
#		ratio_widths.append(
#			{
#				"width": w,
#				"height": int(w / ratio[0] * ratio[1])
#			}
#		)
#		
#	ratio_data[ratio_key] = {
#		"widths": ratio_widths
#	}
#	
#		
##		r = lambda: randint(0,255)
##		c = '%02X%02X%02X' % (r(),r(),r())
##		h = int(w / ratio[0] * ratio[1])
##		f = int(w / 4)
##		fw = int(w * 0.8)
##		fh = int(h * 0.8)
##		url = url_.substitute({"rw": ratio[0], "rh": ratio[1], "w": w, "h": h, "f": f, "c": c, "fw": fw, "fh": fh})
##		path = f"images/{ratio[0]}x{ratio[1]}_at_{w}x{h}.jpg"
##		print(path)
##		save_image_from_url(url, path)
#
#
#print(f'const ratios = {json.dumps(ratio_data)}')