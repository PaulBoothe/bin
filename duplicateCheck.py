import sys,re

inputFile = open(sys.argv[1], "r")

numberList = []
for line in inputFile:
	sections = line.split("|")
	number = sections[3]
	numberList.append(number)



inputFile.close()

print len(numberList)
bareBones = set(numberList)
print len(bareBones)
