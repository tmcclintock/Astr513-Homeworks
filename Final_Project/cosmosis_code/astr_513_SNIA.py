"""
This is the module that compares the supernovae data
to our model and returns a likelihood.

"""

from cosmosis.datablock import names as section_names
from cosmosis.datablock import option_section
from cosmosis.runtime.declare import declare_module
import numpy as np
from scipy import integrate

cosmo = section_names.cosmological_parameters
likes = section_names.likelihoods

"""
adot/a \propto E_z
"""
def E_z(z,om,ode,w,ok=0):
    return np.sqrt(om*(1.0+z)**3+ok*(1.0+z)**2+ode*(1.0+z)**(3.0*(w+1)))
def E_z_inv(z,om,ode,w,ok=0):
    return 1./E_z(z,om,ode,w,ok)
def dc(h,z,om,ode,w,ok=0):
    return 3000.0/h * integrate.quad(E_z_inv,0,z,args=(om,ode,w,ok))[0]
dc = np.vectorize(dc)

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
    w = block[cosmo,"w"] #DE equation of state
    ode = 1.0 - om #Omega_dark_energy

    #Create a model for mu(z)
    #dc = np.ones_like(z)
    #for i in range(len(z)):
        ## This looks wrong to me -- ELW
        #dc[i] = 3000.0/h * integrate.quad(E_z,0,z[i],args=(om,ode,w))[0]
        #dc[i] = 3000.0/h * integrate.quad(E_z_inv,0,z[i],args=(om,ode,w))[0]
    dl = (1+z)*dc(z)
    mu_model = 5*np.log10(dl)+25

    #Calculate the likelihood
    LL = -0.5 np.dot(mu-mu_model,np.dot(icov,mu-mu_model))
    block[likes,"SNIA_LIKE"]=LL

    return 0 #Signal that it finished fine
    
"""
This function has to be here for design reasons.
It is only really used if the module is written in
C/C++/Fortran.
"""
def cleanup(self):
    return 0
