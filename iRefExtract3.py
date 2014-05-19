import sys, re

from collections import defaultdict



inputFile = open(sys.argv[1], "r")

#outputFile = open(sys.argv[1] + ".output.txt", "w")





d = defaultdict(list)

#intialize ryan_gene_list:

ryanGeneList = ['uniprotkb:Q8IWA4', 'uniprotkb:O95140', 'uniprotkb:O60313', 'uniprotkb:Q99623', 'uniprotkb:Q9UJZ1', 'uniprotkb:Q9Y3D6', 'uniprotkb:O00429', 'uniprotkb:Q9GZY8', 'uniprotkb:Q96C03', 'uniprotkb:Q9Y371', 'uniprotkb:Q8TB36']







#check file for complexes and put them in dictionary

for line in inputFile:

      for each in ryanGeneList:

              if each in line:

                      c1 = line.split('\t')[0]

                      c2 = [line.split('\t')[1]]

                      #grab only lines that have a complex in the first column: (no complexes in second column)

                      if 'complex:' in c1:

                              #check to see if c2 is not in dictionary entry for the key c1:

                              if c2 not in d[c1]:

                              #if it is not, add it in.

                                      d[c1].append(c2)

                                      #if it is, done.

                                      #ALL complexes and associated proteins are now in dictionary.



#Close and reopen inputFile. Not sure why. Won't work otherwise.

inputFile.close()

inputFile = open(sys.argv[1], "r")









#initialize dictionary for proteins

dProtein = defaultdict(list)



#scan file, grab lines that aren't metadata(#), and that have a ryangene list protein in them. c1 and c2 represent column 1 and column 2. 

#construction of dProtein dictionary (a dictionary that contains ryanGeneList proteins and their associated)

for line in inputFile:

        if not line.startswith("#"):

                for each in ryanGeneList:

                                if each in line:

                                        sections = line.split('\t')

                                        c1 = sections[0]  #first column

                                        c2 = [sections[1]] #second column



                                        #if ryanGeneList protein is in c1, add c2 to its dProtein dict value

                                        if each in c1:

                                                if c2 not in dProtein[c1]:

                                                        dProtein[c1].append(c2)

#dProtein dictionary is built, but still does not have complexes

#scan file again for complexes, add complex to list of ryanGeneList proteins, and then display contents of complex defined in d dictionary built above.





                                        #now scanning c1 instead of c2. c1 must be a list to dynamically add a list to the value of a dictionary.

                                        c1com = [sections[0]]

                                        c2com = sections[1]





                                        for each in c1com: #must use for loop because we are grabbing from a list. This list only has one item.

                                               

                                                if 'complex:' in each:

                                                        if each not in dProtein[c2com]: #if complex is not already listed in dProtein dictionary listing for ryanGeneList Protein

                                                                dProtein[c2com].append(each)

                                                                



                                                                for item in d[each]: #d[each] is a list of proteins associated with a complex

                                                                        

                                                                        

                                                                        dProtein[c2com].append(item) #add each of the associated proteins defined in d to dProtein values for the correct protein listing.







                                        #switch back columns to no list.

                                        c1 = sections[0]

                                        c2 = sections[1]







                                #if protein complex is in c1, that means c2 is a protein in the ryanGeneList. 

                                        #check if c1 (protein complex) is already in the dProtein dictionary list of values for key ryan protein. If not...









                                        # if 'complex:' in c1:

                                        #       print 'found complex in c1'

                                        #       if c1 not in dProtein[c2]:

                                        #               print 'c1 not in dProtein[c2]'

                                        # #Assign protein complex to dProtein[c2]. So dProtein[c2].append(c1)

                                        #               dProtein[c2].append(c1)

                                        #               print dProtein[c2]

                                        #now dProtein[ryangene] has an added value, which is the protein complex. 

                                        #how to display key and value?



for x,y in dProtein.items():

        print x

        print "\n"

        print y

        print "\n\n\n"



















                #outputFile.write("Found DRP1")



#outputFile.close()

