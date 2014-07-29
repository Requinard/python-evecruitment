#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import winsound

# ###############################################
# SETTINGS
################################################

log_name = u"Recruitment"  # Name of the chat channel
sentence_of_interest = [u"looking for", u"corp", u"active"]  # Sentences you want to look out for
folder = u"%s\\Documents\\EVE\\logs\\Chatlogs\\" % (os.path.expanduser("~"))  # Eve Chat Log folder
copy_to_clipboard = True  # If you want to copy the name to clipboard, set to True
sound_pitch = 1000  # Pitch of the beep in Hz
sound_length = 1.5  # Length of the beep in seconds

# #############################################
# DO NOT TOUCH BELOW
# #############################################

if not os.path.isdir(folder):
	raise Exception("Your EVE chat folder does not exist")

files = [x for x in os.listdir(folder) if os.path.isfile(os.path.join(folder, x)) and log_name in x]
lines = []
first = True

if len(files) == 0:
	raise Exception("There are no chat logs with your log_name")

try:
	file_test = open(os.path.join(folder, files[-1]))
except:
	raise Exception("Your chat log is unreadable!")

while True:
	print "Starting Run\nOpening file %s" % (files[-1])

	try:
		file = open(os.path.join(folder, files[-1]), "r+", )
	except:
		raise Exception("Your file is unreadable")

	file_lines = [x.decode("utf-8", "replace").replace(u"\x00", "").lower() for x in file]

	for line in file_lines:
		if line not in lines:
			print "UNREAD LINE:%s" % (line)
			if first == False:
				for word in sentence_of_interest:
					if word in line:
						print("CHAT HIT\nWORD:%s\nLINE: %sUSER:%s\nMESSAGE:%s" % (
						word, line, line.split("]")[1].split(">")[0], line.split(">")[1]))
						winsound.Beep(sound_pitch, sound_length)
						if copy_to_clipboard:
							os.system("echo %s | clip" % (str(line.split("]")[1].split(">")[0].strip().strip("\n\r"))))
			lines.append(line)
	if first:
		first = False

	file.close()

	time.sleep(2)


