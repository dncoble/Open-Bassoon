import numpy as np
import json
import pandas as pd
"""
make json file of specs from the select group
"""
names = ['7071', '8331', '9280', '9725', '10307']

full_dict = {}

for name in names:
    i_dict = {}
    
    file_name = name + "-parts.xlsx"
    wing = pd.read_excel(file_name, sheet_name="wing").values
    boot_small_bore = pd.read_excel(file_name, sheet_name="boot small bore").values
    boot_large_bore = pd.read_excel(file_name, sheet_name="boot large bore").values
    u_tube_in = pd.read_excel(file_name, sheet_name="u-tube in").values[0,1]
    u_tube_out = pd.read_excel(file_name, sheet_name="u-tube out").values[0,1]
    long_joint = pd.read_excel(file_name, sheet_name="long joint").values
    bell = pd.read_excel(file_name, sheet_name="bell").values
    
    
    
    i_dict["tenor"] = wing.tolist()
    i_dict["boot small"] = boot_small_bore.tolist()
    i_dict["boot large"] = boot_large_bore.tolist()
    i_dict["u tube in"] = u_tube_in
    i_dict["u tube out"] = u_tube_out
    i_dict["bass"] = long_joint.tolist()
    i_dict["bell"] = bell.tolist()
    
    full_dict[name] = i_dict

with open('bore_dims.json', 'w') as f:
    json.dump(full_dict, f)