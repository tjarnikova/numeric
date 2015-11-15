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
             self.initvars.PAR,
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
        I_k = 100
        mu_0 = .79
        chi = 0.525

        R_L = (par/I_k)*(np.sqrt(1+((par*(1-y[4])/I_k)**2)))
        R_T = np.exp(0.063*(sst-Tmax))
        mu = mu_0*R_L*R_T 

        #


        #sea DMS
        f[0] = (y[6]*(mu-chi)*.5)*(1-ice)
        #air DMS
        f[1] = y[5]*k_w
        #CCN
        f[2] = y[2]
        #COD
        f[3] = y[3] 
        #albedo
        f[4] = 0
        #PAR
        f[5] = y[5] 
        #primprod
        # if (t< 60):
        #     f[6] = 0
        # if (t>= 60):
        f[6] = (y[6]*(mu-chi)*.25)*(1-ice)

        #f[6] = y[6]

        
        return f
    

theSolver = Integ59('test.yaml')
timeVals,yVals,errorList,metList=theSolver.timeloop5fixed()
# print(metList[120])
print(type(metList))

ice = np.array(metList.get('ice'))
wind = np.array(metList.get('par'))
print(wind)
yvals=pd.DataFrame.from_records(yVals,columns=['white','black','rabbit','fox','kitten','kitten2','kitten3'])

plt.close("all")
thefig,theAx=plt.subplots(1,1)

points,=theAx.plot(timeVals,yvals['white'],'-b',label='white daisies')
points.set_markersize(12)
#theLine1,=theAx.plot(timeVals,yvals['black'],'--ko',label='black daisies')
# theLine2,=theAx.plot(timeVals,yvals['rabbit'],'--ro',label='rabbits')
# theLine2,=theAx.plot(timeVals,yvals['fox'],'--go',label='foxes')
theAx.set_title('Monthly-Resolution Ice Cover')
theAx.set_xlabel('time')
theAx.set_ylim([0,10])
theAx.set_xlim([0,365])
theAx.set_ylabel('fractional coverage')
out=theAx.legend(loc='best')
plt.show()