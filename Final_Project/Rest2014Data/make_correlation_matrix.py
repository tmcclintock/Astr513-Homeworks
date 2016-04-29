"""
A short script that takes Betoule's covariance matrix and computs the 
correlation matrix, and then makes a figure.
"""
import numpy as np

#Pull out the z and mus
data = np.genfromtxt("redshift_distanceMod.dat")
z,mu = data.T

#Get the covariance matrix
cov  = np.genfromtxt("covarianceMatrix.dat")

#Define the correlation matrix
corr = np.zeros_like(cov)
for i in range(len(cov)):
    for j in range(len(cov[i])):
        corr[i,j] = cov[i,j]/(np.sqrt(cov[i,i]*cov[j,j]))

#Visualize
import matplotlib.pyplot as plt
plt.rc('text',usetex=True,fontsize=28)
fig,ax = plt.subplots()
cax = ax.imshow(corr,interpolation="nearest",\
                    vmin=-1,vmax=1,cmap=plt.get_cmap("bwr"),\
                    extent=[z[0],z[-1],z[-1],z[0]])
ticks = np.linspace(-1.0,1.0,11)
cbar = fig.colorbar(cax,ticks=ticks)
plt.rc
fs = 28
ax.set_xlabel("Redshift $z$",fontsize=fs)
ax.set_ylabel("Redshift $z$",fontsize=fs)
plt.subplots_adjust(bottom=0.15)

plt.gcf().savefig("Rest_correlation.eps")
plt.show()
