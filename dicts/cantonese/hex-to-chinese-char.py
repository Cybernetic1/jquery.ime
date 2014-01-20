#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Convert yale.dat (file from HanConv software) to "char,spelling" format
# Notice that yale.dat is in DOS EOL format

import sys

f1 = open("hanconv//yale.dat", "r")		# format: hex=pinyin with tone number
													# eg: 8E72=CHYUN4 DEUN1
# fo = sys.stdout
fo = open("yale.txt", "w")

for line in f1:
	hex = line[0:4]							# char code in hex
	dec = int(hex, 16)						# convert to integer, from base 16
	c = unichr(dec)							# char in unicode

	yale = line[5:-2].lower()				# -2 because of DOS EOL
	yales = yale.split(' ')					# split multiple spellings

	for y in yales:
		fo.write(c.encode('utf8') + ',' + y + '\n')

f1.close()
fo.close()
