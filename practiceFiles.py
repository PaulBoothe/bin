import sys,re


d = {}
matchIDlist = []

for i in range(1,4):
	with open(sys.argv[1], 'r') as input:
		with open('outputNumber%i.txt' %i, 'w') as output:
			lines = input.readlines()
			for line in lines:
				output.write(line)
						
						
					
		

output.close()


