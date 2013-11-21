#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

f = open("char-pinyin2-freq-raw.csv", "r")
# fo = sys.stdout
fo = open("char-pinyin.js", "w")

# Input Format:
# char,pinyin-with-tone,frequency

# Output Format:
# ["consonant", "nucleus", tone, "char", frequency]

list = []
head = ""

for line in f:
	items = line.split(',')
	print items

	char = items[0]
	pinyin_tone = items[1]		# pinyin with tone at the end
	freq = items[2][:-1]

	tone = pinyin_tone[-1]
	if (not pinyin_tone[-1].isdigit()):
		tone = '0'
		pinyin = pinyin_tone
	else:
		pinyin = pinyin_tone[:-1]

	# ***** convert to consonant-nucleus form *****

	consonants = [ 'b','p','m','f','d','t','n','l','g','k','h','j','q','w','x','y','r' ]
	# 'zh','ch','sh','z','c','s' are treated as special cases

	# test for special cases:  z,c,s,zh,ch,sh
	c = pinyin[0]
	consonant = None
	if (c == 'z' or c == 'c' or c == 's'):
		if (pinyin[1] == 'h'):
			consonant = c + 'h'
			nucleus = pinyin[2:]
		else:
			consonant = c
			nucleus = pinyin[1:]
	else:						# test for the rest
		for k in consonants:
			if (pinyin[0] == k):
				consonant = c
				nucleus = pinyin[1:]
	if (consonant == None):
		consonant = ''
		nucleus = pinyin

	fo.write("['" + consonant + "','" + nucleus + "'," + tone + ",'" \
			+ char + "'," + freq + "],\n")
