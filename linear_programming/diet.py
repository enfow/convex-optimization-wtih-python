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
- Constraints:
    - Dx >= d
    - x >= 0
"""

import cvxpy as cvx
import numpy as np

np.random.seed(1)


# Define size of each variables
NUM_NUTRIENTS = 5  # 5 nutrients
NUM_FOODS = 10  # 10 foods

# Generate random variables
c = np.random.rand(NUM_FOODS)
d = np.random.rand(NUM_NUTRIENTS)
D = np.random.rand(NUM_NUTRIENTS, NUM_FOODS)

# Define optimization variable
x = cvx.Variable(NUM_FOODS)

# Define Problem
problem = cvx.Problem(
    cvx.Minimize(c @ x),
    [
        D @ x >= d,
        x >= 0,
    ],
)

problem.solve()

print("Optimial Value: ", problem.value)
print("Solution x: ")
print(x.value)
"""
Optimial Value:  0.002006716889300396
Solution x:
    [5.65462476e-11 6.06350359e-11 1.75450878e+01 2.46768995e-10
      1.61126275e-09 1.60536902e-09 3.35914284e-10 3.85801841e-11
      1.15011075e-10 5.30695339e-11]
"""
