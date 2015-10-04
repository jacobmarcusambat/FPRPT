import os
import fnmatch
from collections import OrderedDict

path = '/home/jacob/Desktop/S.AureusCOL_seq'

def findfiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)
            
for textfile in findfiles(r'/home/jacob/Desktop/S.AureusCOL_seq', '*.fasta'):
    filename = os.path.basename(textfile)
   
filepaths = []
for root, dirs, files in os.walk(path):   
	for file in files:
		if '.fasta' in file:
			path = os.path.join(root, file)
			filepaths.append(path)

def seqfilter():	
	files = open("/home/jacob/Desktop/S.AureusCOL").read().split(">")
	q_ids = []
	querys = []
	for i,ids in enumerate(files[:]):
		query_ids = ids.strip("\n")
		q_ids.append(query_ids)
		querys = ids.strip(" ")[0:9]
		for filepath in filepaths[:]:
			#print filepath
			if querys in filepath:
				content = open(filepath).read()
				if ids not in content:
					new_content =  content + ">"+ids
					newfile = open('/home/jacob/Desktop/S.AureusCOL_seq/%s.fasta' % querys, 'w')
					newfile.write(new_content)	
			else:
				pass
########################################################################

def blancofilter():					
	blanco  = open('/home/jacob/Desktop/blancoDBproteins').read().split('>')
	blancos = []
	for i,pdbs in enumerate(blanco[:]):
		pdb_seqs = pdbs.strip("\n")
		blancos.append(pdb_seqs)
		pdbids = pdbs.strip(" ")[0:6]
	
		path3 = '/home/jacob/Desktop/pdbseq'
		if not os.path.exists(path3):
			os.makedirs(path3)	
			
		with open(os.path.join(path3,"%s.fasta" % pdbids),'w') as outfile:
			outfile.write(pdbs)

#########################################################################

pdbfiles = '/home/jacob/Desktop/pdbseq'

def msafileprep():
	dirlistings = os.listdir(pdbfiles)
	editfiles =[]
	for item in dirlistings:
		if ".fasta" in item:
			editfiles.append(item)
	
	new_files = open("/home/jacob/Desktop/RESULT/P3/S.AureusCOL_Prot_Blast.txt").readlines()
	
	colfiles = '/home/jacob/Desktop/S.AureusCOL_seq'
	
	lists = os.listdir(colfiles)
	input_fasta_files = []
	for input_file in lists:
		if input_file.endswith(".fasta"):
			input_fasta_files.append(input_file)
	
	for fasta_name_ext in input_fasta_files:
		found = False
		fasta_name = fasta_name_ext.split(".")[0]
		for i,prots in enumerate(new_files[:]):
			if fasta_name == prots.split('\t')[0]:
				structure_name = prots.split('\t')[1][1:-1].split(",")[0].replace("'","").strip(" ")
				structure_name_ext = structure_name + ".fasta"
				if structure_name_ext  in editfiles:
					fasta_file = open(colfiles + "/" + fasta_name_ext, "a")
					sequence = open(pdbfiles + "/" + structure_name_ext, "r").readlines()
					fasta_file.write("\n>")
					for line in sequence:
						fasta_file.write(line)
					fasta_file.close()
				else:
					print "Error: Missing pdb file"
					
				found = True
				break
				
		if found == False:
			os.remove(colfiles + "/" + fasta_name_ext)


seqfilter()	
blancofilter()
msafileprep()
