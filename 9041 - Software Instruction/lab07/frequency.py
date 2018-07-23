#!/usr/bin/python

import re,sys,glob

key = (sys.argv[1]).lower()

for file in sorted(glob.glob("lyrics/*.txt")):
	total = 0
	count = 0
	F = open(file, 'r')
	for line in F:
		line = line.lower()
		words = re.split(r"[^a-zA-Z]", line)
		for word in words:
			pattern = re.compile("^$")
			if not pattern.match(word):
				total +=1
			if word == key:
				count += 1
	
	name = file.replace(".txt", "")
	name = name.replace("_"," ")
	name = name.replace("lyrics/", "")
	
	result = float(count) / total
	print("   "+str(count) + "/ " + str(total) +" = " + str(("%.9f" % result )) +" " + name)