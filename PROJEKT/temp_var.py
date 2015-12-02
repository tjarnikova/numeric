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
import collections

def temp_load(filelist):

	
	with Dataset(filelist) as nc:
		# print(nc.variables)
		air=nc.variables['air'][...]
		lat =nc.variables['lat'][...]
		lon = nc.variables['lon'][...]
		time = nc.variables['time'][...]

	ArcticCircleLat = 66.562778
	#a circuitous way to find the arctic circle indices
	LatCircle = np.where(lat> 66.562778)
	LatCircle = LatCircle[0]
	latlen = len(LatCircle)
	latstart = (LatCircle[0])
	latend = (LatCircle[latlen-1])

	temp_dic = collections.OrderedDict()
	temp_dic['Jan'] = np.mean(air[0,latstart:latend,:])
	temp_dic['Feb'] = np.mean(air[1,latstart:latend,:])
	temp_dic['Mar'] = np.mean(air[2,latstart:latend,:])
	temp_dic['April'] = np.mean(air[3,latstart:latend,:])
	temp_dic['May'] = np.mean(air[4,latstart:latend,:])
	temp_dic['June'] = np.mean(air[5,latstart:latend,:])
	temp_dic['July'] = np.mean(air[6,latstart:latend,:])
	temp_dic['Aug'] = np.mean(air[7,latstart:latend,:])
	temp_dic['Sep'] = np.mean(air[8,latstart:latend,:])
	temp_dic['Oct'] = np.mean(air[9,latstart:latend,:])
	temp_dic['Nov'] = np.mean(air[10,latstart:latend,:])
	temp_dic['Dec'] = np.mean(air[11,latstart:latend,:])


	dataMap = temp_dic

	starts = [1,32,60,91,121,152,182,213,244,274,305,335]
	ends = np.zeros(len(starts))
	mids = np.zeros(len(starts))
	tempvals = np.zeros(len(starts))



	for i in range(0,12):

		if i == 11:
			ends[i] = 365
			mids[i] = int((starts[i] + ends[i])/2)
		else:
			ends[i] = starts[i+1]-1
			mids[i] = int((starts[i] + ends[i])/2)

	for i in range(0,12):
		if i == 0:
			tempvals[i] = dataMap.get('Jan')
		elif i ==1:
			tempvals[i] = dataMap.get('Feb')
		elif i ==2:
			tempvals[i] = dataMap.get('Mar')
		elif i ==3:
			tempvals[i] = dataMap.get('April')
		elif i ==4:
			tempvals[i] = dataMap.get('May')
		elif i ==5:
			tempvals[i] = dataMap.get('June')
		elif i ==6:
			tempvals[i] = dataMap.get('July')
		elif i ==7:
			tempvals[i] = dataMap.get('Aug')
		elif i ==8:
			tempvals[i] = dataMap.get('Sep')
		elif i ==9:
			tempvals[i] = dataMap.get('Oct')
		elif i ==10:
			tempvals[i] = dataMap.get('Nov')
		elif i ==11:
			tempvals[i] = dataMap.get('Dec')


	days_tointerp = np.zeros([14])
	temp_tointerp = np.zeros([14])
	temp_tointerp[0] = (tempvals[0]+tempvals[11])/2
	temp_tointerp[13] = (tempvals[0]+tempvals[11])/2
	days_tointerp[0] = 1
	days_tointerp[13] = 365
	for i in range(1,13):
		days_tointerp[i] = mids[i-1]
		temp_tointerp[i] = tempvals[i-1]


	x = days_tointerp
	y = temp_tointerp
	f = interpolate.interp1d(x, y,kind='cubic' )
	xnew = np.arange(1,366, 1)
	ynew = f(xnew)   # use interpolation function returned by `interp1d`
	temp_interp = ynew
	plt.plot(x, y, 'o', xnew, ynew, '-')
	plt.show()
	temp_interp = 4
	return(temp_interp)

# yamlfile = 'test.yaml'
filelist = 'met_var/air.mon.ltm.nc'
temp_interp = temp_load(filelist)

# print(temp_interp)
# print(len(temp_interp))
