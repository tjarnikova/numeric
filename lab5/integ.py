# integrate constant growth rates with fixed timesteps
#
#matplotlib inline
import numlabs.lab5.lab5_funs
from importlib import reload
reload(numlabs.lab5.lab5_funs)
from numlabs.lab5.lab5_funs import Integrator
from collections import namedtuple
import numpy as np
import matplotlib.pyplot as plt

class Integ51(Integrator):

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
            [self.initvars.whiteconc, self.initvars.blackconc])
        print("whiteconc")
        print(self.initvars.whiteconc)
        print("blackconc")
        print(self.initvars.blackconc)
        self.nvars = len(self.yinit)
        return None
    #
    # Construct an Integ51 class by inheriting first intializing
    # the parent Integrator class (called super).  Then do the extra
    # initialization in the set_yint function
    #
    def __init__(self, coeffFileName):
        super().__init__(coeffFileName)
        self.set_yinit()

    def derivs5_adapt(self, y, t):
        """y[0]=fraction white daisies
           y[1]=fraction black daisies
           
           Constant growty rates for white
           and black daisies beta_w and beta_b
           
           returns dy/dt
        """
        user = self.uservars
        #
        # bare ground
        #
        x = 1.0 - y[0] - y[1]

        # growth rates don't depend on temperature
        beta_b = 0.2  # growth rate for black daisies
        beta_w = 0.2  # growth rate for white daisies

        # create a 1 x 2 element vector to hold the derivitive
        f = np.empty([self.nvars], 'float')
        f[0] = y[0] * (beta_w * x - user.chi)
        f[1] = y[1] * (beta_b * x - user.chi)
 
        return f
    
    

theSolver = Integ51('fixed_growth.yaml')
timeVals, yVals, errorList = theSolver.timeloop5fixed()

file_list = ['fixed_growth.yaml','fixed_growth2.yaml','fixed_growth3.yaml','fixed_growth4.yaml']
#print(file_list[0])


fig, big_axes = plt.subplots( figsize=(12.0, 12.0) , nrows=3, ncols=1, sharey=True) 
for row, big_ax in enumerate(big_axes, start=1):
    big_ax.tick_params(labelcolor=(1.,1.,1., 0.0), top='off', bottom='off', left='off', right='off')
    # removes the white frame
    big_ax._frameon = False
    
for i in range(1,5):
        
    ax = fig.add_subplot(2,2,i)
  

    theSolver = Integ51(file_list[0])
    timeVals, yVals, errorList = theSolver.timeloop5fixed()

    theLines = ax.plot(timeVals, yVals)  
    theLines[0].set_marker('+')
    theLines[0].set_linestyle('-')
    theLines[1].set_color('k')
    theLines[1].set_marker('*')
    
    
    ax.legend(theLines, ('white daisies', 'black daisies'), loc='best')
    titl = "Error in solution by \nforward Euler Method"

    
    ax.hold(True)
    ax.set_title(titl, fontsize = 10)

fig.set_facecolor('w')
plt.show()
