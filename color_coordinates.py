import colorsys
import color_fun
from PIL import Image, ImageDraw
def color_name(*rgb):
	rgb=(rgb[0]/float(255),rgb[1]/float(255),rgb[2]/float(255))
	print rgb
	HSV=  colorsys.rgb_to_hsv(*rgb)
	#print HSV
	HSV2=(HSV[0],HSV[1],(HSV[2]/float(255)))
	HSV=HSV2
	#HSV=HSV/255
	#print HSV
	if HSV[2]<0.001:	
		return('black')
	elif HSV[1]<0.05:
		if HSV[2]>0.8:
			return('white')
		else:
			return('gray')
	else:
		if HSV[0]>=0 and HSV[0]<80/float(360):
			return('yellow')
                if HSV[0]>=135/float(360) and HSV[0]<270/float(360):
                        return('blue')
                if HSV[0]>=270/float(360) and HSV[0]<360/float(360):
                        return('red')
                if HSV[0]>=80/float(360) and HSV[0]<135/float(360):
                        return('green')

def coordinates(image,a,b,c,d,e,f,g,h):
	c1=(c-a)/2+c
        c2=(b+f)/2
	
	rgb=color_fun.get_rgb(image,c1,c2)
	name= color_name(*rgb)
	
	im = Image.open(image)
	im.save(image, "JPEG")
	return(name)

print coordinates("yellow.jpg", 1,1,1,1,1,1,1,1)
			
	
