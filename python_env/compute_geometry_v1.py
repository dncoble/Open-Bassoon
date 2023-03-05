import numpy as np
import json
import sklearn.linear_model
import matplotlib.pyplot as plt
"""
Doing computations on the bassoon geometry and saving data to a file read by 
the CAD program

numpy: 1.19.5
"""
#%% load json and data arrays
with open("./select group parts/bore_dims.json") as f:
    instruments = json.loads(f.read())

instrument_names = ['7170', '8331', '9280', '9725', '10307']

tenors = []
small_boots = []
large_boots = []
basses = []
bells = []
utube_ins = []
utube_outs = []

parts = [tenors, small_boots, large_boots, basses, bells]
part_names = ['tenor', 'small boot', 'large boot', 'bass', 'bell']

for name in instrument_names:
    data = instruments[name]
    
    tenor = np.array(data['tenor'])
    small_boot = np.array(data['boot small'])
    large_boot = np.array(data['boot large'])
    bass = np.array(data['bass'])
    bell = np.array(data['bell'])
    utube_in = data['u tube in']
    utube_out = data['u tube out']
    
    tenors.append(tenor)
    small_boots.append(small_boot)
    large_boots.append(large_boot)
    basses.append(bass)
    bells.append(bell)
    utube_ins.append(utube_in)
    utube_outs.append(utube_out)

#%% 
'''
plot the deviation of each part from a reference cone found using linear
regression
'''
# for i, part in enumerate(parts):
#     lin_model = sklearn.linear_model.LinearRegression()
#     # append all values used for linear regression
#     X = part[0]
#     for instrument in part[1:]:
#         X = np.append(X, instrument, axis=0)
    
#     lin_model.fit(X[:,1].reshape(-1, 1), X[:,0])
    
    
#     plt.figure(figsize=(6.5, 4))
#     plt.title("Deviation from reference cone of %s"%part_names[i])
#     for j, instrument in enumerate(part):
#         d = instrument[:,0] # measured diameter
#         x = instrument[:,1]
        
#         delta = d - lin_model.predict(x.reshape(-1, 1))
        
#         plt.plot(x, delta, label="#%s"%instrument_names[j])
    
#     plt.xlabel("length (in)")
#     plt.ylabel("deviation (in)")
#     plt.legend(loc=1)
#     plt.tight_layout()
#     plt.show()
#     plt.savefig("./plots/%s.png"%part_names[i], dpi=500)
#%%
'''
Inventor imports parameters as XML files which need a specific format. I've 
set up each part to have parameter names which allow as much sharing as possible.
The format is as follows:

For tenor, bass, and bell:
    x: bore length
    rn for n=0...20: equally spaced bore radius through the length
    hm for m=0...(#holes - 1): diameter of the mth hole on that part
    tm for m=0...(#holes - 1): length of the mth hole (taken at the thinnest point)

For boot:
    xs: bore length for small boot
    xl: bore length for large boot
    dc:  diameter of the u-tube curve
    rsn for n=0...20: equally spaced bore radius in small boot. rs20=u-tube in
    rln for n=0...20: equally spaced bore radius in large boot. rl0 = u-tube out
    hsm for m=0...(#small side holes - 1): diameter of the mth small side hole
    hlm for m=0...(#large side holes - 1): diameter of the mth large side hole
'''
# chose which instrument data is being compiled
instrument = 0

# gather all instrument data
tenor = tenors[instrument]
small_boot = small_boots[instrument]
large_boot = large_boots[instrument]
bass = basses[instrument]
bell = bells[instrument]
utube_in = utube_ins[instrument]
utube_out = utube_outs[instrument]

for i, part in enumerate([tenor, bass, bell]):
    part_name = ["tenor", "small boot", "bell"][i]
    D = part[:,0]
    X = part[:,1]
    
    x = X[-1]
    
    rn = .5*np.interp(np.linspace(0, x, num=21, endpoint=True), X, D)
    
    
    
    
    
