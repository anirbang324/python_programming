#sparse data : most of the values will be 0
#dense array : most of the values will not be 0
#CSC - compressed sparse column.
#CSR - compressed sparse row.

# import numpy as np
# from scipy.sparse import csr_matrix
# arr = np.array([0,0,0,0,3,5,7])
# print(csr_matrix(arr))
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(arr))

