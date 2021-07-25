#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:03:42 2021

@author: seburke
"""
import flywheel
fw=flywheel.Client()

group= 'pennftdcenter'
project="TEST_control_hcp"
sub='800162'

sess='2019-03-05 14:04:54'
acq='T1w_MPR'

acquisition=fw.lookup('{}/{}/{}/{}/{}'.format(group,project,sub,sess,acq))
acquisition.add_tag("I am a bad scan!!!")
acquisition.update_info({ 'QC': '1' })
acquisition = acquisition.reload()

acquisition.tags
acquisition.info
