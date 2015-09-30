import os
import subprocess
def invoke():
	bpath = '/home/jacob/Downloads/PROPORES'
	os.environ['PERLLIB'] = bpath + '/module_lib' 
	os.environ['ROTALIB'] =  bpath + '/ROTA_lib_30'
	subprocess.check_call(['perl', bpath + '/Pore_ID.pl' ,'-f', bpath + '/out1.pdb', '-r' ,'1.0','-s','1.2', '-c' ,'1.4', '-n' ,'out1'], env = os.environ)
