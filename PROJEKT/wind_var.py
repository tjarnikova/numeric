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

def wind_load(filelist):

	with Dataset(filelist) as nc:
	#print(nc.variables)
		wspd=nc.variables['wspd'][...]
		lat =nc.variables['lat'][...]
		lon = nc.variables['lon'][...]
		time = nc.variables['time'][...]

	# print(wspd[1,:,:])

	# #dealing with the mask  - assuming it's a value of 0

	# lat[0]
	# le_mask = np.ma.getmask(icec)
	# icec[le_mask]=0

	# firstday = (time[0]) -1 ;
	# newtime = time - firstday;

	ArcticCircleLat = 66.562778
	#a circuitous way to find the arctic circle indices
	LatCircle = np.where(lat> 66.562778)
	LatCircle = LatCircle[0]
	latlen = len(LatCircle)
	latstart = (LatCircle[0])
	latend = (LatCircle[latlen-1])

	wind_dic = collections.OrderedDict()
	wind_dic['Jan'] = np.mean(wspd[0,latstart:latend,:])
	wind_dic['Feb'] = np.mean(wspd[1,latstart:latend,:])
	wind_dic['Mar'] = np.mean(wspd[2,latstart:latend,:])
	wind_dic['April'] = np.mean(wspd[3,latstart:latend,:])
	wind_dic['May'] = np.mean(wspd[4,latstart:latend,:])
	wind_dic['June'] = np.mean(wspd[5,latstart:latend,:])
	wind_dic['July'] = np.mean(wspd[6,latstart:latend,:])
	wind_dic['Aug'] = np.mean(wspd[7,latstart:latend,:])
	wind_dic['Sep'] = np.mean(wspd[8,latstart:latend,:])
	wind_dic['Oct'] = np.mean(wspd[9,latstart:latend,:])
	wind_dic['Nov'] = np.mean(wspd[10,latstart:latend,:])
	wind_dic['Dec'] = np.mean(wspd[11,latstart:latend,:])


	dataMap = wind_dic

	starts = [1,32,60,91,121,152,182,213,244,274,305,335]
	ends = np.zeros(len(starts))
	mids = np.zeros(len(starts))
	windvals = np.zeros(len(starts))



	for i in range(0,12):

		if i == 11:
			ends[i] = 365
			mids[i] = int((starts[i] + ends[i])/2)
		else:
			ends[i] = starts[i+1]-1
			mids[i] = int((starts[i] + ends[i])/2)

		for i in range(0,12):
			if i == 0:
				windvals[i] = dataMap.get('Jan')
			elif i ==1:
				windvals[i] = dataMap.get('Feb')
			elif i ==2:
				windvals[i] = dataMap.get('Mar')
			elif i ==3:
				windvals[i] = dataMap.get('April')
			elif i ==4:
				windvals[i] = dataMap.get('May')
			elif i ==5:
				windvals[i] = dataMap.get('June')
			elif i ==6:
				windvals[i] = dataMap.get('July')
			elif i ==7:
				windvals[i] = dataMap.get('Aug')
			elif i ==8:
				windvals[i] = dataMap.get('Sep')
			elif i ==9:
				windvals[i] = dataMap.get('Oct')
			elif i ==10:
				windvals[i] = dataMap.get('Nov')
			elif i ==11:
				windvals[i] = dataMap.get('Dec')


	days_tointerp = np.zeros([14])
	wind_tointerp = np.zeros([14])
	wind_tointerp[0] = (windvals[0]+windvals[11])/2
	wind_tointerp[13] = (windvals[0]+windvals[11])/2
	days_tointerp[0] = 1
	days_tointerp[13] = 365
	for i in range(1,13):
		days_tointerp[i] = mids[i-1]
		wind_tointerp[i] = windvals[i-1]


	x = days_tointerp
	y = wind_tointerp
	f = interpolate.interp1d(x, y,kind='cubic' )
	xnew = np.arange(1,366, 1)
	ynew = f(xnew)   # use interpolation function returned by `interp1d`
	wind_interp = ynew
	# plt.plot(x, y, 'o', xnew, ynew, '-')
	# plt.show()

	return(wind_interp)

# yamlfile = 'test.yaml'
filelist = 'met_var/wspd.sig995.mon.ltm.nc'
wind_interp = wind_load(filelist)

# print(wind_interp)
# print(len(wind_interp))
