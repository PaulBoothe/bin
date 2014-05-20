import sys, re

from collections import defaultdict



inputFile = open(sys.argv[1], "r")

#outputFile = open(sys.argv[1] + ".output.txt", "w")





d = defaultdict(list)

#intialize ryan_gene_list:

ryanGeneList = ['MFN1', 'MFN2', 'OPA1', 'PHB2', 'STOML2', 'FIS1', 'DNM1L', 'MFF', 'MIEF2', 'SH3GLB1', 'GDAP1']






######################build complex dictionary: d  ##########################
#check file for complexes and put them in dictionary

for line in inputFile:

      for each in ryanGeneList:

              if each in line:

                sections = line.split('\t')

                c5 = sections[4].split('|')[0].split(':')[1] 

                c6 = sections[5].split('|')[0].split(':')[1]

                com1 = line.split('\t')[0]

                #grab only lines that have a complex in the first column: (no complexes in second column)

                if 'complex:' in com1:

                        #check to see if c6 is not in dictionary entry for the key c5:

                  if c6 not in d[com1]:

                  #if it is not, add it in.

                    d[com1].append(c6)

                    #if it is, done.

                    #ALL complexes and associated proteins are now in dictionary.



#Close and reopen inputFile. Not sure why. Won't work otherwise.

inputFile.close()

#########################build protein dictionary: dProtein    #######################

#initialize dictionary for proteins

dProtein = defaultdict(list)



#scan file, grab lines that aren't metadata(#), and that have a ryangene list protein in them. c5 and c6 represent column 1 and column 2. 

#construction of dProtein dictionary (a dictionary that contains ryanGeneList proteins and their associated)

for line in inputFile:

        if not line.startswith("#"):

          sections = line.split('\t')

          c5 = sections[4].split('|')[0].split(':')[1]  #first column

          listSections = sections[5].split('|')[0].split(':')[1] 

          c6 = [listSections] #second column

          for each in ryanGeneList:

            if each in c5: # if any genes in the ryan gene list are in the c5 sections (which have exact name copies of certain ryangeneList genes)

              if c6 not in dProtein[c5]:

                        dProtein[c5].append(c6)        



                        

                          

                          

                          

                           

                            

                                            

#dProtein dictionary is built, but still does not have complexes

#scan file again for complexes, add complex to list of ryanGeneList proteins, and then display contents of complex defined in d dictionary built above.





          #now scanning c5 instead of c6. c5 must be a list to dynamically add a list to the value of a dictionary.

          listSectionsc5com = sections[4].split('|')[0].split(':')[1]

          c5com = [listSectionsc5com]

          c6com = sections[5].split('|')[0].split(':')[1]

          complexColumn = sections[0]





                                        

          for each in ryanGeneList:

            if each in c6com: 

                                                

              if 'complex:' in complexColumn:

                

                

                for complexListing in d[complexColumn]:

                  



                    if complexListing not in dProtein[c6com]: #if complex is not already listed in dProtein dictionary listing for ryanGeneList Protein

                      

                        dProtein[c6com].append(complexListing)





                        

                    



                                           

                                            

                                            

                                              



                                        

                                        

          #switch back columns to no list.

          c5 = sections[4]

          c6 = sections[5]

############################################print###################3

for each in dProtein: ###################correct format



    listString = ', '.join(str(x) for x in dProtein[each])

    listString = listString.replace('[','')

    listString = listString.replace(']','')

    listString = listString.replace('\'','')  



    print each + '\t' + listString + '\n'
