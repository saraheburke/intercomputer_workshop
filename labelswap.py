#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 08:01:22 2020

@author: seburke
"""

import flywheel
fw=flywheel.Client()

groupLab='pennftdcenter'

group=fw.lookup('{}'.format(groupLab))
for project in group.projects():
  print('%s: %s' % (project.id, project.label))

projectLabel='Alector'
project=fw.lookup('{}/{}'.format(groupLab,projectLabel))

phaseOne=[]
for subject in project.subjects():
    print('%s: %s' % (subject.id, subject.label))
    phaseOne.append(subject.label)
    
subjectList=['070109', '070110', '070112', '070113','070115', '070116', '070120', '070122', '070123']    
#070119

phaseOne.sort()
print(phaseOne[0:17])

subjectList=phaseOne[0:17]

subjectList=['070001','070004','070006','070008','070013','070016','070017']

subjectList=['070004','070006','070008']


for sub in range(0,len(subjectList)):
    subject=fw.lookup('{}/{}/{}'.format(groupLab,projectLabel,subjectList[sub]))
    #print(subject.sessions()[0].timestamp)
    #print(subject.sessions()[1].timestamp)
    #print(subject.sessions()[0].label)
    #print(subject.sessions()[1].label)
    subject.sessions()[0].update(label='20201116x1235')
    #subject.sessions()[0].update(label='MR2')
    
    
    
    
    subject.sessions()[1].update(label='MR1')
    print(subject.sessions()[1].label)
    
for sub in range(0,len(subjectList)):
    subject=fw.lookup('{}/{}/{}'.format(groupLab,projectLabel,subjectList[sub]))
    for session in subject.sessions():
        print('%s: %s: %s' % (session.id, session.label, subject.label))


for sess in sessions():
    print(session.label)
subject=fw.lookup('{}/{}/{}'.format(group,projectLabel,subject))
subject.sessions()[1].update(label='MR2')


session.update(label='New session Label')

subject.update({'type': 'human', 'sex': 'female'})

x=fw.get_container_analyses(sess.id)
x[0].items()


###
group= 'pennftdcenter'
project="TEST_control_hcp"
sub='800162'
sess='2019-03-05 14:04:54'
acq='T1w_MPR'

acquisition=fw.lookup('{}/{}/{}/{}/{}'.format(group,project,sub,sess,acq))
acquisition.tags
acquisition.add_tag("I am a bad scan!!!")
acquisition.update_info({ 'QC': 'pass' })
acquisition = acquisition.reload()


