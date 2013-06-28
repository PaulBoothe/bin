import sys,re

inputFile = open(sys.argv[1], "r")



dictionary = {}

for line in inputFile:
	if not line.startswith("#"):
		if line.split("\t")[10] < .01:
			sections = line.split("\t")
			gene = sections[0]
			hit = sections[1]
			if gene in dictionary:
				dictionary[gene].append(hit)
			else:
				dictionary[gene] = [hit]
			
for gene in dictionary:
	filename = gene.split("|")[2]
	
	outputFile = open(filename + ".txt", "w")
	
	hits = dictionary[gene]
	for hit in hits:
		outputFile.write( gene + "\t" + hit + "\n" )
		
inputFile.close()
outputFile.close()

		
