import glob, os
import numpy as np
import yaml
from collections import namedtuple
import scipy
import yaml
import matplotlib.pyplot as plt
from scipy import interpolate
import netCDF4
from netCDF4 import Dataset
import numpy as np
from types import *
import numpy.ma as ma
import math
import collections
# os.chdir("./par")
i = 0 

def par_load():
	store_par = np.zeros(12)
	months = np.arange(1,13, 1)
	# print(months)
	# print(store_par)
	i = 0

	for file in glob.glob("./par/*.nc"):
		#print(file[12:15])

		with Dataset(file) as nc:
			#print(nc.variables)
			par=nc.variables['par'][...]
			lat=nc.variables['lat'][...]
			lon=nc.variables['lon'][...]
			le_mask = np.ma.getmask(par)
			par[le_mask]=np.NaN
			ArcticCircleLat = 66.562778
			#a circuitous way to find the arctic circle indices
			LatCircle = np.where(lat> 66.562778)
			LatCircle = LatCircle[0]
			latlen = len(LatCircle)
			latstart = (LatCircle[0])
			latend = (LatCircle[latlen-1])

			par_mean = (np.nanmean(par[latstart:latend,:]))
			# print(par_mean)
			if math.isnan(par_mean) == False:
				store_par[i] = par_mean
			# print('*')
			# print(i)
			i = i+1

	# plt.plot(months, store_par, 'o')
	# plt.show()

	starts = [1,32,60,91,121,152,182,213,244,274,305,335]
	ends = np.zeros(len(starts))
	mids = np.zeros(len(starts))
	parvals = store_par

	for i in range(0,12):

		if i == 11:
			ends[i] = 365 
			mids[i] = int((starts[i] + ends[i])/2)
		else:
			ends[i] = starts[i+1]-1
			mids[i] = int((starts[i] + ends[i])/2)

	days_tointerp = np.zeros([14])
	par_tointerp = np.zeros([14])
	par_tointerp[0] = (parvals[0]+parvals[11])/2
	par_tointerp[13] = (parvals[0]+parvals[11])/2
	days_tointerp[0] = 1
	days_tointerp[13] = 365

	for i in range(1,13):
		days_tointerp[i] = mids[i-1]
		par_tointerp[i] = parvals[i-1]

	print('daytime')
	print(days_tointerp)
	print(par_tointerp)

	x = days_tointerp
	y = par_tointerp
	f = interpolate.interp1d(x, y,kind='cubic' )
	xnew = np.arange(1,366, 1)
	ynew = f(xnew)   # use interpolation function returned by `interp1d`
	par_interp = ynew


	return(par_interp)

storepar = par_load()
print(storepar)

xnew = np.arange(1,366, 1)

for i in range(0,len(storepar)):
	if storepar[i]<0:
		storepar[i] = 0
plt.plot(xnew, storepar, 'o-')
plt.show()



# starts = [1,32,60,91,121,152,182,213,244,274,305,335]
# ends = np.zeros(len(starts))
# mids = np.zeros(len(starts))
# parvals = storepar

# for i in range(0,12):

# 	if i == 11:
# 		ends[i] = 365 
# 		mids[i] = int((starts[i] + ends[i])/2)
# 	else:
# 		ends[i] = starts[i+1]-1
# 		mids[i] = int((starts[i] + ends[i])/2)

# days_tointerp = np.zeros([14])
# par_tointerp = np.zeros([14])
# par_tointerp[0] = (parvals[0]+parvals[11])/2
# par_tointerp[13] = (parvals[0]+parvals[11])/2
# days_tointerp[0] = 1
# days_tointerp[13] = 365

# for i in range(1,13):
# 	days_tointerp[i] = mids[i-1]
# 	par_tointerp[i] = parvals[i-1]

# print(days_tointerp)
# print(par_tointerp)