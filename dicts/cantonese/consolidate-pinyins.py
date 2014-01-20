#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Input: list sorted by pinyins
# Output: frequencies consolidated for each unique pinyin
# for this version we may ignore tone numbers

import sys

f = open("char-pinyin2-freq_by-pinyin.csv", "r")
# fo = sys.stdout
fo = open("pinyins-consolidated.csv", "w")

# Input Format:
# pinyin-with-tone, char, frequency \n

# Output Format:
# consonant, nucleus, cumulative frequency \n
# old version: pinyin-without-tone, cumulative frequency \n

consonants = [ 'b','p','m','f','d','t','n','l','g','k','h','j','q','w','x','y','r' ]
# 'zh','ch','sh','z','c','s' are treated as special cases

# ***** convert to consonant-nucleus form *****
def k_n(pinyin_):
	# test for special cases:  z,c,s,zh,ch,sh
	c = pinyin_[0]
	consonant = None
	if (c == 'z' or c == 'c' or c == 's'):
		if (pinyin_[1] == 'h'):
			consonant = c + 'h'
			nucleus = pinyin_[2:]
		else:
			consonant = c
			nucleus = pinyin_[1:]
	else:						# test for the rest
		for k in consonants:
			if (pinyin_[0] == k):
				consonant = c
				nucleus = pinyin_[1:]
	if (consonant == None):
		consonant = ''
		nucleus = pinyin_
	return [consonant, nucleus]

big_sum = 0
freq_sum = 0
last_pinyin = "a"							# note: this must be the first pinyin in list

for line in f:
	items = line.split(',')
	print items

	pinyin_tone = items[0]				# pinyin with tone at the end
	char = items[1]
	freq = float(items[2][:-1])

	# remove tone number at the end
	if pinyin_tone[-1].isdigit():
		# tone = '0'
		pinyin = pinyin_tone[:-1]
	else:
		pinyin = pinyin_tone

	############ consolidate frequencies ##############
	if pinyin == last_pinyin:
		freq_sum += freq
	else:
		[k, n] = k_n(last_pinyin)
		fo.write('[\'' + k + '\',\'' + n + '\',%.9f],\n' % freq_sum)
		print '[\'' + k + '\',\'' + n + '\',%.9f],\n' % freq_sum
		big_sum += freq_sum
		last_pinyin = pinyin
		freq_sum = freq

# got to take care of the last bit -- annoying!
[k, n] = k_n(last_pinyin)
fo.write('[\'' + k + '\',\'' + n + '\',%.9f]\n' % freq_sum)
print '[\'' + k + '\',\'' + n + '\',%.9f]\n' % freq_sum

# OK, print the grand total and exit...
print big_sum
