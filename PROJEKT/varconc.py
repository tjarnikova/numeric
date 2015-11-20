import numpy as np
import matplotlib.pyplot as plt
Tmax = 3.7
I_k = 100
mu_0 = .79
chi = 0.5

I= 60
T= 3

R_L = (I/I_k)*(np.sqrt(1+(I/I_k)**2)) 
R_T = np.exp(0.063*(T-Tmax))
mu = mu_0*R_L*R_T 
print(mu-chi)

plt.close("all")
fig, big_axes = plt.subplots( figsize=(12.0, 8.0) , nrows=3, ncols=1, sharey=True) 
for row, big_ax in enumerate(big_axes, start=1):
    big_ax.tick_params(labelcolor=(1.,1.,1., 0.0), top='off', bottom='off', left='off', right='off')
    # removes the white frame
    big_ax._frameon = False

timeVals = [0,1,2,3]
yvals = [0,1,2,3]
for i in range(1,2):
        
    ax = fig.add_subplot(1,1,i)
    
    theLines = ax.plot(timeVals,yvals,'b*')
# points.set_markersize(12) 
    theLines[0].set_marker('+')
    theLines[0].set_linestyle('-')

    titl =  'kitten'
    ax.hold(True)
    ax.set_title(titl, fontsize = 10)
    ax.set_xlabel("time (day)", fontsize = 8)
    ax.set_ylabel("fractional coverage")
    ax.set_xlim([0,365])
    
fig.set_facecolor('w')
plt.suptitle('Model Variables')


fig2, big_axes = plt.subplots( figsize=(12.0, 8.0) , nrows=3, ncols=1, sharey=True) 
for row, big_ax in enumerate(big_axes, start=1):
    big_ax.tick_params(labelcolor=(1.,1.,1., 0.0), top='off', bottom='off', left='off', right='off')
    # removes the white frame
    big_ax._frameon = False

timeVals = [0,1,2,3]
yvals = [7,1,2,6]
for i in range(1,2):
        
    ax = fig2.add_subplot(1,1,i)
    
    theLines = ax.plot(timeVals,yvals,'b*')
# points.set_markersize(12) 
    theLines[0].set_marker('+')
    theLines[0].set_linestyle('-')

    titl =  'kitten'
    ax.hold(True)
    ax.set_title(titl, fontsize = 10)
    ax.set_xlabel("time (day)", fontsize = 8)
    ax.set_ylabel("fractional coverage")
    ax.set_xlim([0,3])
    
fig2.set_facecolor('w')
plt.suptitle('Model Variables')



plt.show()
