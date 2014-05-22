################### this program builds a dictionary out of all positions with an ancestral allele that equals C

import sys, re

from collections import defaultdict





dAA = defaultdict(list)

with open (sys.argv[1], 'r') as inputFile1:

	for line in inputFile1:

		if not line.startswith('#'):

			sections = line.split('\t')

			infoColumn = sections[7]

			positionColumn = sections[1]

			ancestralSection = infoColumn.split(';')[0]

			



				# infoColumnSectionsParts = each.split('=')



				# alleleType = infoColumnSectionsParts[0]



				

			if ancestralSection == 'AA=C':

				if positionColumn not in dAA[ancestralSection]:



					dAA[ancestralSection].append(positionColumn)

					

					# if alleleType not in dAA:

					# 	dAA[positionColumn].append(alleleType)

for each in dAA:

	for item in dAA[each]:

		print item
