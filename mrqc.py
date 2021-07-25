import pandas as pd
import os
import re
import numpy as np
import datetime
import pytz
import pathlib
import flywheel

#####

def run_mrqc(projectLabel, subjectLabel, sessionLabel, group = 'pennftdcenter'):
    fw = flywheel.Client()
    g = fw.lookup('gears/mriqc/0.7.0_0.15.1')
    s = fw.lookup('/'.join([group,projectLabel,str(subjectLabel),str(sessionLabel)]))
    
    config = {
    'measurement': 'T1',
    'save_derivatives': True,
    'save_outputs': True,
    'verbose_reports': True
                    }
    jobs=[]
    input_list=[]
    acqs=[a for a in s.acquisitions() if "T1" in a.label]
    for acq in acqs:
        for file in acq.files:
            if file.name.endswith(".nii.gz") and "BIDS" in file.info.keys() and "norm" in file.info['BIDS']['Filename']:
                input_list.append(acq.id)   
                for f in input_list:
                    infile=fw.get(f)
                    subfiles=infile['files']
                    nifti_file = [n for n in subfiles if "nii.gz" in n.name]
                    for y in range(len(nifti_file)):
                        input = {
                            'nifti':nifti_file[y]}             
                        jobID = g.run(inputs=input,config=config)
                        jobs.append(jobID)   
                        jobDF=pd.DataFrame(jobs,columns=["jobids"])
    
    return jobDF


