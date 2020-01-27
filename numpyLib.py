import numpy as np

a = [[1,2,3],[4,5,6],[7,8,9]]

b = np.array(a) # Transforming the list into an array

c = np.arange(0,485, 5) # Generating a new array populated

d = np.linspace(0, 50, 10) # Generating a new array with evenly spaces and decimals

e = np.ones((8, 4)) # Generate an array full of ones

f = np.zeros((5, 8)) # Generate an array full of zeros

g = np.random.rand(2, 4) # Generate an array of random positive numbers between 0 and 1

h = np.random.randint(1, 100, 25) # Generate an array of 5 random integer numbers between 1 and 100

i = h.reshape(5, 5) # Transforms the array into the format you expects

var = np.array([5, 8, 11, 9])

j = var.max() # Returns the maximum value of the array

k = var.min() # Returns the minimum value of the array

l = var.argmax() # Returns the index of the maximum value of the array

m = var.argmin() # Returns the index of the minimum value of the array

n = var.shape # Returns the current shape of the array (Note the absence of '()', that's because it's not a function, it's a method)

o = var.dtype # Returns the current array content type