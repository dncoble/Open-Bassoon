import numpy as np
import json
import pandas as pd
"""
make json file on bore and hole data for select instruments
"""
#%% compile bore data into dictionary
names = ['Heckel 7170', 'Heckel 8331', 'Heckel 9280', 'Heckel 9725',\
         'Heckel 9919', 'Heckel 10307', 'Riedl 296757']

bore_dict = {}

for name in names:
    i_dict = {}
    
    file_name = "./bores/%s.xlsx"%name
    wing = pd.read_excel(file_name, sheet_name="wing").values
    boot_small_bore = pd.read_excel(file_name, sheet_name="boot small bore").values
    boot_large_bore = pd.read_excel(file_name, sheet_name="boot large bore").values
    u_tube_in = pd.read_excel(file_name, sheet_name="u-tube in").values[0,0]
    u_tube_out = pd.read_excel(file_name, sheet_name="u-tube out").values[0,0]
    long_joint = pd.read_excel(file_name, sheet_name="long joint").values
    bell = pd.read_excel(file_name, sheet_name="bell").values
    
    
    i_dict["tenor"] = wing.tolist()
    i_dict["boot small"] = boot_small_bore.tolist()
    i_dict["boot large"] = boot_large_bore.tolist()
    i_dict["u tube in"] = u_tube_in
    i_dict["u tube out"] = u_tube_out
    i_dict["bass"] = long_joint.tolist()
    i_dict["bell"] = bell.tolist()
    
    bore_dict[name] = i_dict

#%% compile data on holes into dictionary
names = ['Schreiber', 'Heckel 9919', 'Riedl 296757']

holes_dict = {}

file_name = "./holes/hole specification.xlsx"
for name in names:
    holes_dict[name] = data = pd.read_excel(file_name, sheet_name=name).values.tolist()
    


#%% combine both dicts and save to json file
full_dict = {}

full_dict['bore'] = bore_dict
full_dict['holes'] = holes_dict

with open('dimensions.json', 'w') as f:
    json.dump(full_dict, f)