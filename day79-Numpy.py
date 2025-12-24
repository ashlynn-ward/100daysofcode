#Numpy Practice
#Ashlynn Ward, September 3, 2025
#This program was copied from my Google Colab Notebook. It shows the practice I completed to learn the basics of Numpy.

# Import Statements

import numpy as np
from numpy.random import random

import matplotlib.pyplot as plt
from scipy import misc # contains an image of a racoon!
from PIL import Image # for reading image files

# Understanding NumPy's ndarray

#### 1-Dimensional Arrays (Vectors)

my_array = np.array([1.1, 9.2, 8.1, 4.7])
my_array.shape

my_array[2]
my_array.ndim

#### 2-Dimensional Arrays (Matrices)

array_2d = np.array([[1, 2, 3, 9], 
                     [5, 6, 7, 8]])

print(f'array_2d has {array_2d.ndim} dimensions')
print(f'Its shape is {array_2d.shape}')
print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
print(array_2d)

array_2d[1,2]

#### N-Dimensional Arrays (Tensors)

mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                        
                         [[7, 86, 6, 98],
                          [5, 1, 0, 4]],
                          
                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])

# Note all the square brackets!

mystery_array.ndim

mystery_array.shape

mystery_array[2,1,3]

mystery_array[2,1,:]

mystery_array[:,:,0]

# NumPy Mini-Challenges

#### **Challenge 1**: Use [`.arange()`](https://numpy.org/devdocs/reference/generated/numpy.arange.html)to createa a vector `a` with values ranging from 10 to 29. You should get this:

a = np.arange(10,30)
print(a)

#### **Challenge 2**: Use Python slicing techniques on `a` to:

print(a[-3:])
print(a[3:6])
print(a[12:])
print(a[1::2])

#### **Challenge 3**:Reverse the order of the values in `a`, so that the first element comes last:

np.flip(a)

#### **Challenge 4**: Print out all the indices of the non-zero elements in this array: [6,0,9,0,0,5,0]

b = np.array([6,0,9,0,0,5,0])
np.nonzero(b)

#### **Challenge 5**: Use NumPy to generate a 3x3x3 array with random numbers

z = random((3,3,3))
print(z)

#### **Challenge 6**: Use [`.linspace()`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) to create a vector `x` of size 9 with values spaced out evenly between 0 to 100 (both included).

x = np.linspace(0,100,9)
print(x)

#### **Challenge 7**: Use [`.linspace()`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) to create another vector `y` of size 9 with values between -3 to 3 (both included). Then plot `x` and `y` on a line chart using Matplotlib.

y = np.linspace(-3,3,9)
plt.plot(x,y)

#### **Challenge 8**: Use NumPy to generate an array called `noise` with shape 128x128x3 that has random values. Then use Matplotlib's [`.imshow()`](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html) to display the array as an image. 

noise = np.random.random((128,128,3))
plt.imshow(noise)

# Linear Algebra with Vectors

v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])

# Python Lists vs ndarrays
list1 = [4, 5, 2, 7]
list2 = [2, 1, 3, 3]

# Broadcasting and Scalars


a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])
 
b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

# Matrix Multiplication with @ and .matmul()

a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

print(f'{a1.shape}: a has {a1.shape[0]} rows and {a1.shape[1]} columns.')
print(f'{b1.shape}: b has {b1.shape[0]} rows and {b1.shape[1]} columns.')
print('Dimensions of result: (4x2)*(2x3)=(4x3)')

c=np.matmul(a1,b1)
print(c)

# Manipulating Images as ndarrays

# Use your Own Image!

file_name = 'yummy_macarons.jpg'
img_array = np.array(Image.open(file_name))

plt.imshow(Image.open(file_name))

#### Use PIL to open 

plt.imshow(255-img_array)

