"""
This script calculates the mean and standard deviations
from the chains to report in the tables.
"""

import numpy as np

name = "rest"
prior = "withprior/prior"
priorfigname = "withprior"
modelname = "wcdm"

#Get the chain
chainpath = "chains/%s/%s_stuff/%s_astr_513_chain.txt"%(modelname,name,prior)
chain = np.genfromtxt(chainpath)

mean = np.mean(chain,0)
std = np.std(chain,0)

print mean
print std

#Edit the above to print in a format suited to the paper
