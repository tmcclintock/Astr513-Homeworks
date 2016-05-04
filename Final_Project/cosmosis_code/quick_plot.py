import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

#MODEL:
om = 0.3
h = 0.69
w = -1.
ode = 1. - om

def E_z(z,om,ode,w,ok=0):
    return np.sqrt(om*(1.0+z)**3.0+ok*(1.0+z)**2.0+ode*(1.0+z)**(3.0*(w+1.0)))

betoule = False
rest = True

if betoule:
    datapath = "../Betoule2014Data/tablef1.dat"
    covpath = "../Betoule2014Data/tablef2.dat"
elif rest:
    datapath = "../Rest2014Data/redshift_distanceMod.dat"
    covpath = "../Rest2014Data/covarianceMatrix.dat"

data = np.genfromtxt(datapath)
cov = np.genfromtxt(covpath)
errs = np.sqrt(np.diag(cov)) #errorbars
icov = np.linalg.inv(cov)
z,mu = data.T
inds = np.argsort(z)
z = z[inds]
mu = mu[inds]

#Create a model for mu(z)
dc = np.ones_like(z)
for i in range(len(z)):
    dc[i] = 3000.0/h * integrate.quad(E_z,0,z[i],args=(om,ode,w))[0]
dl = (1+z)*dc
mu_model = 5*np.log10(dl)+25
    
plt.errorbar(z,mu,yerr=errs,ls='',marker='.',alpha=0.5)
plt.plot(z,mu_model)
#plt.xscale('log')
#plt.yscale('log')
plt.show()
