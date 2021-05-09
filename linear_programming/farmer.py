"""Farmer Example for Linear Programming.

- Author: Kyeongmin Woo
- E-mail: wgm0601@gmail.com
- Desc:
    - Maximize the farmer's profit.
    - x_1, x_2: land planted with wheat and barley. optimization variable.
    - s_1, s_2: price of the wheat and barley.
    - F_1, F_2: fertilizer the wheat and barley require.
    - P_1, P_2: pesticide the wheat and barley require.
    - L : size of the land.
- Objective function:
    - Maximize s_1 * x_1 + s_2 * x_2
- Constraints:
    - x_1 + x_2 <= L
    - F_1 * x_1 + F_2 * x_2 <= F
    - P_1 * x_1 + P_2 * x_2 <= P
    - x_1 >= 0
    - x_2 >= 0
- Reference:
    - Wiki: https://en.wikipedia.org/wiki/Linear_programming
"""

import cvxpy as cvx
import numpy as np

np.random.seed(1)


# Generate random variables
MAX_LAND = 1000
MAX_FERTILIZER = 100
MAX_PESTICIDE = 100

F1 = 10
F2 = 20

P1 = 15
P2 = 8

S1 = 40
S2 = 30

# Define optimization variable
x_1 = cvx.Variable(1)
x_2 = cvx.Variable(1)

# Define Problem
problem = cvx.Problem(
    cvx.Maximize(S1 * x_1 + S2 * x_2),
    [
        x_1 + x_2 <= MAX_LAND,
        F1 * x_1 + F2 * x_2 <= MAX_FERTILIZER,
        P1 * x_1 + P2 * x_2 <= MAX_PESTICIDE,
        x_1 >= 0,
        x_2 >= 0
    ],
)

problem.solve()

print("Optimial Value: ", problem.value)
print("Solution x: ")
print(x_1.value, x_2.value)
"""
Optimial Value:  286.3636364252908
Solution x:
    [5.45454546] [2.27272727]
"""
