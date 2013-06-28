import sys,re

inputFile = open(sys.argv[1], "r")
lines = inputFile.readlines()
inputFile.close()

outputFile = open(sys.argv[2], "w")

x = 0
for line in lines:
	if not line.startswith("#"):
		split[x] = line.split("|")
		
		
		outputFile.write(line)
		

outputFile.close()

print split



