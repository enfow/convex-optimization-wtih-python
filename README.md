# Convex Optimization Examples with CVXPY

## Installation

[cvxpy homepage](<https://www.cvxpy.org/install/>) suggests pip install

```
pip install cvxpy
```

But sometimes it does not works well. Then it will be helpful.

```
pip install -U pip 
pip install -U setuptools
cat requirements.txt | xargs -n 1 pip install
```

Or just make setup.

```
make setup
```

## Contents

### Linear Programming

- [diet.py](<./linear_programming/diet.py>): Minimize costs of all foods that meet nutritional requirements.
- [farmer.py](<./linear_programming/farmer.py>): Maximize the farmer's profit in the limited resorces.

### Quadratic Programming

- [general_form.py](<./quadratic_programming/general_form.py>): General form of QP problem
- [svm.py](<./quadratic_programming/svm.py>): Support Vector Machine exmaple

### Newton's Method

- [root_finding](<./newton_method/root_finding.py>): Find root of 2 with Newton's method.
