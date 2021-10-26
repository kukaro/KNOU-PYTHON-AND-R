import numpy as np

mx = np.array(range(1, 13)).reshape(2, 6)
print(np.insert(mx, 2, np.array([10, 20]), axis=1).reshape(2, 7))
