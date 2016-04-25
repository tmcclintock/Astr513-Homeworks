"""
This is the script used to run the code for the final project.
"""

import os

do_analysis = True
do_postprocess = False

if do_analysis:
    datapath = "/path/to/the/data"
    covpath  = "/path/to/the/cov/matrix"
    
    cosmology = "final_cosmology.ini"
    pipeline = "final_pipeline.ini"
    
    command = "datapath=%s covpath=%s cosmology=%s cosmosis %s"\
              %(datapath,covpath,cosmology,pipeline)

"""
Now that the code is run, we can do post processing below.
"""

if do_postprocess:
    x=0 #garbage for now
