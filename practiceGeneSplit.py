import sys,re

inputFile = open(sys.argv[1], "r")

dictionary = {}
for line in inputFile:
	if not line.startswith("#"):
		if float(line.split("\t")[10]) < .02:
			gene = line.split("\t")[0]
			hit = line.split("\t")[1]
			
			if gene in dictionary:
				dictionary[gene].append(hit)
			else:
				dictionary[gene] = [hit]
				
print type([hit])
			
	

