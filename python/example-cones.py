import numpy as np
import obstacles as obs
import linesolver as ls
import solvers as pde
import fig_generator as fig
## Example for the linesolver applied to the minimum of two cones.

# Set up computational domain
N = 64
x = np.linspace(-1,1,N)
dx = x[1]-x[0]
x,y = np.meshgrid(x,x)

# Define obstacle
G = obs.cones(x,y)

# Convexify obstacle
eps = .1
U = ls.quasiconvex_rotate(G,dx,eps) # Solution given by line solver
Upde = pde.uniformQC(G,dx,eps,max_its=500)      # Solution given by PDE

# Plot solution
fig.plot3Dc(x,y,U,showplot=False)
fig.plot3Dc(x,y,Upde)


