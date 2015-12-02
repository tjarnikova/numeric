import glob, os
import numpy as np

import scipy

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
	# plt.plot(months, store_par, 'o')
	# plt.show()

x = [1,165,166,365]
y = [.9,.2,.2,.9]
f = interpolate.interp1d(x, y,kind='cubic' )
xnew = np.arange(1,366, 1)
ynew = f(xnew)   # use interpolation function returned by `interp1d`



plt.plot(xnew, ynew, 'o-')
plt.show()

