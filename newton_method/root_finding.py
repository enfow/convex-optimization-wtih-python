"""Find root of 2 with Newton's Method."""
import math

def F(x: float) -> float:
    return math.pow(x, 2) - 2

def diff_F(x: float) -> float:
    return 2 * x

if __name__ == "__main__":
    ITER = 5
    x: float = 1.
    x_star: float = math.sqrt(2)
    for k in range(ITER):
        print(f"iter: {k} | x: {round(x, 6): 9} | x - x*: {x - x_star}")
        x = x - (1 / diff_F(x)) * F(x)

"""
iter: 0 | x:       1.0 | x - x*: -0.41421356237309515
iter: 1 | x:       1.5 | x - x*: 0.08578643762690485
iter: 2 | x:  1.416667 | x - x*: 0.002453104293571595
iter: 3 | x:  1.414216 | x - x*: 2.1239014147411694e-06
iter: 4 | x:  1.414214 | x - x*: 1.5947243525715749e-12
"""
