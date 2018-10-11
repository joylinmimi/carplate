from PIL import Image, ImageEnhance 
def brightness(image):
	im = Image.open(image)
	enhancer = ImageEnhance.Brightness(im)
	#enhanced_im = enhancer.enhance(1.8)
	#enhanced_im = enhancer.enhance(3)   !good for us
	enhanced_im = enhancer.enhance(2.9)
	enhanced_im.save(image)

