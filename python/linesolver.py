import numpy as np

""" General description

    Convex and quasiconvex envelope line solvers. The functions
    defined here compute the envelopes by applying the respective
    line solvers along lines (with slope given by the stencil) 
    partitioning the computational domain.

    The code is based on the algorithms discussed in the following:

                    https://arxiv.org/abs/1612.05584

    Parameters
    ----------
    U : array_like
        The initial condition.
        boundary.
    solution_tol : scalar
        Stopping criterion, in the infinity norm.
    max_iters : scalar
        Maximum number of iterations.

    Returns
    -------
    {U_ce,_U_qce} : array_like
        Convex and quasiconvex envelope, respectively.
    i : scalar
        Number of iterations taken.
"""

# Default stencil to use (canonical basis vectors)
stencil = np.array([[0,1],
                    [1,0],
                    [1,1]])

def convex_linesolver1D(U):
    #Computes the convex envelope along a 1D line.
    ind = 0
    U_ce = np.copy(U)
    N = np.shape(U)[0] #Number of grid points
    x = np.arange(N) # Index
    while ind < len(U)-1:
        slope = (U_ce[ind+1:] - U_ce[ind])/(x[ind+1:]-x[ind]) #Calculate slopes from reference point
        m = np.min(slope) #Retrieve the smallest one
        i = np.argmin(slope)+ind+1 #Update location of reference point
        U_ce[ind:i] = m*(x[ind:i]-x[ind]) + U_ce[ind] #Create line from (old) reference point and where smallest slope occurs
        ind = i
    return U_ce
    
def convex_linesolver_line(Nx,Ny,U,v,i=0,j=0):
    #Computes the convex envelope of U along the line v, starting at the index (i,j)
    U_ce = np.copy(U)
    #If either increment in (v0,v1) is 0, have to manually define index vector
    if v[0] == 0:
        ind_x = np.ones(Nx) * i
        ind_y = np.arange(j,Ny,v[1],dtype=np.intp)
    elif v[1]==0:
        ind_x = np.arange(i,Nx,v[0],dtype=np.intp)
        ind_y = np.ones(Ny) * j
    else:
        ind_x = np.arange(i,Nx,v[0],dtype=np.intp)
        ind_y = np.arange(j,Ny,v[1],dtype=np.intp)
    
    #Make sure you only go as far as you can in BOTH indices
    max_ind = np.min([len(ind_x),len(ind_y)])
    ind_x = ind_x[:max_ind].astype(np.intp)
    ind_y = ind_y[:max_ind].astype(np.intp)
    
    #Now apply the line solver
    u_v = U_ce[ind_x,ind_y]           #Retrieve obstacle along line
    u_v_CE = convex_linesolver1D(u_v) #Apply 1D solver to line
    U_ce[ind_x,ind_y] = u_v_CE        #Insert 1D solution back in

    return U_ce

def convex_linesolver(U,stencil=stencil,sweep_bdry='yes'):
    #Computes the convex envelope by iterating the 1D linesolver along the lines with direction v.
    #Solution propagates from the left and bottom boundaries.
    #Note that the CE line solver is applied along the boundaries as well. This means
    #that the boundary values of the PDE and line solver disagree. The best results are 
    #achieved when the line solver, along the canonical directions, is not applied on the boundary.
    U_ce = np.copy(U)
    if len(np.shape(U)) == 1:
        #If array is one dimensional, apply 1D solver directly.
        U_ce = convex_linesolver1D(U)
    else:
        #Else iterate line solver from the boundary.
        Nx,Ny = np.shape(U)
        for v in stencil:
            if v[0] == 0 and v[1] == 1 and sweep_bdry == 'no':
                y_ind = np.arange(1,Ny-1)
            else:
                y_ind = np.arange(0,Ny)
            if v[0] == 1 and v[1] == 0 and sweep_bdry == 'no':
                x_ind = np.arange(1,Nx-1)
            else:
                x_ind = np.arange(0,Nx)

            for i in x_ind:
                U_ce = convex_linesolver_line(Nx,Ny,U_ce,v,i,0)
            for i in y_ind:
                U_ce = convex_linesolver_line(Nx,Ny,U_ce,v,0,i)
    return U_ce

def quasiconvex_march(U,dx,eps,v=np.array([1,0]),sweep_bdry='yes'):
    """
        Compute the quasiconvex envelopes of U along the lines with slope 
        given by the stencil. This is a sweeping algorithm that does all lines,
        with a given slope, at the same time. It is written for direction vectors
        lying in the positive quadrant. Applying it along vectors in the 2nd quadrant
        is done by simply rotating U and then applying the algorithm (refer to 
        quasiconvex_rotate)
    """
    U_qce = np.copy(U)
    Nx,Ny = np.shape(U)
    
    Uf = np.copy(U_qce) #Forward sweep
    Ub = np.rot90(np.copy(U_qce),2) #Backward sweep, rotate to simplify sweeping in oppositie direction

    #Need to increment along non-zero element in sweep direction
    if v[0] != 0:
        if v[1] == 0 and sweep_bdry == 'no':
            m = 1
            M = Ny - 1
        else:
            m = v[1]
            M = Ny
        Iy = np.arange(m,M,dtype=np.intp)
        for Ix in np.arange(v[0],Nx,dtype=np.intp):
            Uf[Ix,Iy] = np.minimum(Uf[Ix,Iy],
                                    Uf[Ix-v[0],Iy-v[1]]-eps*dx)
            Ub[Ix,Iy] = np.minimum(Ub[Ix,Iy],
                                    Ub[Ix-v[0],Iy-v[1]]-eps*dx)

    elif v[1] != 0:
        if v[0] == 0 and sweep_bdry == 'no':
            m = 1
            M = Nx - 1
        else:
            m = v[0]
            M = Nx
        Ix = np.arange(m,M,dtype=np.intp)
        for Iy in np.arange(v[1],Ny,dtype=np.intp):
            Uf[Ix,Iy] = np.minimum(Uf[Ix,Iy],
                                    Uf[Ix-v[0],Iy-v[1]]-eps*dx)
            Ub[Ix,Iy] = np.minimum(Ub[Ix,Iy],
                                    Ub[Ix-v[0],Iy-v[1]]-eps*dx)
    Ub = np.rot90(Ub,-2) #Rotate back
    U_qce = np.maximum(Uf,Ub) #Take maximum to get QC envelope along lines
    return U_qce

def quasiconvex_rotate(U,dx,eps,stencil=stencil,sweep_bdry='yes'):
    Ur = np.copy(U)
    for v in stencil:
        Ur = quasiconvex_march(Ur,dx,eps,v = v,sweep_bdry=sweep_bdry)
        Ur = np.rot90(Ur,1)
        Ur = quasiconvex_march(Ur,dx,eps,v = v,sweep_bdry=sweep_bdry)
        Ur = np.rot90(Ur,-1)
    return Ur

