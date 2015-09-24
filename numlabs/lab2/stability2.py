"""
  this script show how to plot the heat conduction equation

"""
import matplotlib.pyplot as plt
from numlabs.lab2.lab2_functions import euler,beuler,leapfrog
import numpy as np


theFuncs={'euler':euler,'beuler':beuler,'leapfrog':leapfrog}

if __name__=="__main__":
    tend=100.
    Ta=20.
    To=30.
    theLambda=-8.
    funChoice='euler'
    npts=400.
    deltaT = tend /npts
    print(deltaT)
    approxTime,approxTemp=theFuncs[funChoice](npts,tend,To,Ta,theLambda)
    exactTime=np.empty([npts,],float)
    exactTemp=np.empty_like(exactTime)
    for i in np.arange(0,npts):
       exactTime[i] = tend*i/npts
       exactTemp[i] = Ta + (To-Ta)*np.exp(theLambda*exactTime[i])
    plt.figure(1)
    plt.clf()
    plt.plot(exactTime,exactTemp,'b')
    plt.hold(True)
    plt.plot(approxTime,approxTemp, 'r')
    theAx=plt.gca()
    theAx.set_xlim([0,tend])
    theAx.set_ylim([-100,100])
    titl = "Stability of " + funChoice +" approximation \n Number of points: " + str(npts) + ", deltaT = " + str(deltaT)
    theAx.set_title(titl)
    plt.show()
   
