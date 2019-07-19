import numpy as np
import pypianoroll


data=np.load('temp.npz')
for key in data.keys():
    print(key)

print(data['nonzero'])
print(data['shape'])



print(data['nonzero'].shape)

