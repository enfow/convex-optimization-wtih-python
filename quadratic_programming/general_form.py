"""General Form of Quadratic Programming.

Author
- Name: Kyeongmin Woo
- E-mail: wgm0601@gmail.com

Objective Functions
- Objective Function: (1/2) x^T P x + q^T x
- Constrains:
    - Gx <= h
    - Ax = b

Reference
- cvxpy quadratic program: https://www.cvxpy.org/examples/basic/quadratic_program.html
- cvxpy.quad_form: https://www.cvxpy.org/api_reference/cvxpy.atoms.other_atoms.html#quad-form
"""
import cvxpy as cvx
import numpy as np

np.random.seed(1)

m = 15
n = 10
p = 5

# Generate Random Variable
P = np.random.randn(n, n)
P = P.T @ P  # Positive Definite Matrix P
q = np.random.randn(n)
G = np.random.randn(m, n)
h = G @ np.random.randn(n)
A = np.random.randn(p, n)
b = np.random.randn(p)

# Define Optimization Variable
x = cvx.Variable(n)

# Define Problem
problem = cvx.Problem(
    cvx.Minimize(
        (1/2)*cvx.quad_form(x, P) + q.T @ x
    ), 
    [
        G @ x <= h,
        A @ x == b
    ]
)

problem.solve()

print("Optimial Value: ", problem.value)
print("Solution x: ")
print(x.value)
"""
Optimial Value:  86.89141585569908
Solution x:
    [-1.68244521  0.29769913 -2.38772183 -2.79986015  1.18270433 -0.20911897
     -4.50993526  3.76683701 -0.45770675 -3.78589638]
"""
