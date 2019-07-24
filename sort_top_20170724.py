import numpy as np
E = np.array([0.97894605,0.63243309,0.15664988,0.04969291,0.69779018])
labels = ['A', 'B', 'C', 'D']
samples=np.array([[0.55679902,0.65582205,0.32020463,0.99920748,0.97329702],
[0.80244032,0.07441741,0.05449902,0.71137391,0.49830497],
 [0.78269515,0.46577525,0.30835287,0.86208522,0.64927529],
 [0.54046995,0.92198106,0.90779059,0.38312245,0.8678798]
])
distances = np.sqrt(np.sum(np.square(samples - E), axis = -1))
idxs = np.argsort(distances)
print('E=%s:%f,%s:%f,%s:%f'%(labels[idxs[0]],distances[idxs[0]], labels[idxs[1]],distances[idxs[1]], labels[idxs[2]],distances[idxs[2]]))
