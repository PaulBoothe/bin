######how to run: $python protCancerCorr.py [file that has proteins of interest] [directory where TCGA files are located]

######this program will create a single file that shows ryanGeneList protein 1st order associations and their corresponsponding cancers in TCGA vcf format with annovar annotiation.

###### gene | file | line in file that has the corresponding gene







import sys, re

import gzip

import os

import glob



###open output from iRefExtract6.py which is named protExtract.txt. Put all associated proteins in a list called masterList.

masterList = []

with open (sys.argv[1], 'r') as extractFile:

	for line in extractFile:



		

		sections = line.split('\t')

		if len(sections) > 1:

			assProteins = sections[1]

			

			assProteinsList = assProteins.split(',')

			

			for each in assProteinsList:

				

				if each not in masterList:

					masterList.append(each)

						







fileList = os.listdir(sys.argv[2])



















######## open individual patient cancer file, and grab lines that contain proteins in the masterList

for item in fileList:

	

	inputFile1 = gzip.open(sys.argv[2] + '/' + item, 'r')

	for line in inputFile1:

		sections = line.split('\t')



		subsections = sections[1]

		commaSections = subsections.split(',')

		if len(commaSections) > 1:

			for each in commaSections:

				paraSections = each.split('(')

				if len(paraSections) > 1:

					proteinOfInterest1 = paraSections[0]

					proteinOfInterest2 = paraSections[1]

				else:

					proteinOfInterest2 = 0

		else:

			proteinOfInterest1 = 0

			proteinOfInterest2 = 0



		proteinOfInterest1 = subsections.split('(')[0]



		





		

		for each in masterList:

			if each == proteinOfInterest1:

				print each + '\t' + item + '\t' + line

			if each == proteinOfInterest2:

				print each + '\t' + item + '\t' + line



	inputFile1.close()





