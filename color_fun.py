import webcolors
from PIL import Image
from PIL import Image, ImageDraw
import sys
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
    return closest_name
def get_rgb(image, c1, c2):

        im = Image.open(image)
        #im.crop((10, 15, 15, 10)) #crop the center of the image

        rgb = im.convert('RGB') # get three R G B values
        r, g, b = rgb.getpixel((c1, c2))


        requested_colour = (r,g,b)
        return requested_colour

