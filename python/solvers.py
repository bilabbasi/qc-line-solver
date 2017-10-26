import numpy as np
import derivatives as der
from numpy.linalg import norm
# Default stencil to use (canonical basis vectors)
stencil = np.array([[0,1],
                    [1,0],
                    [1,1],
                    [-1,1]])
def CFL(dx):
	return dx**2/2

def uniformQC(G,dx,eps=0.1,stencil=stencil,tol=1e-4,max_its=1e4):

	U = np.copy(G)     	# Initial condition is obstacle G
	Nx,Ny = np.shape(U)
	err = 1
	its = 0
	while err > tol and its < max_its:

		Uold = np.copy(U)
		F = np.ones((len(stencil),Nx,Ny)) * np.inf

		for k in range(len(stencil)):
			v = stencil[k,:] 				  # direction vector 
			w = norm(v,np.inf).astype(np.int) # width of direction
			F[k,w:-w,w:-w] = der.D2(U,v)/(norm(v*dx)**2) + 1/eps * der.absD1(U,v)/norm(v*dx)

		F = np.amin(F,axis=0)
		U[1:-1,1:-1] += CFL(dx)*np.minimum(F[1:-1,1:-1]-eps,G[1:-1,1:-1]-U[1:-1,1:-1])
		err = np.max(np.abs(Uold-U))
		its+=1
	return U