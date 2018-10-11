import time
import datetime
import json
from pprint import pprint
import os,glob
from PIL import Image, ImageDraw
import sys
import dash_func as dash_func
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
Dict={}
for infile in glob.glob("data/*.jpg"):
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
				(data["results"][i]["coordinates"][0]["x"],data["results"][i]["coordinates"][0]["y"])
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
                                im.save(file + ".thumbnail", "JPEG")

				while True:
					plate2=dash_func.dash(data,i,j,k)
					j=j+1
					#print plate2					
					if (plate2!=None):
						break
				print "plate:",plate2
				if(plate2==0):
                                        i2=0
                                        j2=0
                                        #print "first"
                                        os.system("alpr -j " +infile+ "> test2.json")
                                        with open('test2.json') as f2:
                                                data2=json.load(f2)
                                                #break
                                                while True:
                                                        #print "true"
                                                        k2=0

                                                        try:
                                                                (data2["results"][i2]["coordinates"][0]["x"],data2["results"][i2]["coordinates"][0]["y"])
                                                                while True:
                                                                        plate2=dash_func.dash(data2,i,j2,k2)
                                                                        j2=j2+1
                                                                        print plate2
                                                                        if(plate2!=None):
                                                                                break
                                                                        #break
                                                                i2=i2+1
                                                        except IndexError:
                                                                break
                                                break


            			i=i+1
				
			except IndexError:
				break
