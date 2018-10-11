import time
import datetime
import json
from pprint import pprint
import os
import sys

def dash(data,i,j,k):
	#print i,j,k
	try:
		#j=0
		#print i, j ,k
		plate=data["results"][i]["candidates"][j]["plate"]

		if (len(str(plate))==7 and plate[3:].isdigit()):
			plate2=plate[:3]+'-'+plate[3:]
			k=1

		elif (len(str(plate))==6):
			if (plate[2:].isdigit()):
				plate2=(plate[:2]+'-'+plate[2:])
				k=1
			else:
				if (plate[3:].isdigit()):
					plate2=(plate[:3]+'-'+plate[3:])
					k=1
				else:
					if (plate[:4].isdigit()):
						plate2=(plate[:4]+'-'+plate[4:])
						k=1
					else:
						if (plate[:3].isdigit()):
							plate2=(plate[:3]+'-'+plate[3:])
							k=1
		elif (len(str(plate))==5):
			if (plate[2:].isdigit()):
				plate2=(plate[:2]+'-'+plate[2:])
				k=1
			else:
				if (plate[:3].isdigit()):
					plate2=(plate[:3]+'-'+plate[3:])
					k=1
		if(k==1):
			#print plate2
			return plate2
			Dict[plate] = st
			#break
		#if(k!=1):
			#return "j"
	except IndexError:
		#print "error"
		return 0

