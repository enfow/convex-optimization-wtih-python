"""Diet Program Example for Linear Programming.

- Author: Kyeongmin Woo
- E-mail: wgm0601@gmail.com
- Desc:
    - Minimize costs of all foods that meet nutritional requirements.
    - c_j: cost of the food j.
    - d_i: nutritional requirements for nutrient i.
    - D_{i,j}: degree to which nutrient i in the food j.
    - x_j: amount of food j in the diet.
- Objective function:
    - minimize_x c.T @ x
- Subject 
"""

import cvxpy as cvx
import numpy as np

np.random.seed(1)


# Define size of each variables
I = 5  # 5 nutrients
J = 10  # 10 foods

# Generate Random LP Problem
c = np.random.rand(J)
d = np.random.rand(I)
D = np.random.rand(I, J)

# Define optimization variable
x = cvx.Variable(J)

# Define Problem
problem = cvx.Problem(
    cvx.Minimize(c@x),
    [
        D@x >= d,
        x >= 0,
    ]
)

problem.solve()

print("Optimial Value: ", problem.value)
print("Solution x: ")
print(x.value)
