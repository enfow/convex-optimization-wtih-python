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
