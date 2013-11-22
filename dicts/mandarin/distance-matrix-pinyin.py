#!/usr/bin/python
# -*- coding: UTF-8 -*-

# For an explanation of the ideas, see:
#	/dicts/mandarin/README.fuzzy-pinyin-matching.html

consonants = ['b','p','m','f','d','t','n','l','g','k','h','j','q','x', \
	'zh','ch','sh','r', 'z','c','s','w','y' ];

# classification tree of consonants
cluster_K = \
	["Root=1.0",
		["JQX=0.3",
			["Q=0.2",
				["QC=0.1",
					'q','c'],
				'ch'],
			["J=0.2",
				["JZ=0.1",
					'j','z'],
				'zh'],
			["X=0.2",
				["XS=0.1",
					'x','s'],
				'sh']],
		["WY=0.7",
			'w','y'],
		["RL=0.4",
			'r','l'],
		["MN=0.7",
			'm','n'],
		["BPDTGK=0.7",
			["DT=0.2",
				'd','t'],
			["BP=0.2",
				'b','p'],
			["GK=0.2",
				'g','k']],
		["FH=0.8",
			'f','h']]

nuclei = ['a','ai','an','ang','ao','e','ei','en','eng','er','i','ia', \
		'ian','iang','iao','ie','in','ing','io','iong','iu','o','ong', \
		'ou','u','ua','uai','uan','uang','ue','ui','un','uo','ü','üan','ün']

cluster_N = \
	["Root=1.0",
		["-N/G=0.5",
			["-i-ng=0.3",
				["-ng=0.2",
					"ang", "ing", "uang", "ong", "eng"],
			"iang", "iong"],
			["-an=0.1",
				"uan", "üan", "ian"],
			["-n=0.1",
				"in", "an", "en", "ün", "un"]],
		["-IX=0.4",
			"iao",
			["-ix=0.1",
				"iu", "io"]],
		["X=0.5",
			["-o=0.1",
				"uo", "o"],
			["-u=0.15",
				"ou", "ao", "ü", "u"],
			["-e=0.1",
				"ie", "ue"],
			["A/E=0.4",
				["-a=0.1",
					"ia", "a", "ua"],
				["-e=0.3",
					"er", "e"]],
			["-i=0.15",
					"i", "ei", "uai", "ui", "ai"]]]

def findPath(node, symbol):
	"""Find the path to leaf symbol in cluster tree
	Performs a breath-first search by recursion"""
	#print "symbol = ", symbol
	for child in node[1:]:
		#print "child = ", child
		if type(child) is list:
			# We know that only one branch will succeed
			path2 = findPath(child, symbol)
			if path2 is not None:
				#print "append!!!!!"
				path2.append(node[0])
				return path2
		elif child == symbol:
			#print "match!!!!!"
			return [node[0]]		# return a list contain the leaf
	return None				# reached dead end, should backtrack from here

def d(cluster, k1, k2):
	"""Find distance between k1,k2
	Distance is given by the lowest common parent node
	Algorithm:
	1. Traverse tree to find k1 and k2, record paths of traversal
	2. Find lowest common node in the 2 traversal paths"""
	if k1 == k2:
		return 0.0
	p1 = findPath(cluster, k1)
	#print "p1 = ", p1
	p2 = findPath(cluster, k2)
	#print "p2 = ", p2
	# Find lowest common node of p1, p2
	# The last node is always "Root"
	while p1[-1] == p2[-1]:
		common = p1.pop()
		p2.pop()
		if p1 == [] or p2 == []:
			break
	# The distance is inside the string, following '='
	return float(common.partition('=')[2])

import sys
# fo = sys.stdout

f1 = open("distance-matrix-K.csv", "w")
for i, k1 in enumerate(consonants):
	for k2 in consonants[0:i]:
		distance = d(cluster_K, k1, k2)
		f1.write("{2},".format(k1, k2, distance))
	f1.write("\n");

f2 = open("distance-matrix-N.csv", "w")
for i, n1 in enumerate(nuclei):
	for n2 in nuclei[0:i]:
		distance = d(cluster_N, n1, n2)
		f2.write("{2},".format(n1, n2, distance))
	f2.write("\n");
