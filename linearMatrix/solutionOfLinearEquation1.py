# how to solve the equation?
# solution is like below
# x₁ + 2x₂ + 3x₃ = 14
# x₁ - x₂ + 4x₃ = 11
# 2x₁ + 3x₂ - x₃ = 5

# set Ax = y

import numpy as np
from scipy import linalg

A = np.array([[1, 2, 3],
              [1, -1, 4],
              [2, 3, -1]])

y = np.array([14, 11, 5])

x = linalg.solve(A, y)
print(x)
