import numpy as np
M = np.arange(12.0).reshape((4, 3)) + 1
print(M[2,:])                   # [7. 8. 9.]

print(M[2:])                    # [[ 7.  8.  9.] 
                                #  [10. 11. 12.]]
