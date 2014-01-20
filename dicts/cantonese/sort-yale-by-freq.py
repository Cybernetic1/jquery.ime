#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Notice that by pinyin I mean spellings for Cantonese.

# Input: list1 with char + pinyin
#			list2 with char + freq
# Output: sort list1 by freq looked up from list2

import sys

f1 = open("yale.txt", "r")					# format: char,pinyin with tone number
f2 = open("canto-raw.txt", "r")			# format: char,freq
# fo = sys.stdout
fo = open("yale-sort-by-freq.txt", "w")

pinyins = []

for line in f1:
	pinyins.append(line.split(','))

for line in f2:
	items = line.split(',')
	# print line

	char = items[0]
	# freq = float(items[1][:-1])

	found = False
	for item in pinyins:
		if char == item[0]:
			fo.write(char + ',' + item[1])
			found = True

	if not found:
		print char

	if False: """
	# remove tone number at the end
	if pinyin_tone[-1].isdigit():
		# tone = '0'
		pinyin = pinyin_tone[:-1]
	else:
		pinyin = pinyin_tone
	"""

	# fo.write('[\'' + k + '\',\'' + n + '\',%.9f],\n' % freq_sum)
