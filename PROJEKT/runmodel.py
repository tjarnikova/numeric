import INTFUN
from importlib import reload
from INTFUN import Integrator
reload(INTFUN)
from collections import namedtuple
import numpy as np
#%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd


from importlib import reload
reload(INTFUN)
from collections import namedtuple
import numpy as np
#matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd



class Integ59(Integrator):

    def set_yinit(self):
        #
        # read in 'albedo_white chi S0 L albedo_black R albedo_ground'
        #
        uservars = namedtuple('uservars', self.config['uservars'].keys())
        self.uservars = uservars(**self.config['uservars'])
        #
        # read in 'whiteconc blackconc'
        #
        initvars = namedtuple('initvars', self.config['initvars'].keys())
        self.initvars = initvars(**self.config['initvars'])
        self.yinit = np.array(
            [self.initvars.seaDMS,
             self.initvars.airDMS,
             self.initvars.CCN,
             self.initvars.COD,
             self.initvars.albedo,
             # self.initvars.PAR,
             self.initvars.primprod])       
        self.nvars = len(self.yinit)
        return None

    def __init__(self, coeff_file_name):
        super().__init__(coeff_file_name)
        self.set_yinit()


    def derivs5(self, y, t,met):

        user = self.uservars
        ice = met.get('ice')
        wind = met.get('wind')
        sst = met.get('sst')
        par = met.get('par')
        f = np.empty_like(y)

        #equations for primary prod    
        Tmax = 3.7
        I_k = 112
        mu_0 = .79
        chi = 0.525

        R_L = (par/I_k)*(np.sqrt(1+((par*(1-y[4])/I_k)**2)))
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

        print('kw')
        print(k_w)    
        #sea DMS
        f[0] = (y[0]*(mu-chi)*.4)*(1-ice)
        print(y[0])
        DMS = y[0]+f[0]
        DMSFLUX = k_w*DMS*(1-ice)
        f[1] = DMSFLUX-y[1]
        print(DMSFLUX)
        print(f[1])
        #CCN
        f[2] = 0
        #COD
        f[3] = 0 
        #albedo
        f[4] = 0
        # #PAR
        # f[5] = y[5] 
        #primprod
        # if (t< 60):
        #     f[6] = 0
        # if (t>= 60):
        f[5] = (y[5]*(mu-chi)*.7)*(1-ice)

        #f[6] = y[6]

        
        return f
    

theSolver = Integ59('test.yaml')
timeVals,yVals,errorList,metList=theSolver.timeloop5fixed()
yvals=pd.DataFrame.from_records(yVals,columns=['DMS','DMS flux','CCN','COD','albedo','primary productivity'])

plt.close("all")

fig, big_axes = plt.subplots( figsize=(12.0, 4.0) , nrows=3, ncols=1, sharey=True) 
for row, big_ax in enumerate(big_axes, start=1):
    big_ax.tick_params(labelcolor=(1.,1.,1., 0.0), top='off', bottom='off', left='off', right='off')
    # removes the white frame
    big_ax._frameon = False

yvals=pd.DataFrame.from_records(yVals,columns=['DMS','DMS flux','CCN','COD','albedo','primary productivity'])
str_list = str_list  = ['Fig 1: Sea DMS ','Fig 2: DMS flux','Fig 3: CCN','Fig 4: COD','Fig 5: Albedo','Fig 6: Primary Productivity',]
var_list = ['DMS','DMS flux','CCN','COD','albedo','primary productivity']
key_list = ['DMS','DMS flux','CCN','COD','albedo','primary productivity']

for i in range(1,4):
        
    ax = fig.add_subplot(1,3,i)
    
    if (i==1):
        theLines = ax.plot(timeVals,yvals[var_list[5]],'b*',label='primary productivity')
        titl = 'Primary Productivity'
        ax.set_ylim([0,10])
        ax.set_ylabel("mg/$m^3$")
        ax
    if (i==2):
        theLines = ax.plot(timeVals,yvals[var_list[0]],'b*',label=key_list[1])
        titl = 'DMS concentration'
        ax.set_ylim([0,20])
        ax.set_ylabel("nM")

    if (i==3):
        theLines = ax.plot(timeVals,yvals[var_list[1]],'b*',label=key_list[5])
        titl = 'DMS flux'
        ax.set_ylim([0,40])
        ax.set_ylabel("$\mu$mol / $m^2$/day")

# points.set_markersize(12) 
    theLines[0].set_marker('+')
    theLines[0].set_linestyle('-')

    # titl =  str_list[i-1]  
    ax.hold(True)
    ax.set_title(titl, fontsize = 10)
    ax.set_xlabel("time (day)", fontsize = 8)
    
    ax.set_xlim([0,350])

    
fig.set_facecolor('w')
plt.suptitle('Model Variables', fontsize=16, fontweight='bold')

print(yvals['DMS flux'])

days = np.arange(1,365,1)
ice = np.array(metList.get('ice'))
wind = np.array(metList.get('wind'))
sst = np.array(metList.get('sst'))
par = np.array(metList.get('par'))



fig2, big_axes = plt.subplots( figsize=(12.0, 8.0) , nrows=3, ncols=1, sharey=True) 
for row, big_ax in enumerate(big_axes, start=1):
    big_ax.tick_params(labelcolor=(1.,1.,1., 0.0), top='off', bottom='off', left='off', right='off')
    # removes the white frame
    big_ax._frameon = False

met_list = [ice,wind,sst,par]
tit_list = ['ice','wind','sst','PAR']
ylabel_list = []
for i in range(1,5):
        
    ax = fig2.add_subplot(2,2,i)
    
    theLines = ax.plot(days,met_list[i-1],'b*')
# points.set_markersize(12) 
    theLines[0].set_marker('+')
    theLines[0].set_linestyle('-')

    titl =  'Climatology of ' + tit_list[i-1]
    ax.hold(True)
    ax.set_title(titl, fontsize = 10)
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