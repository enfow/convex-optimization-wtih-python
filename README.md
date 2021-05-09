# Convex Optimization with PYTHON

## Installation

[cvxpy homepage](<https://www.cvxpy.org/install/>) suggests pip install

```
pip install cvxpy
```

But sometimes it does not works well. Then I recommends below commands.

```
pip install -U pip 
pip install -U setuptools
cat requirements.txt | xargs -n 1 pip install
```

Or just make setup

```
make setup
```

## Contents

### Linear Programming

- [diet.py](<https://github.com/enfow/convex-opt-python/blob/master/linear_programming/diet.py>): Minimize costs of all foods that meet nutritional requirements.
- [farmer.py](<https://github.com/enfow/convex-opt-python/blob/master/linear_programming/farmer.py>): Maximize the farmer's profit in the limited resorces.
