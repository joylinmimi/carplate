import time
import math
import datetime
import json
from pprint import pprint
import os,glob
from PIL import Image, ImageDraw
import sys
import dash_func as dash_func
import brightness2
###################################################################################################################################
Dict={}
for infile in glob.glob("data2/*.jpg"):
	brightness2.brightness(infile)
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

	plate3=0
	j=0
	i=0
	file, ext = os.path.splitext(infile)
	print infile
	os.system("alpr -c mx -j " +infile+ "> test.json")
	with open('test.json') as f:
    		data = json.load(f)
    		while True:
        		k=0
			try:
#######################################################################################################################################

#plot out red rectangle
				#print "drawrec"
				coordinates=(data["results"][i]["coordinates"][0]["x"],data["results"][i]["coordinates"][0]["y"])
##################################################################################################################################################	
#plate number
				#detect for tw plate
				while True:
					plate2=dash_func.dash(data,i,j,k)
					j=j+1
					if (plate2!=None):
						plate3=plate2
						break
					#print i,j,k
					#print file+'-'+str(i), plate3, st
                		if(plate3==0):
					i2=i
                                        j2=0
                                        os.system("alpr -j " +infile+ "> test2.json")
                                        with open('test2.json') as f2:
                                                data2=json.load(f2)
						data=data2
                                                while True:
                                                        k2=0
                                                      	while True:
                                                                plate2=dash_func.dash(data2,i2,j2,k2)
                                                                j2=j2+1
                                                                if(plate2!=None):
                                                                	plate3=plate2
									break
                                                        if(plate3==0):
                                                        	plate3="No plate detected"
								#print "label:", plate3
                                                        	break
							break
				print "label:", plate3

                                coordinates=(data["results"][i]["coordinates"][0]["x"],data["results"][i]["coordinates"][0]["y"])
                                a=data["results"][i]["coordinates"][0]["x"]
                                b=data["results"][i]["coordinates"][0]["y"]
                                c=data["results"][i]["coordinates"][1]["x"]
                                d=data["results"][i]["coordinates"][1]["y"]
                                e=data["results"][i]["coordinates"][2]["x"]
                                f=data["results"][i]["coordinates"][2]["y"]
                                g=data["results"][i]["coordinates"][3]["x"]
                                h=data["results"][i]["coordinates"][3]["y"]
                                im = Image.open(infile)
                                draw = ImageDraw.Draw(im)
                                draw.line((a,b, c, d), fill=128, width=10)
                                draw.line((c,d,e,f), fill=128, width=10)
                                draw.line((e,f,g,h), fill=128, width=10)
                                draw.line((g, h,a,b), fill=128, width=10)
                                print file+'-'+str(i)
                                im.save(file+'-'+str(i), "JPEG")






				print plate3, i, a,b
				os.system("montage -label 'Capture Time: "+st+" Plate No.: "
+plate3+" Event Type: Illegal Parking' "+file+'-'+str(i)+" -fill yellow -pointsize 50 -geometry +0+0 -background Black "+file+'-'+str(i))
					#break

            			i=i+1
			
			except IndexError:
				break
'''
		if(plate3==0):
			plate3="No plate detected"
			print 'None in'
		print 'x:',st, plate3
########################################################################################################################################################
#violation ticketi

                os.system("montage -label 'Capture Time: "+st+" Plate No.: "+plate3+" Event Type: Illegal Parking' "+infile+" -fill yellow -pointsize 50 -geometry +0+0 -background Black "+file)

                if plate3 not in Dict:
                	Dict[plate3] = [st,coordinates]
			print "not in"
                else:
			#print "in:", new-old
                        old=int(Dict[plate3][0][14:][:2])*60+int(Dict[plate3][0][14:][3:])
                        new=int(st[14:][:2])*60+int(st[14:][3:])
			print "in:", new,old

                        if(new-old >1 and math.sqrt((Dict[plate3][1][0]-coordinates[0])**2+(Dict[plate3][1][1]-coordinates[1])**2)<500):
                        	print math.sqrt((Dict[plate3][1][0]-coordinates[0])**2+(Dict[plate3][1][1]-coordinates[1])**2)
                                print "first:",Dict[plate3],"\nsecond:",st,"\ncoordinates:",coordinates,"\nplate:",plate3
'''
