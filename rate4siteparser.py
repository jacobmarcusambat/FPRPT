import os
import re
import scipy.stats as stats
import matplotlib.pyplot as plt
import pylab as plt2
import numpy as np
from decimal import *
from scipy.stats import norm
from sklearn import preprocessing
from math import floor, ceil 


#path = '/home/jacob/Desktop/'



#rootDir = '.'
#blast_files = []
#for root, subdirList, fileList in os.walk(rootDir, topdown=False):
	##print ("%s" % dirName)
	#for fname in fileList:
		##print ("%s" % fname)
		#if fname.startswith("S.A"):
			#fname = os.path.join(root, fname)
			#blast_files.append(fname)
#print blast_files


rate_file = open('/home/jacob/Desktop/rate4siteoutputs/SACOL/SACOL0098','r')
confidence = []
data_reqs = []
fil_data = []
#datas = open('data.txt','w')
#datas_filter = open('data_filter','w')
scores = []
residues = []
range1 = []
range2=[]
y_count = []
for i,interval in enumerate(rate_file):
	if i == 0:
		True
	else:
		if not interval.startswith('#') and interval != '\n':
			interval = interval.split(',')
			parts1 = interval[0].split()
			seq = parts1[0]
			res = parts1[1]
			residues.append(res)
			#print res
			y_count.append(seq)
			score = parts1[2]		
			scores.append(float(score))					
			range1.append(parts1[3][1:])
			range1 = [item for item in range1 if item.strip()]					
			parts2 = interval[-1].split()
			range2.append(parts2[0][:-1])
			range2 = [item for item in range2 if item.strip()]
			range_diff = range2 + range1
			confidence.append(interval)
			data_reqs.append([score,range_diff])
#print residues		
fig, ax = plt.subplots(1, 1)
mean, var, skew, kurt = norm.stats(moments='mvsk')

rang = [min(scores), max(scores)]
Long = len(scores)
Maxim = max(scores) #MaxValue
Minim = min(scores) #MinValue
av = np.mean(scores) #Average
StDev = np.std(scores) #Standard Dev.

x = np.linspace(Minim, Maxim, Long)
ax.plot(x, norm.pdf(x, av, StDev),'r-', lw=3, alpha=0.9, label='norm pdf')

weights = np.ones_like(scores)/len(scores)

normalized = [(s-min(scores))/(max(scores)-min(scores)) for s in scores]

ax.hist(normalized, weights = weights, normed=True, histtype='stepfilled', alpha=0.2)


plt.figure(figsize=(10,8))

y_count = map(int, y_count)

bins = np.arange(floor(min(normalized[:])), ceil(max(normalized[:])), 0.10)

colors = ('blue', 'red', 'green','cyan','purple','pink','violet','lime','aqua','brown')

# get the max count for a particular bin for all classes combined
max_bin = max(np.histogram(normalized[:], bins=bins)[0])

pairs = [(x,y) for x,y in zip(normalized, residues)]
group1 = []
group2 = []
group3 = []
for item in pairs[:]:
	if item[0]<= 0.3:
		group1.append(item)
	elif 0.4 <= item[0] <=0.7:
		group2.append(item)
	else:
		group3.append(item)	
print len(group1)
#print group1
print len(group2)
print len(group3)
		
conserved_residues = open('conserved_residues.txt', 'w')
for items in group1[:]:
	conserved_residues.write('%s\n' %items[1])		
	
for label,color in zip(range(1,10), colors):
    mean = np.mean(normalized[:][y_count == label]) # class sample mean
    stdev = np.std(normalized[:][y_count == label]) # class standard deviation
n, bins, patches = plt.hist(normalized[:], bins , alpha=0.3, label = 'class {} ($\mu={:.2f}$, $\sigma={:.2f}$)'.format(label, mean, stdev))

for c, p in zip(colors, patches):
	plt.setp(p, 'facecolor', c)  
plt.ylim([0, max_bin*1.3])
plt.title('normalized data')
plt.xlabel('normalized score in 10 bins', fontsize=14)
plt.ylabel('count', fontsize=14)
plt.legend(loc='upper right')
plt.show()

	


