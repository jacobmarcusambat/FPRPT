import os
import glob

os.chdir('/home/jacob/Desktop/S.AureusCOL_seq/')

alignment_files = glob.glob('*.aln')
print alignment_files

rate_out_files = '/home/jacob/Desktop/RESULT/MODULE2'
if not os.path.exists(rate_out_files):
	os.makedirs(rate_out_files)
	with open(os.path.join(rate_out_files,alignment_files)) as rateout:
		os.system('rate4site -s alignment_files -o rate_out_files')
rate4site()
