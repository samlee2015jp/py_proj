from re import T
import numpy as np

A = np.array([[1,2,3,4]])
print(A)
print(A.transpose())
print(A.T)

print('--------------')
u = np.array([[1,2,3]]).T
v = np.array([[5,6,7]]).T
print(u + v)

print(3*u)
print('--------------')

u = np.array([1,2,3])
v = np.array([5,6,7])
print(np.dot(u,v))

u = np.array([1,2,3]).T
v = np.array([5,6,7]).T
print(np.dot(u,v))

print('--------------')
