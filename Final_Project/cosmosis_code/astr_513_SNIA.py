"""
This is the module that compares the supernovae data
to our model and returns a likelihood.

"""

from cosmosis.datablock import names as section_names
from cosmosis.datablock import option_section
from cosmosis.runtime.declare import declare_module
import numpy as np

cosmo = section_names.cosmological_parameters
likes = section_names.likelihoods


"""
The setup function runs only once at the start
"""
def setup(options):

    #Open the data and covariance matrix
    #Then calculate the inverse covariance matrix
    datapath = options[option_section,"datapath"]
    covpath = options[option_section,"covpath"]
    data = np.genfromtxt(datapath)
    cov = np.genfromtxt(covpath)
    icov = np.linalg.inv(cov)
    z,mu = data.T
    
    #Pass it all forward
    return (z,mu,cov,icov)

"""
This function evaluates the likelihood.
"""
def execute(block,config):
    z,mu,cov,icov = config #Passed from setup

    #Read in the cosmology
    h = block[cosmo,"h0"]
    om = block[cosmo,"omega_m"]
    ode = 1.0 - om #Omega_dark_energy

    #Create a model for mu(z)
    #TODO: decide how to implement this
    mu_model = z*0 #MODEL GOES HERE

    #Calculate the likelihood
    LL = -1.0
    #for i in range(len(cov)):
        #for j in range(len(cov[i])):
            #LL += -0.5 * (mu[i]-mu_model[i])*icov[i,j]*(mu[j]-mu_model[j])
    block[likes,"SNIA_LIKE"]=LL

    return 0 #Signal that it finished fine
    
"""
This function has to be here for design reasons.
It is only really used if the module is written in
C/C++/Fortran.
"""
def cleanup(self):
    return 0
