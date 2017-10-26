import numpy as np
# import context

def cones(x,y,vshift = 0,rot = 0,peaks = np.array([[-0.5,0],[0.5,0]])):
	"""
	Generates a function whose cones reside at the given peaks.
	Works best on the domain [-1,1]^2. 

	Parameters
    ----------
    x,y : array_like
        Computational domain.
    vshift : scalar
        Vertical shift of one cone.
    rot: scalar
        Rotation of peaks of cones.
    peaks : array_like
        Locations of peaks.

    Returns
    -------
    F : array_like
        The surface.
    """
	rot_mat = np.array([[np.cos(rot), np.sin(rot)],
						[-np.sin(rot), np.cos(rot)]]) #rotation matrix
	a = rot_mat.dot(peaks[0])
	b = rot_mat.dot(peaks[1])
	F = np.minimum(np.sqrt((x+a[0])**2+(y+a[1])**2),
               np.sqrt((x+b[0])**2+(y+b[1])**2)+vshift)
	return F


