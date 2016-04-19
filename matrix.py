import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
arr = np.zeros((9,9))
print(arr)
#make all entries last row have value 1 and left 3 columns have value 1
arr[8,:],arr[:,:3] = 1,1
print(arr)
#assign specific entries with value 1
arr[(4,5)], arr[(7,7)], arr[(1,8)] = 1,1,1
plt.spy(arr)
plt.savefig('arrplot.png')