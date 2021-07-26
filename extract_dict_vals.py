#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 11:06:25 2021

@author: seburke
"""

import pandas as pd
import os
import flywheel
fw=flywheel.Client()

project="HCPMultiCenter"

sessPath='pennftdcenter/' + project + '/' + '800174' + '/' + 'MR1'
session=fw.lookup(sessPath)

#make a list of dictionaries within acquisitions
files_list=session.acquisitions()

acq_list=[]
jj=[]
for acq in session.acquisitions():
    if "SpinEchoFieldMap" in acq.label:
        acq_list.append(acq)
        for i in acq_list:
            for j in i.files:
                if "nifti" in j.type:
                    jj.append(j.name)
    
##single subject example               
                    
import pandas as pd
import os
import flywheel
fw=flywheel.Client()

project="HCPMultiCenter"

sessPath='pennftdcenter/' + project + '/' + '800174' + '/' + 'MR1'
session=fw.lookup(sessPath)


acq_list=[]
for acq in session.acquisitions():
    if "SpinEchoFieldMap" in acq.label:
        acq_list.append(acq)
        acq_list[0].reload()
        subj='sub-800174'
        sesslab='ses-MR1'
        file=acq_list[0]['files'][1]
        tmp_ap=file.get('info',{})             
        tmp_ap['BIDS'].update({"IntendedFor":["{}/func/{}_{}_task-gambling_dir-PA_bold.nii.gz".format(sesslab,subj,sesslab),"{}/func/{}_{}_task-WM_dir-PA_bold.nii.gz".format(sesslab,subj,sesslab)]})
        file.update_info(tmp_ap)
        
#check file info for updated field
acq_list[0]['files'][1]['info']['BIDS']           

#####



a_files=[]
for acq in session.acquisitions():
    if "SpinEchoFieldMap" in acq.label:
        a_files.append(acq)
        for s in a_files:
            print(s['files'][1]['info']['BIDS']['Filename'])

                
            [f for f in subfiles_list if "nifti" in f['type']]
        
        for f in files_list:
            subfiles_list.append(f)
            for g in subfiles_list:
                if subfiles_list[g]['type']=='nifti':
                    print(g)
                
[dictio for dictio in dictlist if dictio[key] in valuelist]


files_list[0]['files'][0]['type']

#acquisition.download_file('hello.txt', '/tmp/hello.txt')