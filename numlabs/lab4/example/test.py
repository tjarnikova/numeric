import numpy as np 
import matplotlib.pyplot as plt

F = np.array([0,10,15,20,25,30,35,30,25,20,15,10,0])
print(max(F))
delta_F = np.zeros(len(F))
albedo = .5
cc = .5
ccn_change = 1
for i in range (0, len(F)):
  delta_F[i] = (-1/3)*F[i]*cc*albedo*(1-albedo)*ccn_change

months = np.arange(1,14,1)
print(len(months))
print(len(delta_F))
plt.plot(months,delta_F)
plt.show()


R_T = np.exp(0.063*(1-3))
print(R_T)