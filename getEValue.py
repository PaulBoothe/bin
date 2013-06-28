import sys,re

inputFile = open(sys.argv[1], "r")
lines = inputFile.readlines()
inputFile.close()

outputFile = open(sys.argv[2], "w")

d = {}
genelist = []
trimList = []

for line in lines:
	if not line.startswith('#'):
		phrase = line.split('\t')[10]
		phraseInt = float(phrase)
		if phraseInt < .01:  #e value check
			trimList.append(line)
			

gene = trimList[0].split('\t')[0]
for item in trimList:
	with open('{0}.txt'.format(gene[10:19]), 'w') as newGeneOutput:
		if gene == item.split('\t')[0]:
			newGeneOutput.write(item)
		
			

		


	






outputFile.close()

print gene

			






















