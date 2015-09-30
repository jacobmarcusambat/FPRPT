#!/usr/bin/python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from itertools import product, combinations
import os
import re
import math
from pymol.cgo import *
from pymol import cmd
from pymol.vfont import plain
import box
import glob
from os.path import basename
import invokepores

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("equal")

os.chdir("/home/jacob/Downloads/opm files/")
chainss = open("/home/jacob/Downloads/out5.txt",'r').readlines()
opm_name = glob.glob("*.pdb")

chains = []
for names in opm_name[:]:
	pdb_name = names.split(".")[0]
	pdb_name_1 = pdb_name[:-3].upper()
	for pd in chainss[:]:
		chain_name = ''
		if  pdb_name_1 in pd:
			chain_name += pd.split(':')[1][0]
			print chain_name
		pdb = open(names,'r').readlines()
		
		charged_res = []
		x =[]
		z =[]
		z_select = []
		y =[]
		com = []
	print chain_name
	for item in pdb:
		if item.startswith('ATOM'):
			item = item.replace('',"")
			item = item.split()
			if item[4] == chain_name:
				#print item
				x.append(float(item[6]))
				y.append(float(item[7]))
				z.append(float(item[8]))
	
	for item in z[:]:
		if -15.0<= item and item <=15.0:
			z_select.append(item)
				
	x_cord = sum(x)/len(x)
	y_cord = sum(y)/len(y)
	z_cord = sum(z_select)/len(z_select)
	one_comp = box.box((x_cord,y_cord,z_cord))
	out1 = open(names + '_box ' + '.txt','w')
	out1.write(str(one_comp))
	out1.close()
	
	##########################3d-plot###################################
	
	centre = ax.scatter([x_cord],[y_cord],[z_cord],color="g",s=100)
	points = box.box((x_cord,y_cord,z_cord))
	scatterfile = ax.scatter(points[0], points[1], points[2],color = "r")
	plt.show()

invokepores.invoke()

