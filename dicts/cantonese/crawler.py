#!/usr/bin/python
# -*- coding: utf-8 -*-

#######################################################################
# fetch a file from an HTTP (web) server over sockets via httplib;
# the filename param may have a full directory path, and may name a CGI
# script with query parameters on the end to invoke a remote program;
# fetched file data or remote program output could be saved to a local
# file to mimic FTP, or parsed with str.find or the htmllib module;
#######################################################################

import sys, httplib
import string
import re				# regular expressions

# Reader:  you can use 'view source' to look at the HTML page
# Here we start inspecting the lines from 554
inspectBegin = 554
inspectEnd = 555

servername = 'ckc.ied.edu.hk'
filename = '/ckc2/dictionary.php?jiinput=闡&lang=en&form1=1'
# servername = 'www.mdbg.net'
# filename = '/chindict/chindict.php?page=chardict&cdcanoce=0&cdqchi=%E7%82%BA'

server = httplib.HTTP(servername)						# connect to http site/server

# Input list of characters:
f = open("canto-freq.txt", "r")

# Output 
fo = open("HKIEd-sort-by-freq.txt", "w")

# c = raw_input("Enter character to look up: ")

# read command line argument
# startIndex = int(sys.argv[1])
index = 0

while True:							# this loop is for looking up multiple chars
	line = f.readline()
	c = line.decode('utf8')[0]
	# print c
	filename = '/ckc2/dictionary.php?jiinput=' + \
		"%{:X}%{:X}%{:X}".format(ord(line[0]), ord(line[1]), ord(line[2])) + \
		'&lang=en&form1=1'
	# print filename

	# increment index
	index += 1
	# if index > 100: break								# look up N characters

	server.putrequest('GET', filename)				# send request and headers
	server.putheader('Accept', 'text/html')		# POST requests work here too
	server.endheaders()									# as do CGI script filenames

	errcode, errmsh, replyheader = server.getreply( )	# read reply info headers
	if errcode != 200:									# 200 means success
		print 'HTTP GET failed:', errcode, errmsh
	else:
		file = server.getfile()							# file obj for data received
		htmlPage = file.readlines()
		file.close()									# show lines with EOL at end

		for line in htmlPage[inspectBegin : inspectEnd]:
			# print line
			# The format of the HTML element is:
			# <a href="javascript: playSound('audio/can/tsin2.wav'); "><img src="image/audio_play.gif" alt=""/>tsin2</a>
			pinyin = re.findall('<img src=\"image/audio_play\.gif\" alt=\"\"/>([a-z]*[0-9 ]*)</a>', line)
			print str(index) + '.', c, " = ", pinyin

			for p in pinyin:
				fo.write(c.encode('utf8') + ',' + p + '\n')

fo.close()
f.close()
