import subprocess
import sys
import os
import glob
from Bio.Align.Applications import ClustalOmegaCommandline

os.chdir("/home/jacob/Desktop/S.AureusCOL_seq/")

files = glob.glob("*.fasta")


def clustalo():
	for fasta_files in files[:]:
		fasta_file_s = fasta_files.split('.')[0]
		print fasta_file_s
		cline = ClustalOmegaCommandline('clustalo',infile = fasta_files,outfile = fasta_file_s + '.aln' ,verbose= False, auto=True)
		cline()
clustalo()
