# Linear Programming

## Contents

1. [farmer.py](<./farmer.py>)

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
