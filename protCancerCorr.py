import sys, re

import gzip

import os

import glob



###open output from iRefExtract4.py which is named protExtract.txt. Put all associated proteins in a list called masterList.

masterList = []

with open ('protExtract.txt', 'r') as extractFile:

	for line in extractFile:

			sections = line.split('\t')

			if len(sections) > 1:

				assProteins = sections[1]

				

				assProteinsList = assProteins.split(',')

				

				for each in assProteinsList:

					if each not in masterList:

						masterList.append(each)











######## open individual patient cancer file, and grab lines that contain proteins in the masterList

	inputFile1 = gzip.open(sys.argv[1], 'r')

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



		proteinOfInterest1 = subsections.split('(')[0]



		







		for each in masterList:

			if each == proteinOfInterest1:

				print each + '\t' + sys.argv[1] + '\t' + line

			if each == proteinOfInterest2:

				print each + '\t' + sys.argv[1] + '\t' + line



	inputFile1.close()
