#This code reduces the tim files to FITS using dspsr. 
################## Importing required libraries #######################

import os, sys
import numpy as np
import os.path

#######################################################################

#Path where all the directories are present
path_prof_start = '/data/test_AGDP/'

#List of pulsars and other parameters
pulsar_files = '/data/test_AGDP/codes/pulsar_testfile.txt'
pulsars_read = np.loadtxt(pulsar_files, dtype = '|S500')
pulsars = pulsars_read[:,0]
nbins = pulsars_read[:,1]
intsub = pulsars_read[:,2]

#Listing of tim files
for i in range(len(pulsars)):
	path_prof = path_prof_start+pulsars[i]+'/tims'
	command1 = 'cd '+path_prof
	
	command2 = 'ls *.tim > Name_of_tim_file.txt'
	print(command2)
	#os.system(command1+'&&'+command2)
	os.popen(command1+'&&'+command2)

#####################################################################


#####################################################################

#Path where all the directories are present
path_prof_start = '/data/test_AGDP/'

#List of pulsars and other parameters
pulsar_files = '/data/test_AGDP/codes/pulsar_testfile.txt'
pulsars_read = np.loadtxt(pulsar_files, dtype = '|S500')
pulsars = pulsars_read[:,0]
nbins = pulsars_read[:,1]
intsub = pulsars_read[:,2]

#Enter the tims folder of respective pulsar and check if the Fits file is 
#already present if not run the dspsr command
for i in range(len(pulsars)):
	path_prof = path_prof_start+pulsars[i]+'/tims'
	psr = pulsars[i]
	par=path_prof+'/'+psr+'.par'
	nb = nbins[i]
	it = intsub[i]
	get_in = "cd "+path_prof
	tim_file = path_prof+'/Name_of_tim_file.txt'
	with open(tim_file, "rb") as file_name:
		filenames = file_name.read().split()[0::1]
	for j in range(len(filenames)):
		fil = filenames[j]
		basename = os.path.basename(fil)
		check = os.path.isfile(path_prof+'/'+fil+'.fits')
		if check==False:
			command = 'dspsr -N '+psr+' -d 1 -b '+nb+' -L '+it+' -A -K -f 334.5 -B -16.0 -k or -e .fits -O '+filenames[j]+' -E '+par+' '+filenames[j]
			print command
			os.popen(get_in+'&&'+command)
		else:
			print('The Fits file already exist')
	command3 = 'cd '+path_prof 
	command4 = 'ls *.fits >'+path_prof+'/Name_of_fits_file.txt    '
	os.popen(command3+'&&'+command4)

a = ['i ran']
np.savetxt('log_makefits', a, fmt ='%s')
############################ End of Program ##############################
 ###### The next program to be executed is remove_bad_profiles.py ####### 
