
import pandas as pd
import os
import flywheel
fw=flywheel.Client()

colnames=["paths"]
#os.chdir('/Volumes/burkesar/research_projects')
os.chdir('/Users/burkesar/research_projects/')

#read in pathlists for available data on pmacs
pathlist = pd.read_csv('hcp/fmriprep/singularity_tools/fmapPaths.csv', header=None, names=colnames)
pathlist=pathlist["paths"].str.split("/", n=1, expand=True)
pathlist.columns=["subject","session"]

###create sublist from filepaths
#split paths into INDDID and session labels
subs=pathlist["subject"].str.split("-",n=1,expand=True)
sess=pathlist["session"].str.split("-",n=1,expand=True)
frames=[subs[1],sess[1]]
sublist=pd.concat(frames,axis=1)
sublist.columns=["INDDID","session"]

#####################read in test batch subs
df = pd.read_csv('/Users/burkesar/research_projects/hcp/sublists/hcp_reduced_tst1_20210419.csv')
contain_values = df[df['ID'].astype(str).str.contains('800')].reset_index(drop=True)

asymDF=contain_values.loc[contain_values['Symptomatic'] == 'Asymptomatic'].reset_index(drop=True)
asyMR1=asymDF[asymDF['ID_MR'].str.contains('MR1')].reset_index(drop=True)
##############

sublist=asyMR1["ID_MR"].str.split("_",n=1,expand=True)
sublist.columns=["INDDID","session"]


#read in subjects from flywheel by session
project="HCPMultiCenter"

####

#sessPath='pennftdcenter/' + project + '/' + sublist.iloc[i,0] + '/' + sublist.iloc[i,1]

#acqpath='pennftdcenter/' + project + '/' + '070003' + '/' + 'MR1' + '/SpinEchoFieldMap_PA'


sessPath='pennftdcenter/' + project + '/' + '070004' + '/' + 'MR1'
session=fw.lookup(sessPath)

for acq in session.acquisitions():
    if "SpinEchoFieldMap" in acq.label:
        print(acq.label)



project='HCPMultiCenter'
sessPath='pennftdcenter/' + project + '/' + 'techdev20210602' + '/' + 'BRAIN RESEARCH^GROSSMAN'
session=fw.lookup(sessPath)

for acq in session.acquisitions():
    if "SpinEchoFieldMap" in acq.label:
        print(acq.label)

acq=fw.lookup(sessPath + '/SpinEchoFieldMap_AP')
for file in acq.files:
    print(file.name)
    print(file)

sessions=fw.lookup(sessPath)
#search accuisitions for any type of fieldmap

acqs=[a for a in sessions.acquisitions() if "SpinEchoFieldMap" in a.label]
for acq in acqs:
    acq=acq.reload()
    for file in acq.files:
        if file.name.endswith(".nii.gz") and file['info']['BIDS']['Run']=='3' and file['info']['BIDS']['Dir']=='AP':         
            subj=file.info['BIDS']['Path'][0:10]
            sesslab=file.info['BIDS']['Path'][11:18]
            tmp_ap=file.get('info',{})
            tmp_ap['BIDS'].update({"IntendedFor":["{}/func/{}_{}_task-gambling_dir-PA_bold.nii.gz".format(sesslab,subj,sesslab),"{}/func/{}_{}_task-WM_dir-PA_bold.nii.gz".format(sesslab,subj,sesslab)]})
            file.update_info(tmp_ap)
        elif file.name.endswith(".nii.gz") and file['info']['BIDS']['Run']=='3' and file['info']['BIDS']['Dir']=='PA':         
            subj=file.info['BIDS']['Path'][0:10]
            sesslab=file.info['BIDS']['Path'][11:18]
            tmp_pa=file.get('info',{})
            tmp_pa['BIDS'].update({"IntendedFor":["{}/func/{}_{}_task-gambling_dir-PA_bold.nii.gz".format(sesslab,subj,sesslab),"{}/func/{}_{}_task-WM_dir-PA_bold.nii.gz".format(sesslab,subj,sesslab)]})
            file.update_info(tmp_pa)
                

#check output
for f in range(len(acqs)):
    files=acqs[f]['files']
    for i in range(len(files)):
        if files[i].name.endswith(".nii.gz"):
            if files[i]['info']['BIDS']['Run']=='3' and files[i]['info']['BIDS']['Dir']=='AP':
                print(files[i].info)
            elif files[i]['info']['BIDS']['Run']=='3' and files[i]['info']['BIDS']['Dir']=='PA':
                print(files[i].info)




                
   
