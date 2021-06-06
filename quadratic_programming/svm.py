"""Support Vector Machine Example

Author
- Name: Kyeongmin Woo
- E-mail: wgm0601@gmail.com

Objective Functions
- Objective Function: (1/2) ||beta|| + C * sum(slack)
- Constrains:
    - slack >= 0
    - y(x^T beta + beta_0) >= 1 - slack
"""
import cvxpy as cvx
import numpy as np

from data.svm import X, y


y = 2 * (y - 0.5)  # [0, 1] => [-1, 1]
C = 1
m, n = X.shape

# Define Optimization Problem
beta = cvx.Variable((n,1))
b = cvx.Variable()
slack = cvx.Variable((m,1))

# Define Problem
objective = cvx.Minimize(
    (1/2) * cvx.norm(beta) + C * sum(slack)
)
constrains=[
    cvx.multiply(y, (X @ beta + b)) >= 1 - slack,
    slack >= 0
]
problem = cvx.Problem(objective, constrains)

# Solve
result = problem.solve() 
print(beta.value)
