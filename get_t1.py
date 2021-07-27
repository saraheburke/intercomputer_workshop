#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 11:13:39 2021

@author: burkesar
"""

def get_t1_file(sess):
    '''
        Function to pick the most desirable T1 file out of several in a session. Very, very FTDC-specific.
    '''
    #is_t1 = [any(['T1' in f.classification['Measurement'] for f in a.files \
    #    if 'Measurement' in f.classification.keys()]) for a in sess.acquisitions()]
    #t1_acq = [a for (a, v) in zip(sess.acquisitions(), is_t1) if v]
    
    t1_acq = []
    acqlist = sess.acquisitions()
    for acq in acqlist:
        if any(['T1' in f.classification['Measurement'] for f in acq.files \
            if 'Measurement' in f.classification.keys()]):
                t1_acq.append(acq)
    
    t1_file = None
    
    for acq in t1_acq:
        lab = acq.label.lower()
        if ("vnav" in lab) and ("moco" in lab) and ("rms" in lab) and not ("nd" in lab):
            t1_file = get_bids_nifti(acq)
            return(t1_file)
    
    for acq in t1_acq:
        lab = acq.label.lower()
        if ("vnav" in lab) and ("rms" in lab) and not ("nd" in lab):
            t1_file = get_bids_nifti(acq)
            return(t1_file)
    
    for acq in t1_acq:
        lab = acq.label.lower()
        if ("ax" in lab) and ("mprage" in lab):
            t1_file = get_bids_nifti(acq)
            return(t1_file)
    
    for acq in t1_acq:
        lab = acq.label.lower()
        if ("sag" in lab) and ("mprage" in lab):
            t1_file = get_bids_nifti(acq)
            return(t1_file)
    
    return(t1_file)