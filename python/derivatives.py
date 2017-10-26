import numpy as np
from numpy.linalg import norm

def D2(U,v):
    #Centered difference of v^T D^2 v. Computed only where possible.
    W = norm(v,np.inf)
    Nx,Ny = np.shape(U)
    Ix,Iy = np.ix_(np.arange(W,Nx-W,dtype=np.intp),np.arange(W,Ny-W,dtype=np.intp))
    Uf = U[Ix+v[0],Iy+v[1]]
    Ub = U[Ix-v[0],Iy-v[1]]
    Uc = U[Ix,Iy]
    return Uf + Ub - 2 * Uc
    
def absD1(U,v):
    #non-monotone finite difference of abs{grad u ^T v}
    W = norm(v,np.inf)
    Nx,Ny = np.shape(U)
    Ix,Iy = np.ix_(np.arange(W,Nx-W,dtype=np.intp),np.arange(W,Ny-W,dtype=np.intp))
    Uf = U[Ix+v[0],Iy+v[1]]
    Ub = U[Ix-v[0],Iy-v[1]]
    Uc = U[Ix,Iy]
    return np.maximum(Uf,Ub) - Uc
    
def eik(U):
    #Elliptic FD of Eikonal operator (ref. HK Zhao)
    u = np.copy(U)
    Nx,Ny = np.shape(U)
    Ix,Iy = np.ix_(np.arange(1,Nx-1,dtype=np.intp),np.arange(1,Ny-1,dtype=np.intp))
    
    Ux = u[Ix,Iy] - np.minimum(u[Ix+1,Iy],u[Ix-1,Iy])
    Ux = np.maximum(Ux,0)
    
    Uy = u[Ix,Iy] - np.minimum(u[Ix,Iy+1],u[Ix,Iy-1])
    Uy = np.maximum(Uy,0)
    
    u[Ix,Iy] = np.sqrt(Ux**2 + Uy**2) #u preserves boundary values of U
    return u
    
    