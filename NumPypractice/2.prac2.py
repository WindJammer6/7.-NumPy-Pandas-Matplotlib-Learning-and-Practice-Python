#How to create a boolean array? ( Create a 3×3 numpy array of all True’s)
import numpy as np

a = np.full((3,3), True)
print(a)

# Alternate method:
print(np.ones((3,3), dtype=bool))
