import sys
import re
import subprocess
import os

files = os.listdir("/home/pboothe/mito/results/20130626_psiBlast_resultsFIX")

for item in files:






	subprocess.call(["fastacmd", "-d", "/home/pboothe/mito/data/nr/nr", "-i", "/home/pboothe/mito/results/20130626_psiBlast_resultsFIX", item, "-o", "Testinput.fas"])





