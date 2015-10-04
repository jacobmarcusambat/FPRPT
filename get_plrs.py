import os
import glob
import re 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import box_2
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("equal")
def sorted_nicely(l):
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key:[convert(c) for c in re.split('([0-9]+)',key)] 
    return sorted(l, key = alphanum_key)
source_file = os.chdir('/home/jacob/Downloads/PROPORES/')
files = sorted_nicely(glob.glob('*.PTin'))
print len(files)
zcors = []
xcors = []
ycors=[]
coins = []
for file in sorted_nicely(files[:]):
	cord = open(file,'r').read().splitlines()[2:-1]
	record = False
	for line in cord:
		f = line.split()
		x = float(f[0:3][0])
		y = float(f[0:3][1])
		z = float(f[0:3][2])
		plrs = [x,y,z]
		if z >= -36.0 and z<= -6.0 and y>=-1.0 and y <= 2.0 and x>= -2.0 and x<= 1.0:
			record = True
			xcors.append(x)
			ycors.append(y)
			zcors.append(z)
	if record:
		coins.append(file)
#print coins
listcontent = ''
plr = open('plr.txt', 'w')
for lis in coins:
	name = lis[:-4] + 'list'
	#print name
	content =  open(name).readlines()[:-1]
	content = ''.join(content)
	listcontent += content
#print len(listcontent)
plr.write(listcontent)
plr.close()
plr_list = open('plr_list.txt','w')
chainfile = os.chdir('/home/jacob/Desktop/S.AureusCOL_seq/')
ch_file  = sorted_nicely(glob.glob('*.fasta'))
pdb_chain = open(ch_file[0]).read().split(">")
for  i,pdbids in enumerate(pdb_chain[:]):
	pds_identifier = pdbids.find('PDBID')
	if pds_identifier >=1:
		chain = pdbids.split("|")[0]
		chain_info = chain.split(":")[-1]
		print chain_info
		merge = open('/home/jacob/Downloads/PROPORES/plr.txt').readlines()
		print len(merge)	
		final = []
		for i, info in enumerate(merge[:]):
			if info.startswith(chain_info):
				final_lists = info.split()[2]
				final.append(final_lists)
		print len(final)
		for resi in final[:]:
			plr_list.write('%s\n' %resi)	
print len(zcors)
print len(xcors)
print len(ycors)		
ax.scatter([x for x in xcors],[y for y in ycors],[z for z in zcors], alpha = 0.2,color = "r")
points = box_2.box()
ax.scatter(points[0], points[1], points[2])
plt.show()



	
