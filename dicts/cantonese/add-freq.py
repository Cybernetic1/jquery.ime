#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

f1 = open("HKIEd-simp.txt", "r")	# format: char,spelling with tone number
f2 = open("char-pinyin2-freq-raw.csv", "r")	# format: char,pinyin2,freq
# fo = sys.stdout
fo = open("HKIEd.js", "w")					# format: K,N,tone,char,freq

freqs = {}			# python built-in dictionary function

for line in f2:
	f = (line.split(','))
	freqs[f[0]] = f[2][:-1]

for line in f1:
	items = line.split(',')
	# print line

	char = items[0]
	# it's verified that every spelling has a single-digit tone number:
	tone = items[1][-2:-1]
	spelling = items[1][:-2]

	# extract consonant-nuclei form

	if freqs.has_key(char):
		fo.write('[\'' + spelling + '\',' + tone + ',\'' + char + '\',' + freqs[char] + '],\n')
	else:
		# make up a small frequency for unmatched chars,
		# freq will not sum to 1, but we don't care at this moment
		fo.write('[\'' + spelling + '\',' + tone + ',\'' + char + '\',' + '0.0000001],\n')
		print char			# this is an error output to stdout

	if False: """
	# remove tone number at the end
	if pinyin_tone[-1].isdigit():
		# tone = '0'
		pinyin = pinyin_tone[:-1]
	else:
		pinyin = pinyin_tone
	"""

	# fo.write('[\'' + k + '\',\'' + n + '\',%.9f],\n' % freq_sum)
