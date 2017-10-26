import numpy as np
import obstacles as obs
import linesolver as ls
import fig_generator as fig
# Set up computational domain
N = 100
x = np.linspace(-1,1,N)
dx = x[1]-x[0]
x,y = np.meshgrid(x,x)

# Define obstacle
G = obs.cones(x,y)

# Convexify obstacle
eps = 0.1
U = ls.quasiconvex_rotate(G,dx,eps)

# Plot solution
fig.plot3Dc(x,y,U)


