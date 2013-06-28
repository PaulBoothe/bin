import sys,re

inputFile = open(sys.argv[1], "r")



dictionary = {}

for line in inputFile:
	if not line.startswith("#"):
		sections = line.split("\t")
		eValue = sections[10]
		if float(eValue) < .01:
			
			gene = sections[0]
			hit = sections[1]
			if gene in dictionary:
				#dictionary[gene].append(hit)
				dictionary[gene][hit] =1;
			else:
				dictionary[gene]={}
				dictionary[gene][hit] = 1;
				#dictionary[gene] = [hit]
			
for gene in dictionary:
	filename = gene.split("|")[2]
	
	outputFile = open(filename + ".txt", "w")
	
	hits = dictionary[gene]
	for hit in hits:
		outputFile.write( gene + "\t" + hit + "\t" + "\n" )


	outputFile.close()
inputFile.close()





		
