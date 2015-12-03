import INTFUN
from importlib import reload
from INTFUN import Integrator
reload(INTFUN)
from runmodel_withfeedback import Integ591
from runmodel import Integ59
from collections import namedtuple
from interp_met import met_get, temp_load, ice_load, wind_load
import numpy as np
#%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import glob, os
# import math
# from importlib import reload
# reload(INTFUN)
# from collections import namedtuple
# import numpy as np
# #matplotlib inline
# import matplotlib.pyplot as plt
import pandas as pd
import datetime

met = met_get()
theSolver = Integ59('test.yaml',met)
timeVals,yVals,errorList,metList=theSolver.timeloop5fixed(met)
yvals=pd.DataFrame.from_records(yVals,columns=['primprod','sea DMS','ice DMS','air DMS','air_dms_icecont','CCN', 'CCN_icecont', 'forcing', 'forcing_icecont'])

theSolver_feedback = Integ591('test.yaml',met)
timeVals,yVals,errorList,metList=theSolver_feedback.timeloop5fixed(met)
yvals_fb=pd.DataFrame.from_records(yVals,columns=['primprod','sea DMS','ice DMS','air DMS','air_dms_icecont','CCN', 'CCN_icecont', 'forcing', 'forcing_icecont'])




plt.close("all")

fig, big_axes = plt.subplots( figsize=(10.0, 10.0) , nrows=3, ncols=1, sharey=True) 
for row, big_ax in enumerate(big_axes, start=1):
    big_ax.tick_params(labelcolor=(1.,1.,1., 0.0), top='off', bottom='off', left='off', right='off')
    # removes the white frame
    big_ax._frameon = False

str_list = ['primprod','sea DMS','ice DMS','air DMS','air_dms_icecont','CCN', 'CCN_icecont', 'forcing', 'forcing_icecont']
var_list = ['primprod','sea DMS','ice DMS','air DMS','air_dms_icecont','CCN', 'CCN_icecont', 'forcing', 'forcing_icecont']
key_list = ['primprod','sea DMS','ice DMS','air DMS','air_dms_icecont','CCN', 'CCN_icecont', 'forcing', 'forcing_icecont']

for i in range(1,10):
    
    ax = fig.add_subplot(3,3,i)

    theLines = ax.plot(timeVals,yvals[var_list[i-1]],'b*',yvals_fb[var_list[i-1]],'r*',label=key_list[i-1])
    # theLines[0].set_marker('+')
    # theLines[0].set_linestyle('-')
    #theLines[1] = ax.plot(timeVals,yvals_fb[var_list[i-1]],'r*',label=key_list[i-1])
    # theLines[1].set_marker('+')
    # theLines[1].set_linestyle('-')

    titl =  str_list[i-1]  
    ax.hold(True)
    ax.set_title(titl, fontsize = 10)
    ax.set_xlabel("time (day)", fontsize = 8)

    ax.set_xlim([0,350])

fig.tight_layout()
fig.set_facecolor('w')
plt.suptitle('Model Variables', fontsize=16, fontweight='bold')
w = datetime.datetime.now()
w.isoformat()
day = str(w)
filename = 'Model_output' + day + '.png'
fig.savefig(filename)
# print(yvals['DMS flux'])

days = np.arange(1,366,1)
ice = np.array(metList.get('ice'))
wind = np.array(metList.get('wind'))
sst = np.array(metList.get('sst'))
par = np.array(metList.get('par'))
ccsen = np.array(metList.get('ccsen'))
cloud = np.array(metList.get('cloud'))

fig2, big_axes = plt.subplots( figsize=(10.0, 10.0) , nrows=3, ncols=1, sharey=True) 
for row, big_ax in enumerate(big_axes, start=1):
    big_ax.tick_params(labelcolor=(1.,1.,1., 0.0), top='off', bottom='off', left='off', right='off')
    # removes the white frame
    big_ax._frameon = False

met_list = [ice,wind,sst,par,ccsen,cloud]
tit_list = ['Ice Cover','Windspeed','Sea Surface Temperature','Light Intensity','CCN sensitivity to DMS flux', 'Cloud Cover']
ylabel_list = []
for i in range(1,7):
    
    ax = fig2.add_subplot(3,2,i)

    theLines = ax.plot(days,met_list[i-1],'b*')
# points.set_markersize(12) 
    theLines[0].set_marker('+')
    theLines[0].set_linestyle('-')

    titl =  'Climatology of ' + tit_list[i-1]
    ax.hold(True)
    ax.set_title(titl, fontsize = 12)
    ax.set_xlabel("time (day)", fontsize = 8)

    ax.set_xlim([0,365])

    if (i ==1):
        ax.set_ylabel("fractional coverage")
    if (i ==2):
        ax.set_ylabel("m/s")
    if (i ==3):
        ax.set_ylabel("degrees Celsius")
    if (i ==4):
        ax.set_ylabel("W /m^2")
fig2.set_facecolor('w')
fig2.tight_layout()
#plt.suptitle('Meteorological Forcing', fontsize=12, fontweight='bold')
w = datetime.datetime.now()
w.isoformat()
# print(w)
# day = str(w)
filename = 'met_force' + day + '.png'
fig2.savefig(filename)
plt.show()