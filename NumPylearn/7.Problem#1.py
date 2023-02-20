#Initialise this array pattern (try your best not to hardcode)
#[[1. 1. 1. 1. 1.]
# [1. 0. 0. 0. 1.]
# [1. 0. 9. 0. 1.]
# [1. 0. 0. 0. 1.]
# [1. 1. 1. 1. 1.]]
import numpy as np

a = np.ones((5,5))

a[1:(5-1), 1:(5-1)] = 0

a[2, 2] = 9

print(a)




