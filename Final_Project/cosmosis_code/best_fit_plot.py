"""
This script takes in a chain and plots the most likely model.

NOTE: My laptop (Tom) won't write things correctly when I force it to
use latex. Uncomment the line plt.rc... and rerun to make the figures please.

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
plt.rc('text',usetex=True,fontsize=24)

def E_z(z,om,ode,w,ok=0):
    return 1./np.sqrt(om*(1.0+z)**3.0+ok*(1.0+z)**2.0+ode*(1.0+z)**(3.0*(w+1.0)))

betoule = True
rest = False
prior = "withprior/prior"
priorfigname = "withprior"
modelname = "wcdm"

if betoule:
    datapath = "../Betoule2014Data/tablef1.dat"
    covpath = "../Betoule2014Data/tablef2.dat"
    name = "betoule"
elif rest:
    datapath = "../Rest2014Data/redshift_distanceMod.dat"
    covpath = "../Rest2014Data/covarianceMatrix.dat"
    name = "rest"

figname = "%s_%s_%s_bestfit.eps"%(name,modelname,priorfigname)

#Get the model
chainpath = "chains/%s/%s_stuff/%s_astr_513_chain.txt"%(modelname,name,prior)
chain = np.genfromtxt(chainpath)
om,h,w,maxlike = chain[np.argmax(chain[:,-1])]
ode = 1.0 - om

data = np.genfromtxt(datapath)
cov = np.genfromtxt(covpath)
errs = np.sqrt(np.diag(cov)) #errorbars
icov = np.linalg.inv(cov)
if rest:
    icov = np.genfromtxt(covpath) #rest matrix is mislabeled
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
    
fs = 30
plt.errorbar(z,mu,yerr=errs,ls='',marker='.',alpha=0.5)
plt.plot(z,mu_model,c='k')
plt.xlabel(r"$z$",fontsize=fs)
plt.ylabel(r"$\mu(z)$",fontsize=fs)
plt.gcf().savefig(figname)
plt.subplots_adjust(bottom=0.15)
plt.show()
