import netCDF4
from netCDF4 import Dataset
import numpy as np
from types import *
import numpy.ma as ma
import collections
import matplotlib.pyplot as plt
filelist = 'met_var/air.mon.ltm.nc'
with Dataset(filelist) as nc:
    #print(nc.variables)
    # icec=nc.variables['icec'][...]
    lat =nc.variables['lat'][...] 
    lon = nc.variables['lon'][...]
    time = nc.variables['time'][...]
    air = nc.variables['air'][...]
LatCircle = np.where(lat> 66.562778)
LatCircle = LatCircle[0]

latlen = len(LatCircle)
print(latlen)
latstart = (LatCircle[0])
latend = (LatCircle[latlen-1])
print(latend)
test = air[1,40,1]
print(test)

mon_temp = np.zeros([12])
for i in range (0,12):
	mon_temp[i] = np.mean(air[i,latstart:latend,:])

plt.plot(mon_temp)
plt.show()