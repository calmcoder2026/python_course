# Modules and Packages in Python

## What are Modules and Packages?
- A module is a single .py file containing reusable code
- A package is a folder of modules with an __init__.py file
- The standard library is Python's built-in collection of modules

## Importing
    import math                    # import whole module
    from math import sqrt          # import specific item
    from math import sqrt as sq    # with alias
    import os, sys                 # import multiple

## Creating Your Own Module
Any .py file is a module. In utils.py:
    def add(a, b):
        return a + b

Import it:
    from utils import add

## Package Structure
    my_package/
        __init__.py     <- makes this folder a package
        module1.py
        module2.py

## Useful Standard Library Modules
- os: file and directory operations
- json: parse and create JSON
- datetime: dates, times, formatting
- random: generate random data
- re: regular expressions
- collections: Counter, defaultdict, deque

## Common Mistakes and Tips
| Mistake | Problem | Fix |
|---|---|---|
| import * | Pollutes namespace | Always import specifically |
| Circular imports | ImportError | Restructure to avoid cycles |
| Missing __init__.py | Not a package | Add it (can be empty) |

Tip: Use if __name__ == "__main__": to make a file runnable as script AND importable as module.
