import virtualPC as vpc
from virtualPC import VirtualData as VD
import editorVPC as ev
import os

proName = 'kkkk'
SEP = '|||'
SMALLSEP = '</>'
newLineCommand = 'stiffMouse|||1|||1|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
chkID = 's1:#$%^&*(st)</>typeWrite</>hello world</>TAB4</>TAB5</>TAB6</>TAB7</>TAB8</>TAB9</>TAB10'
chkID=str(chkID)
chkSpl = chkID.split(SMALLSEP)
SHELL = f'dataProjects/{proName}/{proName}.vpc'    

tempID = chkSpl[0].split(':')
ssID = int(tempID[0].lstrip('s'))

if ssID > 1:
    preID = ssID - 1
else:
    preID = 1

newLID = f's{preID}:{tempID[1]}{SEP}{newLineCommand}'
onNewLID = f's{preID}:{tempID[1]}'


V = VD(SHELL)
HEADER = V.header()
PRE = V.preLoader()
PRO = V.proGeneral()
SEQ = V.proSequence()
LOG = V.logsSession()

#Sequences
newSEQinsert = []
for i in SEQ:
    iss = str(i)
    ill = iss.split(SEP)
    for j in ill:
        if j==onNewLID:
            newSEQinsert.append(newLID)        
    newSEQinsert.append(i)

# for i in newSEQinsert:print(i)

noIDSEQ=[]
for i in newSEQinsert:
    i=str(i)
    iTr=i.startswith('s')
    if iTr: 
        ill=i.split(SEP)
        newLine=ill[1:]
        noIDSEQ.append(newLine)  

# for i in noIDSEQ:print(i)


lnIDS = len(noIDSEQ)
freshLinesSEQ=[newSEQinsert[0]]
for i in range(lnIDS):
    x = i+1
    idConstruct = f's{x}:#$%^&*(st)'
    consT=""
    for j in noIDSEQ[i]:        
        consT += j + SEP
    consT=consT.rstrip(SEP)
    compleT= idConstruct+SEP+consT
    freshLinesSEQ.append(compleT)  

for i in freshLinesSEQ:print(i)

#Corect ID General
freshLinesPRO = [PRO[0]]
gID = 1
for s in freshLinesSEQ:
    s=str(s)
    splS = s.split(SEP)
    if splS[1]=="DictWrite":
        sID = splS[0]
        gFile = splS[2]
        gLine=f'g{gID}:#$%^&*(gg)|||DictWrite|||{gFile}|||TypeWrite|||{sID}|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
        freshLinesPRO.append(gLine)
        gID+=1

for i in freshLinesPRO:print(i)

f=open(f'dataProjects/{proName}/{proName}.vpc', 'w+')    
for vpcH in HEADER:f.write(vpcH+'\n')    
for vpcPRE in PRE:f.write(vpcPRE+'\n')    
for vpcPRO in freshLinesPRO:f.write(vpcPRO+'\n')    
for vpcSEQ in freshLinesSEQ:f.write(vpcSEQ+'\n')    
for vpcLOG in LOG:f.write(vpcLOG+'\n')
f.close()


