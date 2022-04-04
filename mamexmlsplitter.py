# MAME XML Splitter
# Author: NebularNerd Version 1.0 (2022)
# https://github.com/NebularNerd/mamexmlsplitter
# Import required packages
import sys
import os
import os.path

# Setup argparse
import argparse
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description='Split MAME.xml into custom .xml, Great for Neo-Geo, Naomi, AtomisWave etc...\nVisit https://github.com/NebularNerd/mamexmlsplitter for more information')                                               
parser.add_argument("--file", "-f", type=str, required=True, help='Path to MAME.xml file, enclose in quotes if path has spaces')
parser.add_argument("--sourcefile", "-src", type=str, required=True, help='Name of system sourcefile, e.g. naomi.cpp')
args = parser.parse_args()
# Setup some basic file wrangling stuff
inputfile = os.path.normpath(args.file)
inputdirectory = os.path.dirname(args.file)
outputfile = os.path.join(inputdirectory +"\\mame-"+ args.sourcefile[:-4]+".xml")
print('MAME.xml Splitter 1.0\n')
print('Input .xml file      : ',args.file)
print('String to search for : ',args.sourcefile)
print('Output .xml file     : ',outputfile,"\n\n")

# Now we do stuff
# Parts adapted from https://stackoverflow.com/questions/55264953/copy-lines-between-two-strings-to-another-file and https://stackoverflow.com/questions/58773880/str-contains-pandas-returns-str-object-has-no-attribute-contains
answer = None 
while answer not in ("y","n"): 
    answer = input("Shall we proceed? ") 
    if answer == "y": 
        textfile = open(inputfile, 'r', encoding="utf8")
        writing = False
        linecount = 0
        firstline = 0
        line1 = '<?xml version="1.0"?>\n<mame>\n'
        lastline = "</mame>"
        with open(inputfile, 'r', encoding="utf8") as original, open(outputfile, 'w', encoding="utf8") as new:
            for line in original:
                if firstline == 0:
                    new.write(line1)
                    firstline = firstline+1
                if args.sourcefile in line:
                    writing = True
                elif '</machine>' in line and linecount > 1:
                    new.write(line)
                    writing = False
                    linecount = 0
                elif '</machine>' in line:
                    writing = False    

                if writing:
                    new.write(line)
                    linecount = linecount+1
            new.write(lastline)

    elif answer == "n": 
        print ("OK, bye for now...\n\n")
    else: 
    	print("Please enter y or n.") 
















