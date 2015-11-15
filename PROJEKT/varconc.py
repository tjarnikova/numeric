import numpy as np


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