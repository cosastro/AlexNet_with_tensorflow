import numpy as np

mdl = np.load('bvlc_alexnet.npy', encoding = "bytes").item()

#print(type(mdl))
for k,v in mdl.items():
    print(k, len(v), type(v[0]), v[0].shape)
    #print(k, np.array(v[0]).shape)

