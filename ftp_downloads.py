from Bio import Entrez
from urllib2 import HTTPError
import time
import os


Entrez.email ="ambat.jacob@gmail.com"

path = '/home/jacob/Desktop/RESULT/P3/S.AureusCOL_Blast.txt'

p3files = open(path,'r').readlines()

d = {}
for hits in p3files[:]:
	key,value = hits.strip("\n").split("\t")[0],hits.strip("\n").split("\t")[1:]
	key = key.strip('\t')
	value = [str(x).split('|')[0:] for x in value]
	for items in value:
		value_S = items[1]
		notgood = items[0].split('[')[-1]
		notgood_s = notgood.split("'")[-1]
		if 'pdb' in notgood_s:
			pass
		elif key not in d:
			d[key] = [value_S]
		else:
			d[key].append(value_S)	


ftps = open("/home/jacob/Desktop/RESULT/P3/Entrez_ids.txt",'w')
for item in d.keys()[:]:
	line = item
	hits = d[item]
	for hit in hits:
		line += '\t%s' % hit
	ftps.write("%s\n" % line)	
	
#for items in d:
	#value = d[items]
	#print value
	
	
#itempaths=[]
for item in d:
	
	ftp_path = '/home/jacob/Desktop/RESULT/FTP'
	
	if os.path.exists(ftp_path):
		print "File already exists"
	
	else:
		#if not os.path.exists(ftp_path):
		os.makedirs(ftp_path)
		item_path = ftp_path + '/%s' %item
		print item_path
		#itempaths.append(item_path)
		if not os.path.exists(item_path):
			os.makedirs(item_path)
			
			counter = 0
			values = d[item]
			
			os.chdir(item_path)
			for value in values:
				out = open('%s' % value, 'w')
				fetch_success = False
				while(fetch_success == False):
					try:
						handle = Entrez.efetch(db="protein", id=value, retmode="xml")
						records = Entrez.read(handle)
						fastaseq = value.rstrip()+" "+records[0]["GBSeq_primary-accession"]+" "+records[0]["GBSeq_definition"]+"\n"+records[0]["GBSeq_sequence"]
						out.write(fastaseq)
						out.close()
						fetch_success = True
					except:
						pass
					time.sleep(1) # to make sure not many requests go per second to ncbi	
			counter += 1
		
	

