##### iRefExtract program using new method 



import sys, re



from collections import defaultdict



d = defaultdict(list)

dProtein = defaultdict(list)

ryanGeneList = ['MFN1', 'MFN2', 'OPA1', 'PHB2', 'STOML2', 'FIS1', 'DNM1L', 'MFF', 'MIEF2', 'SH3GLB1', 'GDAP1']

##### build dictionary

with open(sys.argv[1], 'r') as inputFile1:

	for line in inputFile1:

		sections = line.split('\t')

		c1 = sections[0]

		protein = sections[5].split('|')[0].split(':')[1]

		





		if 'complex:' in c1:

			

			if protein not in d[c1]:

				d[c1].append(protein)





counter = 0

comcounter = 0

with open(sys.argv[1], 'r') as inputFile1:

	for line in inputFile1:

		for gene in ryanGeneList:

			if gene in line:

				sections = line.split('\t')

				c5 = sections[4].split('|')[0].split(':')[1] 

				c6 = sections[5].split('|')[0].split(':')[1]

				com1 = line.split('\t')[0]



				if gene == c5:

					if c6 not in dProtein[c5]:

						dProtein[c5].append(c6)

						counter += 1



				

				if gene == c6:

					if 'complex:' in com1:

						for item in d[com1]:

							if item not in dProtein[gene]:

								dProtein[gene].append(item)

								comcounter += 1





			

			















for each in dProtein:

	print each + '\t' + ', '.join(dProtein[each]) + '\n'

