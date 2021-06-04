#!/usr/bin/python
import numpy as np 
import matplotlib.pyplot as plt 
import sys
import astropy.stats as st
import smtplib

path_residue = '/data/AGDP/residuals/'

path_contact = '/data/AGDP/codes/'

path_pulsar_file = '/data/AGDP/codes/'

contact_file = path_contact+'contacts.txt'

pulsar_file = path_pulsar_file+'pulsar_file.txt'

contacts = np.loadtxt(contact_file, dtype='|S500')

emails = contacts

pulsar_details = np.loadtxt(pulsar_file, dtype = '|S500')

pulsar = pulsar_details[:,0]

window = pulsar_details[:,1]

cutoff = pulsar_details[:,2]

mjd_start = pulsar_details[:,3]

win = np.round( [float(i) for i in window], 20)

CUTOFF = np.round( [float(j) for j in cutoff], 20)

MJD_start = np.round( [float(k) for k in mjd_start], 20)



msg_gen = 'Hi, \n \n Right now the AGDP has finished analysis. Today the pipeline ran sucessfully \n \n Thanks \n \n RAC-OOTY\n Glitch monitoring system'


for k in emails:
	print '\n\n\n Im here \n\n\n\n'
	fromaddr = "ortglitches@gmail.com"
	toaddr =k
	message = msg_gen
	password = '***********'  #provide the password here
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.set_debuglevel(1)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(fromaddr, password)
	server.ehlo()
	server.sendmail(fromaddr, toaddr, message)


server.quit()



for l in range(len(pulsar)):
	
	psr = pulsar[l]
	residue = path_residue+pulsar[l]+'.resi'
	bad_toa = path_residue+pulsar[l]+'.bad.toa'

	
	msg = 'Hi, \n \n  Probably the pulsar '+ pulsar[l] +' has glitched today kindly look at the phase connected solutions. \n \n Thanks \n \n RAC-OOTY\n Glitch monitoring system'




	###Start reading the residues of pulsar ###
	timing_solution=np.loadtxt(residue)
	MJD=timing_solution[:,0]
	bad_index=[]
	index = np.where( MJD > MJD_start[l] )[0]
	print 'U HAVE CHOSEN TO SEARCH GLITCH AFTER MJD, ', MJD_start[l], 'for pulsar ', psr, 'with MAD cut-off', CUTOFF[l], 'and Window ', int(win[l]), '\n '
	MJD = MJD[index]
	try:
		bad_mjd = np.loadtxt(bad_toa)
		bad_mjd == True
	except:
		IOError
		bad_mjd = []
	for i in range(len(MJD)):
		if np.size(bad_mjd)== 0:
			bad_index = []
		if np.size(bad_mjd)== 1:
			if (np.abs(MJD[i]-bad_mjd) < 0.001):
				bad_index.append(i)
		else:
			for k in range(len(bad_mjd)):
				if (np.abs(MJD[i]-bad_mjd[k]) < 0.001):
					bad_index.append(i)
	MJD = np.delete(MJD,bad_index)
	post_fit_residuals=timing_solution[:,1]
	post_fit_residuals=post_fit_residuals[index]
	post_fit_residuals= np.delete(post_fit_residuals,bad_index)

	CONDITION_CUTOFF = CUTOFF[l]

	NOT_FOUND = False
	FOUND = True

	NUmber_of_obs = len(MJD)



	## Method : MAD median absolute deviation



	window = int(win[l])
	


	glitch_global_epoch =[]
	glitch_epoch=[]
	length = len(post_fit_residuals) - window +1


	b=np.arange(length)


	for k in range(len(b)):
		moving_box=post_fit_residuals[k:k+window]
	    	M= np.median(moving_box)
		MAD= st.median_absolute_deviation(moving_box)
		if (MAD == 0.0):
			condition=np.zeros(window)
		else:
			condition = (np.abs((moving_box-M)/MAD))


	
		for i in range(len(condition)):
			try:
				MJD[k+i+1] == NOT_FOUND
				if (condition[i] >= CONDITION_CUTOFF):

	######## HERE YOU SEND SMS OR EMAIL #######################
					ll = MJD[k+i-1]
					uu = MJD[k+i]
					print 'GLITCH OCCURED BETWEEN MJD', MJD[k+i-1], 'and', MJD[k+i]
					
					for k in range(len(emails)):
						#print emails[k]

						fromaddr = "ortglitches@gmail.com"
						message = msg
						password = '********' #provide password here
						server = smtplib.SMTP('smtp.gmail.com:587')
						server.set_debuglevel(1)
						server.ehlo()
						server.starttls()
						server.ehlo()
						server.login(fromaddr, password)
						server.ehlo()
						server.sendmail(fromaddr, toaddr, message)
					server.quit()
				
			except:
				IndexError



	
		












