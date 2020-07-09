import numpy as np
rand_matrix=np.random.randint(1,10,size=(4,4))
print(rand_matrix)
print('sum of diagonals is : ', np.trace(rand_matrix))
