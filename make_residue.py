import numpy as np
import os
import sys

os.chdir('/data/test_AGDP/codes/')
pulsar_files = '/data/test_AGDP/codes/pulsar_testfile.txt'


pulsarfile = np.loadtxt(pulsar_files, dtype='|S100')
pulsars = pulsarfile[:,0]
print pulsars


path_residuals ='/data/test_AGDP/residuals/'

for i in range(len(pulsars)):
	par = '/data/test_AGDP/'+pulsars[i]+'/tims/'+pulsars[i]+'.par'
	print par 
	tim = '/data/test_AGDP/'+pulsars[i]+'/tims/'+pulsars[i]+'.tim2'
	print tim
	command1 = 'tempo2 -output general2 -s "{sat}\\t{pre}\\n" -f '+par+' '+tim+' > /data/test_AGDP/codes/residuals.txt'
	print(command1)
	os.popen(command1)
	command2 = "/usr/bin/grep '^[0-9]' /data/test_AGDP/codes/residuals.txt > "+path_residuals+pulsars[i]+'.resi'
	print command2
	os.popen(command2)
