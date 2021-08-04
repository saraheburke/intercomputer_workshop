#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:55:54 2021

@author: burkesar
"""

#!/usr/bin/env python3

import json
import os
import subprocess
import sys
from collections import defaultdict
import re
import pandas as pd
import flywheel 
fw=flywheel.Client()

project='HCPMultiCenter'

df = {"INDDID":["070001","070001","800172","800177"], "Session":["MR1","MR2","MR1","MR1"]}
df = pd.DataFrame(df)

subs = df["INDDID"].to_list()
sesslist = df["Session"].to_list()

for s in range(len(subs)):   
    sessPath='pennftdcenter/' + project + '/' + subs[s] + '/' + sesslist[s]
    session=fw.lookup(sessPath)
    apfiles=[]
    pafiles=[]
    for acq in session.acquisitions():
        if "SpinEchoFieldMap" in acq.label:
            acq=acq.reload()
            for file in acq.files:
                if file.type=="nifti" and file.info['PhaseEncodingDirection']=='j-' and "BIDS" in file.info.keys():
                    apfiles.append(file)
                elif file.type=="nifti" and file.info['PhaseEncodingDirection']=='j' and "BIDS" in file.info.keys():
                    pafiles.append(file)
    apS=sorted(apfiles, key=lambda i:i['info']['BIDS']['Filename'])
    paS=sorted(pafiles, key=lambda i:i['info']['BIDS']['Filename'])
    ya=apS.pop()      
    yaz=ya.get('info',{})
    #print(yaz['BIDS']['Filename'])
    yp=paS.pop()
    ypz=yp.get('info',{})
    #print(ypz['BIDS']['Filename'])
    
    if "IntendedFor" in ya.info:
        yaz['IntendedFor'].append(["func/{}_{}_task-gambling_dir-PA_bold.nii.gz".format(subs[s],sesslist[s]), "func/{}_{}_task-WM_dir-PA_bold.nii.gz".format(subs[s],sesslist[s]),"sub-{}_ses-{}_task-rest_dir-PA_run-{}_bold.nii.gz".format(subs[s],sesslist[s],ya.info['BIDS']['Run'])])
    elif "IntendedFor" not in ya.info:
        yaz.update({'IntendedFor':["func/{}_{}_task-gambling_dir-PA_bold.nii.gz".format(subs[s],sesslist[s]), "func/{}_{}_task-WM_dir-PA_bold.nii.gz".format(subs[s],sesslist[s]),"sub-{}_ses-{}_task-rest_dir-PA_run-{}_bold.nii.gz".format(subs[s],sesslist[s],ya.info['BIDS']['Run'])]})
        ya.update_info(yaz)
    elif "IntendedFor" in yp.info:
        ypz['IntendedFor'].append(["func/{}_{}_task-gambling_dir-AP_bold.nii.gz".format(subs[s],sesslist[s]), "func/{}_{}_task-WM_dir-AP_bold.nii.gz".format(subs[s],sesslist[s]),"sub-{}_ses-{}_task-rest_dir-AP_run-{}_bold.nii.gz"].format(subs[s],sesslist[s],yp.info['BIDS']['Run']),"sub-{}_ses-{}_task-rest_dir-AP_run-{}_bold.nii.gz".format(subs[s],sesslist[s],yp.info['BIDS']['Run']))
    else:
        ypz.update({'IntendedFor':["func/{}_{}_task-gambling_dir-AP_bold.nii.gz".format(subs[s],sesslist[s]), "func/{}_{}_task-WM_dir-AP_bold.nii.gz".format(subs[s],sesslist[s]),"sub-{}_ses-{}_task-rest_dir-AP_run-{}_bold.nii.gz".format(subs[s],sesslist[s],yp.info['BIDS']['Run'])]})
        yp.update_info(ypz)


######check fields
for s in range(len(subs)):   
    sessPath='pennftdcenter/' + project + '/' + subs[s] + '/' + sesslist[s]
    session=fw.lookup(sessPath)
    for acq in session.acquisitions():
        if "SpinEchoFieldMap" in acq.label:
    #acqs=[a for a in session.acquisitions() if "SpinEchoFieldMap" in a.label]
            acq=acq.reload()
            for file in acq.files:
                if file.type=="nifti":
                    yz=file.get('info',{})           
                    if "IntendedFor" in file.info:
                        print("yes",file.info['BIDS']['Filename'])
                    else:
                        print("no",file.info['BIDS']['Filename'])    
                        

#remove IF field
for s in range(len(subs)):   
    sessPath='pennftdcenter/' + project + '/' + subs[s] + '/' + sesslist[s]
    session=fw.lookup(sessPath)
    for acq in session.acquisitions():
        if "SpinEchoFieldMap" in acq.label:
    #acqs=[a for a in session.acquisitions() if "SpinEchoFieldMap" in a.label]
            acq=acq.reload()
            for file in acq.files:
                if file.type=="nifti":
                    if "IntendedFor" in file.info.keys():
                        print('yes', file.info['BIDS']['Filename'])
                        fdel=file.get('info',{})
                        del(fdel['IntendedFor'])
                        file.update_info(fdel)
                    else:
                        print('no',file.info['BIDS']['Filename']
                        
                        
                        

