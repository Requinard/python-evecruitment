#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import winsound

# Setup
log_name = u"Corp"
sentence_of_interest = [u"looking for", u"corp", u"active"]
folder = u"%s\\Documents\\EVE\\logs\\Chatlogs\\" % (os.path.expanduser("~"))

# #############################################
# DO NOT TOUCH BELOW
##############################################

files = [x for x in os.listdir(folder) if os.path.isfile(os.path.join(folder, x)) and log_name in x]
lines = []
first = True

while True:
	print "Starting Run\nOpening file %s" % (files[-1])

	file = open(os.path.join(folder, files[-1]), "r+", )
	file_lines = [x.decode("utf-8", "replace").replace(u"\x00", "").lower() for x in file]

	for line in file_lines:
		if line not in lines:
			print "UNREAD LINE:%s" % (line)
			if first == False:
				for word in sentence_of_interest:
					if word in line:
						print("CHAT HIT\nWORD:%s\nLINE: %sUSER:%s\nMESSAGE:%s" % (
						word, line, line.split("]")[1].split(">")[0], line.split(">")[1]))
						winsound.Beep(1000, 1500)
						os.system("echo %s | clip" % (str(line.split("]")[1].split(">")[0].strip().strip("\n\r"))))
			lines.append(line)

	if first:
		first = False

	time.sleep(2)

file.close()


