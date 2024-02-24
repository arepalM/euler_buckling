from abaqus import *
from abaqusConstants import *
from caeModules import *
import json
import os

# Dumped JSON files from build_hinge.py to be read in here
#with open('parameter_dict.json', 'r') as openfile:
#   parameter_dict = json.load(openfile)
with open('file_dict.json','r') as openfile:
    file_dict = json.load(openfile)

file_dict['odb_file'] = 'C:\\Users\\hokie\\OneDrive - Johns Hopkins\\Documents\\JHU\\Research\\morphing wing\\Abaqus\\buckling\\iter_1000\\part_iter1000.odb'
# Need to reformat dictionary value for Abaqus syntax
odb_file = file_dict['odbfile'].replace('\\','/')
odb = session.odbs[odb_file]
# Extract total vertical reaction force
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RF', 
    NODAL, ((COMPONENT, 'RF2'), )), ), operator=ADD, nodeSets=(
    "PART-1-1.BOT_NSET", ))
session.odbs[odb_file]
# Extract RP vertical displacement
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('U', 
    NODAL, ((COMPONENT, 'U2'), )), ), nodeSets=("RP-SET", ))
xy1 = session.xyDataObjects['U:U2 PI: ASSEMBLY N: 1']
xy2 = session.xyDataObjects['ADD_RF:RF2']
# Write out csv file for total vertical RF
x0 = session.xyDataObjects['ADD_RF:RF2']
session.writeXYReport(fileName=str(odb_file) + '_RF_TOT.csv', appendMode=OFF, xyData=(x0, ))
# Write out csv file for vertical displacement of RP
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('U', 
    NODAL, ((COMPONENT, 'U2'), )), ), nodeSets=("RP-SET", ))
x0 = session.xyDataObjects['U:U2 PI: ASSEMBLY N: 1']
session.writeXYReport(fileName=str(odb_file) + '_U2.csv', xyData=(x0, ))