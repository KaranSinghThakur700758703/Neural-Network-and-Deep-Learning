import numpy as np #importing the package for using numpy package
random_vec = np.random.uniform(1, 20, 20)#Generates random vector of size 20
matrix_shape = random_vec.reshape(4, 5)
print("Default Vector of Size 20:")
print(random_vec)
print("\nReshaped Vector for Size 20:")
print(matrix_shape)
max_values = np.max(matrix_shape, axis=1, keepdims=True) #For Calculating the maximum value in each row of the matrix_shape array, retaining the shape as a column vector.
max_value_mask = matrix_shape == max_values # Creating  a boolean mask indicating the positions of maximum values
matrix_shape[max_value_mask] = 0  # After getting the position Replacing those  maximum values with 0 using the mask
print("\n After replacing max values with 0 The Matrix is:")
print(matrix_shape)
