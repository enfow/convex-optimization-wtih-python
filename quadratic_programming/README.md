# Quadratic Programming

## Contents

### 1. [general form](<./general_form.py>)

- Objective Function
    - (1/2) x^T P x + q^T x
- Constrains:
    - Gx <= h
    - Ax = b

### 2. [Support Vector Machine](<./svm.py>)

- Objective Function
    - (1/2) ||beta|| + C * sum(slack)
- Constrains:
    - slack >= 0
    - y(x^T beta + beta_0) >= 1 - slack
