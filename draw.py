from PIL import Image, ImageDraw
import sys
im = Image.open("test")

draw = ImageDraw.Draw(im)

draw.line((1188,1883, 1613, 1872), fill=128, width=3)
draw.line((1613, 1872,1623,2092), fill=128, width=3)

#draw.line((100,200, 150,300), fill=128)
#draw.line((0, im.size[1], im.size[0], 0), fill=128)
#del draw

# write to stdout
#im.save(sys.stdout, "PNG")
im.show()
