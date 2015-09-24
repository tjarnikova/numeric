import matplotlib.pyplot as plt
from lab2_functions import euler,leapfrog,runge
import numpy as np
import os, fnmatch

theFuncs={'euler':euler,'leapfrog':leapfrog,'runge':runge}

if __name__=="__main__":
    Ta= 20
    To= 30
    tend = 30.0
    theLambda=-0.8
    npts=500.
    points = str(npts)
    print(points)
    funChoice='runge'

    # plt.close('all')
    #
    #find the method in the theFuncs dictionary and call it
    #
    approxTime_runge,approxTemp_runge=theFuncs[funChoice](npts,tend,To,Ta,theLambda)
    funChoice = 'euler'
    approxTime_euler,approxTemp_euler=theFuncs[funChoice](npts,tend,To,Ta,theLambda)
    funChoice = 'leapfrog'
    approxTime_leapfrog,approxTemp_leapfrog=theFuncs[funChoice](npts,tend,To,Ta,theLambda)
    fig1=plt.figure(1)
    fig1.clf()
    # Set x limits
    plt.xlim(0,30)
    plt.ylim(-20,60)
    plt.plot(approxTime_runge,approxTemp_runge, 'b', label="runge")
    plt.plot(approxTime_euler,approxTemp_euler, 'g', label = "euler")
    plt.plot(approxTime_leapfrog,approxTemp_leapfrog, 'r', label = "leapfrog")
    plt.plot()
    titl =  "Comparison of estimates by 3 approximation methods. Steps: " + points 
    plt.title(titl)
    plt.hold(True)
    exactTime=np.empty([npts,],np.float)
    exactTemp=np.empty_like(exactTime)
    for i in np.arange(0,npts):
        exactTime[i] = tend*i/npts
        exactTemp[i] = Ta + (To-Ta)*np.exp(theLambda*exactTime[i])
    plt.plot(exactTime,exactTemp,'k', label = "exact solution")

    plt.legend( loc='upper left' )

    figname = "Comparison of estimates - no pts " + points  + ".png"

    filepath = '/Users/alena/Sync/numeric/lab2/asst'
    figname = os.path.join(filepath, figname)
    plt.savefig(figname)


    #(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
     #      ncol=2, mode="expand", borderaxespad=0.)
   
    
    fig2=plt.figure(2)
    fig2.clf()
    difference_runge = approxTemp_runge-exactTemp;
    difference_euler = approxTemp_euler-exactTemp;
    difference_leapfrog = approxTemp_leapfrog - exactTemp;
    plt.xlim(0,30)
    plt.ylim(-50,50)
    plt.plot(exactTime,difference_runge, 'b', label= "difference - runge")
    plt.plot(exactTime,difference_euler, 'g', label= "difference - euler")
    plt.plot(exactTime,difference_leapfrog, 'r', label= "difference - leapfrog")
    titl = "Difference between approximations and exact solution. Steps: " + points
    plt.title(titl)
    plt.legend( loc='upper left' )
    plt.hold(True)
    figname = "Difference between approximations and soln - no pts " + points  + ".png"

    filepath = '/Users/alena/Sync/numeric/lab2/asst'
    figname = os.path.join(filepath, figname)
    plt.savefig(figname)

    plt.show()
