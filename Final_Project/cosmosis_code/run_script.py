"""
This is the script used to run the code for the final project.
"""

import os

do_analysis = True
do_postprocess = False

if do_analysis:
    base = "/home/tmcclintock/Desktop/Github_stuff/Astr513-Homeworks/Final_Project/Betoule2014Data/"
    datapath = base+"tablef1.dat"
    covpath  = base+"tablef2.dat"
    
    path = "my_tests/astr513/"
    cosmology = path+"final_cosmology.ini"
    pipeline = path+"final_pipeline.ini"
    cosmosis = "mpirun -n 4 cosmosis --mpi"
    
    command = "datapath=%s covpath=%s cosmology=%s %s %s"\
              %(datapath,covpath,cosmology,cosmosis,pipeline)

    os.system(command)

"""
Now that the code is run, we can do post processing below.
"""

if do_postprocess:
    x=0 #garbage for now
