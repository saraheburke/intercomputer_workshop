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

fullfiles=[]
for s in range(len(subs)):   
    sessPath='pennftdcenter/' + project + '/' + subs[s] + '/' + sesslist[s]
    session=fw.lookup(sessPath)
    for acq in session.acquisitions():
        if "SpinEchoFieldMap" in acq.label:
            acq=acq.reload()
            for file in acq.files:
                if file.type=="nifti" and file.info['PhaseEncodingDirection']=='j-' and "BIDS" in file.info.keys():
                    fullfiles.append(file)
                    fx=sorted(fullfiles, key=lambda i:i['info']['BIDS']['Filename'])
    yy=fx.pop()
    print(yy.info['BIDS']['Filename'])
    yz=yy.get('info',{})       
    
if "IntendedFor" in yy.info:
        yz['IntendedFor'].append(["func/{}_{}_task-gambling_dir-PA_bold.nii.gz".format(subs[s],sesslist[s]), "func/{}_{}_task-WM_dir-PA_bold.nii.gz".format(subs[s],sesslist[s])])
    else:
        yz.update({'IntendedFor':["func/{}_{}_task-gambling_dir-PA_bold.nii.gz".format(subs[s],sesslist[s]), "func/{}_{}_task-WM_dir-PA_bold.nii.gz".format(subs[s],sesslist[s])]})
    yy.update_info(yz)
        if file.type=='nifti' and file.info['PhaseEncodingDirection']=='j-' and "BIDS" in file.info.keys():
                fullfiles.append(file)
                fx=sorted(fullfiles, key=lambda i:i['info']['BIDS']['Filename'])
    
    
    
    
    if "IntendedFor" in file.info.keys():
                        
    else:
                        
                
                
  
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
                    yz=yy.get('info',{})
    if "IntendedFor" in yy.info:
        yz['IntendedFor'].append(["func/{}_{}_task-gambling_dir-PA_bold.nii.gz".format(subs[s],sesslist[s]), "func/{}_{}_task-WM_dir-PA_bold.nii.gz".format(subs[s],sesslist[s])])
    else:
        yz.update({'IntendedFor':["func/{}_{}_task-gambling_dir-PA_bold.nii.gz".format(subs[s],sesslist[s]), "func/{}_{}_task-WM_dir-PA_bold.nii.gz".format(subs[s],sesslist[s])]})
    yy.update_info(yz)
        if file.type=='nifti' and file.info['PhaseEncodingDirection']=='j-' and "BIDS" in file.info.keys():
                fullfiles.append(file)
                fx=sorted(fullfiles, key=lambda i:i['info']['BIDS']['Filename'])
    yy=fx.pop()
    print(yy.info['BIDS']['Filename'])
    yz=yy.get('info',{})
    if "IntendedFor" in yy.info:
        yz['IntendedFor'].append(["func/{}_{}_task-gambling_dir-PA_bold.nii.gz".format(subs[s],sesslist[s]), "func/{}_{}_task-WM_dir-PA_bold.nii.gz".format(subs[s],sesslist[s])])
    else:
        yz.update({'IntendedFor':["func/{}_{}_task-gambling_dir-PA_bold.nii.gz".format(subs[s],sesslist[s]), "func/{}_{}_task-WM_dir-PA_bold.nii.gz".format(subs[s],sesslist[s])]})
    yy.update_info(yz)
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    if "IntendedFor" in file.info.keys():
                        print('yes', file.info['BIDS']['Filename'])
                    else:
                        print('no',file.info['BIDS']['Filename'])
                
                         
                
                
    

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
                        print('no',file.info['BIDS']['Filename'])
                        
                        
                        
                        #print(file.info.keys())
                        #file.update_info(file.info)
                        print(file.info['IntendedFor'])
                        
                        
                        
filecheck = 'pennftdcenter/' + project + '/' + subs[s] + '/' + sesslist[s] 
session=fw.lookup(filecheck)
acqs=[a for a in session.acquisitions() if "SpinEchoFieldMap" in a.label]
for acq in acqs:
        acq=acq.reload()
        for file in acq.files:
            print(file.info.keys())

