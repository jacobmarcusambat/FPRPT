import os
import glob

#os.chdir('/home/jacob/Desktop/S.AureusCOL_seq/')

#alignment_files = glob.glob('*.aln')
#print alignment_files

#rate_out_files = '/home/jacob/Desktop/RESULT/MODULE2'
#if not os.path.exists(rate_out_files):
	#os.makedirs(rate_out_files)
	#with open(os.path.join(rate_out_files,alignment_files)) as rateout:
#for aln in alignment_files[:25]:
	#print aln
	#os.system('rate4site -s aln -o /home/jacob/Desktop/')

def rate4site():
	os.system('rate4site -s /home/jacob/Desktop/S.AureusCOL_seq/SACOL0098.aln -o /home/jacob/Desktop/SACOL0098.txt')
rate4site()	
