"""
This script takes in the chain and creates corner plots.
"""
import numpy as np
import matplotlib.pyplot as plt
import corner
plt.rc('text',usetex=True,fontsize=16)

priors = False
makecorner = True

path = "prior_astr_513_chain.txt"

data = np.genfromtxt(path)
print data.shape

chain = data[:,:2]
likes = data[:,2]
print chain.shape

if makecorner:
    fontsize = 28
    pad = 100
    fig = corner.corner(chain,labels=[r"$\Omega_{\rm M}$",r"$h$"],\
                            quantiles=[0.16, 0.84],\
                            levels=[1-np.exp(-0.5),1-np.exp(-(2.**2)/2.)],\
                            plot_datapoints=False)
    fig.get_axes()[2].set_ylabel(r"$h$",fontsize=fontsize)
    fig.get_axes()[2].set_xlabel(r"$\Omega_{\rm M}$",fontsize=fontsize)
    fig.get_axes()[3].set_xlabel(r"$h$",fontsize=fontsize)

    plt.gcf().savefig("betoule_lcdm_withprior_corner.eps")
    #plt.show()
