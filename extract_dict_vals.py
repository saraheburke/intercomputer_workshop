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

files_list=[]
subfiles_list=[]
for acq in session.acquisitions():
    if "SpinEchoFieldMap" in acq.label:
        files_list.append(acq)
        for f in files_list:
            subfiles_list.append(f)
            for g in subfiles_list:
                if subfiles_list[g]['type']=='nifti':
                    print(g)
                
[dictio for dictio in dictlist if dictio[key] in valuelist]


files_list[0]['files'][0]['type']

#acquisition.download_file('hello.txt', '/tmp/hello.txt')