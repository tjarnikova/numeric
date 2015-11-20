import netCDF4
from netCDF4 import Dataset
import numpy as np
from types import *
import numpy.ma as ma
import collections

filelist = 'ice/icec.day.mean.2014.v2.nc'
with Dataset(filelist) as nc:
    print(nc.variables)
    # icec=nc.variables['icec'][...]
    # lat =nc.variables['lat'][...] 
    # lon = nc.variables['lon'][...]
    # time = nc.variables['time'][...]