import sys, re

from collections import defaultdict



inputFile = open(sys.argv[1], "r")

#outputFile = open(sys.argv[1] + ".output.txt", "w")





d = defaultdict(list)









#Close and reopen inputFile. Not sure why. Won't work otherwise.

inputFile.close()

inputFile = open(sys.argv[1], "r")



#intialize ryan_gene_list:

ryanGeneList = ['uniprotkb:Q8IWA4', 'uniprotkb:O95140', 'uniprotkb:O60313', 'uniprotkb:Q99623', 'uniprotkb:Q9UJZ1', 'uniprotkb:Q9Y3D6', 'uniprotkb:O00429', 'uniprotkb:Q9GZY8', 'uniprotkb:Q96C03', 'uniprotkb:Q9Y371', 'uniprotkb:Q8TB36']

#check file for instances of specific protein in list. Assign complexes according to dictionary.



#initialize dictionary for proteins

dProtein = defaultdict(list)



for line in inputFile:

	if not line.startswith("#"):

		for each in ryanGeneList:

				if each in line:

					sections = line.split('\t')

					c1 = sections[0]

					c2 = [sections[1]]



					#if ryanGeneList protein is in c1, add c2 to its dProtein value

					if each in c1:

						if c2 not in dProtein[c1]:

							dProtein[c1].append(c2)



					#if protein complex is in list, add the associated values of that complex to the dProtein dict.

					if 'complex' in c1:

						if c2 not in dProtein[c1]:

							dProtein[c1].append(d[c1])



					#if ryanGeneList protein is in c2, add c1 to its dProtein value

					#if each in c2:

						#if c1 not in dProtein[c2]:

							#dProtein[c2].append(c1)





for k,v in dProtein.items():

	print k + '\t' + v

	





		

		



		

		#outputFile.write("Found DRP1")

		

#outputFile.close()



inputFile.close()
