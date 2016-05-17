#!/usr/bin/env python3
# Requires BioPython
import re # imports regular expressions
import sys, glob
from Bio.Seq import Seq
from Bio import SeqIO
import shutil

# Copies .xml files with names matching entries in a fasta file to a new directory
# To run: GatherMatchingFiles.py infile.fa

InFileName = sys.argv[1]
InFilePipe = open(InFileName,'r')

SeqDict = SeqIO.to_dict(SeqIO.parse(InFilePipe, "fasta"))
XmlList = glob.glob('*.xml')
SeqCount = 0
for FileName in XmlList:
	SeqName = FileName.replace('.xml','')
	if SeqName in SeqDict:
		SeqCount += 1
		print(SeqName)
		shutil.copy(FileName,'/Users/matt/Documents/Dropbox/RNA-Seq/GeneOntology/NewFolder')

print("Input file %s contains %d sequences; %d .xml files matched & written to NewFolder" % (InFileName, len(SeqDict), SeqCount))