import sys, re

from collections import defaultdict



inputFile = open(sys.argv[1], "r")

#outputFile - open(sys.argv[1], + ".output.text", "w")



d = defaultdict(list)



#check file for complexes and put them in dictionary

for line in inputFile:

	c1 = line.split('\t')[0]

	c2 = [line.split('\t')[1]]

	#grab only lines that have a complex in the first column:

	if 'complex:' in c1:

		#check to see if c2 is not in dictionary entry for the key c1:

		if c2 not in d[c1]:

			#if it is not, add it in.

			d[c1].append(c2)

			#if it is, done.





	

	









	#if 'complex:' in c1:

		#if d[c1] == c2:

			#d[c1].append(c2)

		#else:

			#d[c1] = c2

	











	#if d[c1] == [c2]

	#	d[c1].append(c2)

	#else:

	#	d[c1] = [c2]

	#print type(c2)

		





#for k, v in d.items():

#		print k

#		print '\t'

#		print v

keyNumber = 0

for each in d:

	print each

	print d[each]

	keyNumber += 1



print keyNumber

inputFile.close
