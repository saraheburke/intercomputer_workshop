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

#bidsdir = '/project/ftdc_hcp/fmriBids/test06'
#files = os.listdir(bidsdir)
project='HCPMultiCenter'

df = {"INDDID":["070001","070001"], "Session":["MR1","MR2"]}
df = pd.DataFrame(df)

subs = df["INDDID"].to_list()
sesslist = df["Session"].to_list()

fullfiles=[]
for s in range(len(subs)):     
    sessPath='pennftdcenter/' + project + '/' + subs[s] + '/' + sesslist[s]
    session=fw.lookup(sessPath)
    acqs=[a for a in session.acquisitions() if "SpinEchoFieldMap" in a.label]
    for acq in acqs:
        acq=acq.reload()
        for file in acq.files:
            if file.type=='nifti' and file.info['PhaseEncodingDirection']=='j-' and "BIDS" in file.info.keys():
                fullfiles.append(file)
                #print(file.info['BIDS']['Filename'])
                fx=sorted(fullfiles, key=lambda i:i['info']['BIDS']['Filename'])
    yy=fx.pop()
    print(yy.info['BIDS']['Filename'])
    yz=yy.get('info',{})
    print(yz.keys())
    if "IntendedFor" in yy.info:
        yz['IntendedFor'].append('testno')
        #then update info:
    else:
        yz.update({'IntendedFor':['testpos']})



 file_info = file_.get('info',{})
         file_info.update({
            'BIDS':{
                <your_data>
            })
        file_.update_info(file_info)    
         

        for f,g in zip(files_json,files_json_fullpaths):
            temp = re.findall(r'\d+', f)
            if int(temp[-1]) == runs[-1]:
                items = f.split('_')
                if 'dir-AP' in items:
                    with open(g,'r')as f_json:
                        data=json.load(f_json)
                        data["IntendedFor"]=["func/{}_{}_task-gambling_dir-PA_bold.nii.gz".format(subj,s$
                                             "func/{}_{}_task-WM_dir-PA_bold.nii.gz".format(subj,ses)]
                        f_json.close
                    with open(g,'w')as f_json:
                        json.dump(data,f_json,indent=4,sort_keys=True)
                        f_json.close
                elif 'dir-PA' in items:
                    with open(g,'r')as f_json:
                        data=json.load(f_json)
                        data["IntendedFor"]=["func/{}_{}_task-gambling_dir-AP_bold.nii.gz".format(subj,s$
                                             "func/{}_{}_task-WM_dir-AP_bold.nii.gz".format(subj,ses)]
                        f_json.close
                    with open(g,'w')as f_json:
                        json.dump(data,f_json,indent=4,sort_keys=True)
                        f_json.close
