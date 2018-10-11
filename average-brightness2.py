im = Image.open("test2.jpg")
stat = ImageStat.Stat(im)
gs = (math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2)) 
	for r,g,b in im.getdata())
return sum(gs)/stat.count[0]
print sum(gs)/stat.count[0]
