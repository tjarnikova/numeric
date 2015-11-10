import numpy as np
from scipy import integrate

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation
import time

N_trajectories = 1

def lorentz_deriv(coords, t0, sigma=10., beta=8./3, rho=28.0):
    x,y,z = coords
    out = [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]
    return out

# Choose random starting points, uniformly distributed from -15 to 15
np.random.seed(1)
x0 = -15 + 30 * np.random.random((N_trajectories, 3))

# Solve for the trajectories
t = np.linspace(0, 4, 1000)
#program here

x_t = np.asarray([integrate.odeint(lorentz_deriv, x0i, t)
                  for x0i in x0])


print('kitten')
