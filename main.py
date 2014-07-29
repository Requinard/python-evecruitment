#!/usr/bin/python
# -*- coding: ascii -*-

import os
import time
import winsound

#Setup
ChatlogName = "Recruitment"
StringsOfInterest = ["looking"]
folder = "%s\\Documents\\EVE\\logs\\Chatlogs\\" % (os.path.expanduser("~"))


files = [x for x in os.listdir(folder) if os.path.isfile(os.path.join(folder, x)) and ChatlogName in x]
file = open(os.path.join(folder, files[-1]), "r+",)
lines = []
firstRun = True

while True:
	for line in file.readlines():
		print line
		if line not in lines:
			# String has not been found yet
			if not firstRun:
				#We're not starting the parse anymore. It's on now
				for word in StringsOfInterest:
					if word in line:
						winsound.Beep(1000, 1000)
			lines.append(line)
	else:
		break

file.close()


