# This program moves the Fits files where there is no detection to the 
# folder= bad/ .

################## Importing required libraries #######################

import os, sys
import numpy as np
import os.path
import psrchive

#######################################################################

#Path where all the directories are present
path_prof_start = '/data/test_AGDP/'

#List of pulsars and other parameters
pulsar_files = '/data/test_AGDP/codes/pulsar_testfile.txt'
pulsars_read = np.loadtxt(pulsar_files, dtype = '|S500')
pulsars = pulsars_read[:,0]
nbins = pulsars_read[:,1]
intsub = pulsars_read[:,2]
min_snr = pulsars_read[:,3]

#Check if the SNR of the profile is less than the minimum SNR
#If so move the fits and tim files to bad/ folder.
for i in range(len(pulsars)):
	path_prof = path_prof_start+pulsars[i]+'/tims'
	path_bad = path_prof_start+pulsars[i]+'/bad/'
	fits_file = path_prof+'/Name_of_fits_file.txt'
	with open(fits_file, "rb") as file_name:
		filenames = file_name.read().split()[0::1]
	for j in range(len(filenames)):
		msnr = min_snr[i]
		fil = filenames[j]
		arch = psrchive.Archive_load(path_prof+'/'+fil)
		arch.tscrunch()	
	 	snr = arch.get_Profile(0,0,0).snr()	
		diff = float(snr) - float(msnr)
		if diff < 0.0:
			basename1 = os.path.basename(fil)
			basename = os.path.splitext(basename1)[0]
			command1 = 'mv '+path_prof+'/'+fil+' '+path_bad	
			command2 = 'mv '+path_prof+'/'+basename+' '+path_bad
			os.popen(command1+'&&'+command2)


a = ['i ran']
np.savetxt('log_removebadfits', a, fmt ='%s')


######################## End of Program #################################
###### The next program to be executed is make_toa_with_psrchive.py #######
