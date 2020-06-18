import numpy as np
import sys
import time 
list =range(100)
print(sys.getsizeof(3)*len(list))

array=np.arange(100)
print(array.size * array.itemsize)
