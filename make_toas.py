#!/usr/bin/python
import os, sys
import numpy as np

pulsar_files = '/data/test_AGDP/codes/pulsar_testfile.txt'
pulsars_read = np.loadtxt(pulsar_files, dtype = '|S500')
pulsars = pulsars_read[:,0]


for i in range(len(pulsars)):
	
	get_into_area = 'cd /data/test_AGDP/'+pulsars[i]+'/tims'

	template = '../../template/'+pulsars[i]+'.std'
	fits = '*.fits'

	toafile1 = pulsars[i]+'.tim1'
	toafile2 = pulsars[i]+'.tim2'

	command_toa = '/psrsoft/bin/pat -f tempo2 -A PGS -s '+template+' '+fits+' > '+toafile1
	print command_toa
	os.popen(get_into_area+"&&"+command_toa)

	with open ('/data/test_AGDP/'+pulsars[i]+'/tims/'+toafile1) as f:
    		lines = f.readlines()
	new = []
	for jk in range(len(lines)):
    
    		if jk == 0:
        		header = 'FORMAT 1'
        		new.append(header)
        
    		else:
        		ll =  lines[jk][:-4] +'OR'
        		new.append(ll)
        		print ll
	print toafile2
	ff = '/data/test_AGDP/'+pulsars[i]+'/tims/'+toafile2
        print ff
	np.savetxt(ff, new, fmt = "%s")



a = ['i ran']
np.savetxt('log_maketoa', a, fmt ='%s')
