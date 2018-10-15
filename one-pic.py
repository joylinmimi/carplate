from __future__ import division
import time
import colorsys
import math
import datetime
import json
from pprint import pprint
import os,glob
from PIL import Image, ImageDraw
import sys
import dash_func as dash_func
import brightness
import color_fun
import colorname
import hollow_color
import matplotlib.pyplot as plt

###################################################################################################################################
Dict={}
for infile in glob.glob("data2/*.jpg"):
	brightness.brightness(infile)
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

	plate3=0
	j=0
	i=0
	file, ext = os.path.splitext(infile)
	print infile
	os.system("alpr -j " +infile+ "> test.json")
	with open('test.json') as f:
    		data = json.load(f)
    		while True:
        		k=0
			try:
				print 'try'
#######################################################################################################################################

#plot out red rectangle
				print data
				#print "drawrec"
				coordinates=(data["results"][i]["coordinates"][0]["x"],data["results"][i]["coordinates"][0]["y"])
##################################################################################################################################################	
#plate number
				print '2'

                                coordinates=(data["results"][i]["coordinates"][0]["x"],data["results"][i]["coordinates"][0]["y"])
                                x1=data["results"][i]["coordinates"][0]["x"]
                                y1=data["results"][i]["coordinates"][0]["y"]
                                x2=data["results"][i]["coordinates"][1]["x"]
                                y2=data["results"][i]["coordinates"][1]["y"]
                                x3=data["results"][i]["coordinates"][2]["x"]
                                y3=data["results"][i]["coordinates"][2]["y"]
                                x4=data["results"][i]["coordinates"][3]["x"]
                                y4=data["results"][i]["coordinates"][3]["y"]
				print x1,y1,x2,y2,x3,y3,x4,y4
				print 'x'
				#c1=(c-a)/2+c
				#c2=(b+f)/2
				#rgb=color_fun.get_rgb(infile,c1,c2)
				#print rgb, colorsys.rgb_to_hsv(*rgb)
				#color= colorname.color_name(*rgb)
				#print color
                                im = Image.open(infile)
                                #draw = ImageDraw.Draw(im)
                                #draw.line((x1,y1, x2, y2), fill=128, width=10)
                                #draw.line((x2,y2,x3,y3), fill=128, width=10)
                                #draw.line((x3,y3,x4,y4), fill=128, width=10)
                                #draw.line((x4, y4,x1,y1), fill=128, width=10)
                                #print file+'-'+str(i)
                                #im.save(infile, "JPEG")
				size=4000 
				outer_width=2*(x3-x4)
				outer_height=2*(y4-y1)
				a=(x3-x4)/2
				b=(y4-y1)/2
				c=x1-(x3-x4)/2
				d=y1-(y4-y1)/2
				inner_width=x3-x4
				inner_height=y4-y1
				print 'x'
				print (x1,y1,x2,y2,x3,y3,x4,y4), size, outer_width, outer_height, a, b,c,d, inner_width, inner_height
				pts=hollow_color.sample_hollow_lamina(size, outer_width, outer_height, a, b,c,d, inner_width, inner_height)		
				
				plt.plot(pts[:,0], pts[:,1], 'o', alpha=0.75)
				plt.show()

				#os.system("montage -label 'Color: "+color+" Capture Time: "+st+" Plate No.: "
#+plate3+" Event Type: Illegal Parking' "+infile+" -fill yellow -pointsize 40 -geometry +0+0 -background Black "+infile)
					#break

            			i=i+1
			
			except IndexError:
				break
