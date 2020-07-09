import numpy as np
a=np.array([[2,1,-2],[3,-3,-1],[1,-2,3]])
b=np.array([-1,5,6])
c=np.linalg.solve(a,b)
print(c)
