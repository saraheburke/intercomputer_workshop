#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 11:31:18 2021

@author: burkesar
"""

import pandas as pd
import os
import flywheel
fw=flywheel.Client()

qcSubs=pd.read_csv('/Users/burkesar/scripts/general/mrqc_setup/metadata.csv')
qcSubs.columns
qcSubs.dtypes

subIDs = qcSubs['SID']

#####

#create a project object and read in sublist of interest
group = 'pennftdcenter'
project_label = 'HUP6'
project= fw.lookup('{}/{}'.format(group,project_label))

audit_subs=qcSubs[qcSubs['Group']=='Penn FTD Center'].reset_index(drop=True)

#create a session level view
view = fw.View(columns='session')
df = fw.read_view_dataframe(view, project.id)
df.dtypes

#subet view output to include only columns of interest
sublist = df[['subject.label','session.label','session.timestamp','subject.id', 'session.id','project.label', 'project.id']]

#check compatibable data types
audit_subs.dtypes
#create series from df to use in isin command
audit_subs['SID']

#combine and compare get boolean values
sublist['subject.label'].isin(audit_subs['SID'])


####put all steps together by indexing booleans
#get intersection of INDDIDs in sublist that are also in audit 
HUP6qcList=sublist[sublist['subject.label'].isin(audit_subs['SID'])].reset_index(drop=True)

#will get ~ 2x b/c multiple sessions in sublist - verify with count of unique values
##A set doesn't store duplicate objects. 
##Even if an object is added more than once inside the curly brackets, only one copy is held in the set object.

#u_set=set(HUP6qcList['subject.label'])
#len(u_set)


#get intersection of INDDIDs in auditsubs that are also in sublist
QCboth=audit_subs[audit_subs['SID'].isin(sublist['subject.label'])]

QCboth['Path'][0]

QCboth['Path'].apply(lambda x: '/'.split(x),axis=1)

#show the opposite - subs not in qc list
#negtest=sublist[~sublist['subject.label'].isin(audit_subs['SID'])].reset_index(drop=True)

proj_log['sess_merge'] = proj_log[['subject.label','session.label']].apply(lambda x: '_'.join(x),axis = 1)
HUP6qcList

