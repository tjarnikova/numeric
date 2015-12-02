import INTFUN
from importlib import reload
from INTFUN import Integrator
reload(INTFUN)
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



class Integ59(Integrator):

    def set_yinit(self):

        initvars = namedtuple('initvars', self.config['initvars'].keys())
        self.initvars = initvars(**self.config['initvars'])
        self.yinit = np.array(
            [self.initvars.primprod,
             self.initvars.seaDMS,
             self.initvars.iceDMS,
             self.initvars.airDMS,
             self.initvars.airDMS_icecont,
             self.initvars.CCN,
             self.initvars.CCN_icecont,
             self.initvars.forcing,
             self.initvars.forcing_icecont])
      
        self.nvars = len(self.yinit)
        return None

    def __init__(self, coeff_file_name,met):
        super().__init__(coeff_file_name,met)
        self.set_yinit()


    def derivs5(self, y, t,met):

        # user = self.uservars
        ice = met.get('ice')
        wind = met.get('wind')
        sst = met.get('sst')
        par = met.get('par')
        icemelt = met.get('icemelt')
        ccsen = met.get('ccsen')
        # print('icemelt')
        # print(icemelt)
        parmax = 36.954097122
        f = np.empty_like(y)

        #equations for primary prod    
        Tmax = 0.201127738931
        sst = sst 
        mu_0 = .79
        chi = .4
        albedo = .5
        cc = .5

        R_L = ((par)/parmax)*(np.sqrt(1+((par*(1)/parmax)**2)))
        R_T = np.exp(0.063*(sst-Tmax))
        mu = mu_0*R_L*R_T 

        #equations for flux
        Sc = 2674.0 - 147.12*(sst) + 3.726*((sst)**2) - 0.038*((sst)**3)
        alpha = (600/Sc)**(2/3)
        beta = (600/Sc)**(1/2)



        if (wind <= 3.6):
            k_w = alpha * 0.17 * wind
        elif (wind <= 13):
            k_w = beta * (2.85*wind - 10.3) + 0.61 * alpha
        elif (wind > 13):
            k_w = beta * (5.9*wind - 49.9) + 0.61 * alpha

        #primprod    
        f[0] = (y[0]*(mu-chi))*(1-ice)
        #seaDMS
        f[1] = (y[1]*(mu-chi))*(1-ice)
        DMS = y[1]+f[1]
        # print('DMS')
        # print(DMS)
        #iceDMS
        iceDMS = icemelt * 100
        # print('iceDMS')
        print(iceDMS)
        f[2] = iceDMS - y[2]
        #airDMS

        #DMS_copy = DMS
        DMSFLUX = k_w*DMS
        f[3] = DMSFLUX-y[3]
        totDMS = DMS+iceDMS
        #print(totDMS)
        #airDMS_icecont
        DMSFLUX_icecont = k_w*(totDMS)
        f[4] =  DMSFLUX_icecont - y[4]
        #CCN
        perc_change = 0.02*((DMSFLUX-y[3])/y[3])
        CCN = (1+perc_change)*y[5]

        f[5] = CCN - y[5]
        delt_N = f[5]/CCN
        #CCN icecont
        perc_change = 0.02*((DMSFLUX_icecont-y[4])/y[4])
        CCN_icecont = (1+perc_change)*y[6]
        f[6] = CCN_icecont - y[6]
        delt_N_ice = f[6]/CCN_icecont
        #forcing
        f[7] = (-1/3)*par*cc*albedo*(1-albedo)*delt_N
        #forcing_icecont
        f[8] = (-1/3)*par*cc*albedo*(1-albedo)*delt_N_ice
        
        return f  
    
temp_file = 'met_var/air.mon.ltm.nc'
wind_file = 'met_var/wspd.sig995.mon.ltm.nc'
ice_file = 'ice/icec.day.mean.2014.v2.nc'

met = met_get(temp_file,ice_file,wind_file)
theSolver = Integ59('test.yaml',met)
timeVals,yVals,errorList,metList=theSolver.timeloop5fixed(met)
yvals=pd.DataFrame.from_records(yVals,columns=['primprod','sea DMS','ice DMS','air DMS','air_dms_icecont','CCN', 'CCN_icecont', 'forcing', 'forcing_icecont'])

plt.close("all")

fig, big_axes = plt.subplots( figsize=(12.0, 4.0) , nrows=3, ncols=1, sharey=True) 
for row, big_ax in enumerate(big_axes, start=1):
    big_ax.tick_params(labelcolor=(1.,1.,1., 0.0), top='off', bottom='off', left='off', right='off')
    # removes the white frame
    big_ax._frameon = False

yvals=pd.DataFrame.from_records(yVals,columns=['primprod','sea DMS','ice DMS','air DMS','air_dms_icecont','CCN', 'CCN_icecont', 'forcing', 'forcing_icecont'])

str_list = ['primprod','sea DMS','ice DMS','air DMS','air_dms_icecont','CCN', 'CCN_icecont', 'forcing', 'forcing_icecont']
var_list = ['primprod','sea DMS','ice DMS','air DMS','air_dms_icecont','CCN', 'CCN_icecont', 'forcing', 'forcing_icecont']
key_list = ['primprod','sea DMS','ice DMS','air DMS','air_dms_icecont','CCN', 'CCN_icecont', 'forcing', 'forcing_icecont']

for i in range(1,10):
    
    ax = fig.add_subplot(3,3,i)

    theLines = ax.plot(timeVals,yvals[var_list[i-1]],'b*',label=key_list[i-1])
    theLines[0].set_marker('+')
    theLines[0].set_linestyle('-')

    titl =  str_list[i-1]  
    ax.hold(True)
    ax.set_title(titl, fontsize = 10)
    ax.set_xlabel("time (day)", fontsize = 8)

    ax.set_xlim([0,350])


fig.set_facecolor('w')
plt.suptitle('Model Variables', fontsize=16, fontweight='bold')

# print(yvals['DMS flux'])

days = np.arange(1,366,1)
ice = np.array(metList.get('ice'))
wind = np.array(metList.get('wind'))
sst = np.array(metList.get('sst'))
par = np.array(metList.get('par'))
print('days')
print(len(days))
print('ice')
print(len(ice))


fig2, big_axes = plt.subplots( figsize=(12.0, 8.0) , nrows=3, ncols=1, sharey=True) 
for row, big_ax in enumerate(big_axes, start=1):
    big_ax.tick_params(labelcolor=(1.,1.,1., 0.0), top='off', bottom='off', left='off', right='off')
    # removes the white frame
    big_ax._frameon = False

met_list = [ice,wind,sst,par,par,par]
tit_list = ['Ice Cover','Windspeed','Sea Surface Temperature','Light Intensity','Light Intensity', 'Light Intensity']
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
plt.suptitle('Meteorological Forcing', fontsize=16, fontweight='bold')

plt.show()