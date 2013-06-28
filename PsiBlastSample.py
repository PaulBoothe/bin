import sys,re

inputFile = open(sys.argv[1], "r")
lines = inputFile.readlines()
inputFile.close()

outputFile = open(sys.argv[2], "w")
d = {}
for line in lines:
	x = 0
	if not line.startswith("#"):
		phrases = line.split("|")
		
		for phrase in phrases:
			if x == 3:
				d[phrase] = 1
			x += 1
for key in d:
	outputFile.write(key + ' is the key, the value is ' + str(d[key]) + '\n')
outputFile.close()

print len(phrases)

