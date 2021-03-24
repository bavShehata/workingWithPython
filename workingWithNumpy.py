

import sys

print(sys.version)

# We import NumPy into Python
import numpy as np

# We create a 1D ndarray that contains only integers
x = np.array([1, 2, 3, 4, 5])

# Let's print the ndarray we just created using the print() command
print('x = ', x)
print(type(x))


abc = np.array(['a','b','c','d','e','f','g','h','i','j'])
print("x: ", x)
print("shape: ", x.shape)
print("size: ", x.size)
print("type: ", x.dtype)


x = np.zeros((5,2))
print("x: ", x)
print("shape: ", x.shape)
print("size: ", x.size)
print("type: ", x.dtype)


# Using the Built-in functions you learned about in the
# previous lesson, create a 4 x 4 ndarray that only
# contains consecutive even numbers from 2 to 32 (inclusive)

x = np.arange(2,33,2).reshape((4,4))
print(x)




# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
# Afterwards use Boolean indexing to pick out only the odd numbers in the array

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
X = np.arange(25).reshape((5,5))

print(X)
# Use Boolean indexing to pick out only the odd numbers in the array
Y = X[X % 2 != 0]
print(Y)



import numpy as np

# Use Broadcasting to create a 4 x 4 ndarray that has its first
# column full of 1s, its second column full of 2s, its third
# column full of 3s, etc.. 

# Do not change the name of this array. 
# Please don't print anything from your code! The TEST RUN button below will print your array. 


X = np.zeros((4,4)) + np.arange(1,5)
print(X)