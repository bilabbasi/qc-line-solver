import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
def plot3D(x,y,u,showplot=True,saveplot=False,filename='figure',filetype='eps'):

	fig = plt.figure()
	ax = fig.add_subplot(111,projection='3d')
	ax.plot_surface(x,y,u,cmap = cm.coolwarm,rstride=2,cstride=2)

	ax.w_xaxis.set_pane_color((1,1,1,0))
	ax.w_yaxis.set_pane_color((1,1,1,0))
	ax.w_zaxis.set_pane_color((1,1,1,0))

	if saveplot:
		plt.savefig(filename + '.' + filetype, format=filetype, dpi=1000)
	if showplot:
		plt.show()
	return

def plot3Dc(x,y,u,showplot=True,saveplot=False,filename='figure',filetype='eps'):

	fig = plt.figure()
	ax = fig.add_subplot(111,projection='3d')
	ax.plot_surface(x,y,u,cmap = cm.coolwarm,rstride=2,cstride=2)
	ax.contour(x,y,u,8,cmap=cm.coolwarm,offset=np.min(u))

	ax.w_xaxis.set_pane_color((1,1,1,0))
	ax.w_yaxis.set_pane_color((1,1,1,0))
	ax.w_zaxis.set_pane_color((1,1,1,0))

	if saveplot:
		plt.savefig(filename + '.' + filetype, format=filetype, dpi=1000)
	if showplot:
		plt.show()
	return

def plotcontour(x,y,u,showplot=True,saveplot=False,filename='figure',filetype='eps'):

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.contour(x,y,u)

	if saveplot:
		plt.savefig(filename + '.' + filetype, format=filetype, dpi=1000)

	plt.show()
	return