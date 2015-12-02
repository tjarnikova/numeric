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
import glob, os
import math

def ice_load(filelist):

	with Dataset(filelist) as nc:
	    #print(nc.variables)
	    icec=nc.variables['icec'][...]
	    lat =nc.variables['lat'][...] 
	    lon = nc.variables['lon'][...]
	    time = nc.variables['time'][...]

	#dealing with the mask in icec - assuming it's a value of 0

	w = icec[0,0,0]
	lat[0]
	le_mask = np.ma.getmask(icec)
	icec[le_mask]=0

	firstday = (time[0]) -1 ;
	newtime = time - firstday;

	ArcticCircleLat = 66.562778
	#a circuitous way to find the arctic circle indices
	LatCircle = np.where(lat> 66.562778)
	LatCircle = LatCircle[0]
	latlen = len(LatCircle)
	#print(latlen)
	latstart = (LatCircle[0])
	latend = (LatCircle[latlen-1])

	start_indices = [1,32,60,91,121,152,182,213,244,274,305,335]
	#print(len(start_indices))
	end_indices = [32,60,91,121,152,182,213,244,274,305,335,365]
	for i in range (len(start_indices)):
	    start = start_indices[i]
	    end = end_indices[i]

	    index = (newtime>=start)*(newtime<end)
	    where_index = np.where(index)
	    if i == 0:
	        Jan = where_index
	    if i == 1:
	        Feb = where_index
	    if i == 2:
	        Mar = where_index
	    if i == 3:
	        April = where_index
	    if i == 4:
	        May = where_index
	    if i == 5:
	        June = where_index
	    if i == 6:
	        July = where_index
	    if i == 7:
	        Aug = where_index
	    if i == 8:
	        Sep = where_index
	    if i == 9:
	        Oct = where_index
	    if i == 10:
	        Nov = where_index
	    if i == 11:
	        Dec = where_index
	        
	        
	Ice_cover = collections.OrderedDict()
	Ice_cover['Jan'] = np.mean(icec[Jan,latstart:latend,:])
	Ice_cover['Feb'] = np.mean(icec[Feb,latstart:latend,:])
	Ice_cover['Mar'] = np.mean(icec[Mar,latstart:latend,:])
	Ice_cover['April'] = np.mean(icec[April,latstart:latend,:])
	Ice_cover['May'] = np.mean(icec[May,latstart:latend,:])
	Ice_cover['June'] = np.mean(icec[June,latstart:latend,:])
	Ice_cover['July'] = np.mean(icec[July,latstart:latend,:])
	Ice_cover['Aug'] = np.mean(icec[Aug,latstart:latend,:])
	Ice_cover['Sep'] = np.mean(icec[Sep,latstart:latend,:])
	Ice_cover['Oct'] = np.mean(icec[Oct,latstart:latend,:])
	Ice_cover['Nov'] = np.mean(icec[Nov,latstart:latend,:])
	Ice_cover['Dec'] = np.mean(icec[Dec,latstart:latend,:])


	dataMap = Ice_cover

	starts = [1,32,60,91,121,152,182,213,244,274,305,335]
	ends = np.zeros(len(starts))
	mids = np.zeros(len(starts))
	icevals = np.zeros(len(starts))



	for i in range(0,12):

		if i == 11:
			ends[i] = 365 
			mids[i] = int((starts[i] + ends[i])/2)
		else:
			ends[i] = starts[i+1]-1
			mids[i] = int((starts[i] + ends[i])/2)

	for i in range(0,12):
		if i == 0:
			icevals[i] = dataMap.get('Jan')
		elif i ==1:
			icevals[i] = dataMap.get('Feb')
		elif i ==2:
			icevals[i] = dataMap.get('Mar')
		elif i ==3:
			icevals[i] = dataMap.get('April')
		elif i ==4:
			icevals[i] = dataMap.get('May')
		elif i ==5:
			icevals[i] = dataMap.get('June')
		elif i ==6:
			icevals[i] = dataMap.get('July')
		elif i ==7:
			icevals[i] = dataMap.get('Aug')
		elif i ==8:
			icevals[i] = dataMap.get('Sep')
		elif i ==9:
			icevals[i] = dataMap.get('Oct')
		elif i ==10:
			icevals[i] = dataMap.get('Nov')
		elif i ==11:
			icevals[i] = dataMap.get('Dec')


	days_tointerp = np.zeros([14])
	ice_tointerp = np.zeros([14])
	ice_tointerp[0] = (icevals[0]+icevals[11])/2
	ice_tointerp[13] = (icevals[0]+icevals[11])/2
	days_tointerp[0] = 1
	days_tointerp[13] = 365
	for i in range(1,13):
		days_tointerp[i] = mids[i-1]
		ice_tointerp[i] = icevals[i-1]


	x = days_tointerp
	y = ice_tointerp
	f = interpolate.interp1d(x, y,kind='cubic' )
	xnew = np.arange(1,366, 1)
	ynew = f(xnew)   # use interpolation function returned by `interp1d`
	ice_interp = ynew
	# plt.plot(x, y, 'o', xnew, ynew, '-')
	# plt.show()

	return(ice_interp)

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

def temp_load():

	
	# with Dataset(filelist) as nc:
	# 	# print(nc.variables)
	# 	air=nc.variables['air'][...]
	# 	lat =nc.variables['lat'][...]
	# 	lon = nc.variables['lon'][...]
	# 	time = nc.variables['time'][...]

	# ArcticCircleLat = 66.562778
	# #a circuitous way to find the arctic circle indices
	# LatCircle = np.where(lat> 66.562778)
	# LatCircle = LatCircle[0]
	# latlen = len(LatCircle)
	# latstart = (LatCircle[0])
	# latend = (LatCircle[latlen-1])

	temp_dic = collections.OrderedDict()
	temp_dic['Jan'] = -1.1878#np.mean(air[0,latstart:latend,:])
	temp_dic['Feb'] =  -1.0299#np.mean(air[1,latstart:latend,:])
	temp_dic['Mar'] =    -1.1541#np.mean(air[2,latstart:latend,:])
	temp_dic['April'] = -1.3006#np.mean(air[3,latstart:latend,:])
	temp_dic['May'] = -1.1803#np.mean(air[4,latstart:latend,:])
	temp_dic['June'] = -0.7960 #np.mean(air[5,latstart:latend,:])
	temp_dic['July'] = 0.0897# np.mean(air[6,latstart:latend,:])
	temp_dic['Aug'] =  0.0934 #np.mean(air[7,latstart:latend,:])
	temp_dic['Sep'] = -0.2942#np.mean(air[8,latstart:latend,:])
	temp_dic['Oct'] = -0.7948#.mean(air[9,latstart:latend,:])
	temp_dic['Nov'] =    -1.0141# np.mean(air[10,latstart:latend,:])
	temp_dic['Dec'] = -1.1229  #np.mean(air[11,latstart:latend,:])


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
	# plt.plot(x, y, 'o', xnew, ynew, '-')
	# plt.show()
	#temp_interp = 
	return(temp_interp)


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

	# print('daytime')
	# print(days_tointerp)
	# print(par_tointerp)

	x = days_tointerp
	y = par_tointerp
	f = interpolate.interp1d(x, y,kind='cubic' )
	xnew = np.arange(1,366, 1)
	ynew = f(xnew)   # use interpolation function returned by `interp1d`
	par_interp = ynew

	for i in range(0,len(par_interp)):
		if par_interp[i]<0:
			par_interp[i] = 0


	return(par_interp)

def ccsen_load():
	x = [1,165,166,365]
	y = [.9,.2,.2,.9]
	f = interpolate.interp1d(x, y,kind='cubic' )
	xnew = np.arange(1,366, 1)
	ynew = f(xnew)
	return(ynew)


def met_get(temp_file,ice_file,wind_file):
	met_var = collections.OrderedDict()
	met_var['ice'] = ice_load(ice_file)
	ice = (met_var.get('ice'))
	icemelt = np.zeros(len(ice))
	for i in range(1,len(ice)):
		ice_melt = ice[i-1]-ice[i]
		if(ice_melt>=0):
			icemelt[i] = ice_melt
	met_var['icemelt'] = icemelt
	met_var['temp'] = temp_load()
	met_var['wind'] = wind_load(wind_file)
	met_var['par'] = par_load()
	met_var['ccsen'] = ccsen_load()

	return met_var


temp_file = 'met_var/air.mon.ltm.nc'
wind_file = 'met_var/wspd.sig995.mon.ltm.nc'
ice_file = 'ice/icec.day.mean.2014.v2.nc'



met = met_get(temp_file,ice_file,wind_file)
# print(met.get('icemelt'))
# # temp = (met.get('temp'))
# print(max(temp))
# icemelt = np.zeros(len(ice))
# for i in range(1,len(ice)):
# 	ice_melt = ice[i-1]-ice[i]
# 	if(ice_melt>=0):
# 		icemelt[i] = ice_melt
# xnew = np.arange(1,366, 1)

# plt.plot(xnew,icemelt)
# plt.show()