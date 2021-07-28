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

sessPath='pennftdcenter/' + project + '/' + '800167' + '/' + 'MR1'
session=fw.lookup(sessPath)


acq_list=[]
for acq in session.acquisitions():
    if "SpinEchoFieldMap" in acq.label:
        acq_list.append(acq)
        acq = acq.reload()
        subj='sub-800167'
        sesslab='ses-MR1'
        # Only update intended for on Nifti files.        
        for file in acq.files:
            if file.type == 'nifti' and file['info']['BIDS']['Run']=='3' and file['info']['BIDS']['Dir']=='AP':  
                file.update_info({
                   "IntendedFor":[
                       "{}/func/{}_{}_task-gambling_dir-PA_bold.nii.gz".format(sesslab,subj,sesslab),
                       "{}/func/{}_{}_task-WM_dir-PA_bold.nii.gz".format(sesslab,subj,sesslab)
                   ]})
            elif file.type == 'nifti' and file['info']['BIDS']['Run']=='3' and file['info']['BIDS']['Dir']=='PA':  
                file.update_info({
                   "IntendedFor":[
                       "{}/func/{}_{}_task-gambling_dir-AP_bold.nii.gz".format(sesslab,subj,sesslab),
                       "{}/func/{}_{}_task-WM_dir-AP_bold.nii.gz".format(sesslab,subj,sesslab)
                   ]
                })
###########
