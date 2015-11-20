import numpy as np
import yaml
from collections import namedtuple
import scipy
import yaml
import matplotlib.pyplot as plt
from scipy import interpolate





f = open('test.yaml')
dataMap = yaml.load(f)


# w = dataMap.values() 
# print(w)
# print(type(w))
# for key, value in dataMap.iteritems():
#     temp = [key,value]
#     dictlist.append(temp)

sandwich = dataMap.get('icevars', {}).get('Jan')
print(sandwich)
print(type(sandwich))


starts = [1,32,60,91,121,152,182,213,244,274,305,335]
ends = np.zeros(len(starts))
mids = np.zeros(len(starts))
icevals = np.zeros(len(starts))
for i in range(0,12):
	#print('kitten')
	if i == 11:
		ends[i] = 365 
		mids[i] = int((starts[i] + ends[i])/2)
	else:
		ends[i] = starts[i+1]-1
		mids[i] = int((starts[i] + ends[i])/2)

for i in range(0,12):
	if i == 0:
		icevals[i] = dataMap.get('icevars', {}).get('Jan')
	elif i ==1:
		icevals[i] = dataMap.get('icevars', {}).get('Feb')
	elif i ==2:
		icevals[i] = dataMap.get('icevars', {}).get('March')
	elif i ==3:
		icevals[i] = dataMap.get('icevars', {}).get('April')
	elif i ==4:
		icevals[i] = dataMap.get('icevars', {}).get('May')
	elif i ==5:
		icevals[i] = dataMap.get('icevars', {}).get('June')
	elif i ==6:
		icevals[i] = dataMap.get('icevars', {}).get('July')
	elif i ==7:
		icevals[i] = dataMap.get('icevars', {}).get('Aug')
	elif i ==8:
		icevals[i] = dataMap.get('icevars', {}).get('Sept')
	elif i ==9:
		icevals[i] = dataMap.get('icevars', {}).get('Oct')
	elif i ==10:
		icevals[i] = dataMap.get('icevars', {}).get('Nov')
	elif i ==11:
		icevals[i] = dataMap.get('icevars', {}).get('Dec')
print(icevals)
print(ends)
print(mids)

days_tointerp = np.zeros([14])
ice_tointerp = np.zeros([14])
ice_tointerp[0] = (icevals[0]+icevals[11])/2
ice_tointerp[13] = (icevals[0]+icevals[11])/2
#print(to_interp)
days_tointerp[0] = 1
days_tointerp[13] = 365
for i in range(1,13):
	days_tointerp[i] = mids[i-1]
	ice_tointerp[i] = icevals[i-1]

# #print(to_interp)
# plt.plot(mids,icevals)
# plt.plot(days_tointerp,ice_tointerp)

x = days_tointerp
y = ice_tointerp
f = interpolate.interp1d(x, y,kind='cubic' )
xnew = np.arange(1,365, 1)
ynew = f(xnew)   # use interpolation function returned by `interp1d`
plt.plot(x, y, 'o', xnew, ynew, '-')
plt.show()









plt.show()
