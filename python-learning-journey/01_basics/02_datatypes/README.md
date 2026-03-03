# Data Types in Python

## What are Data Types?
A data type defines what kind of value a variable holds and what operations are allowed on it.

## Core Built-in Types
| Type | Keyword | Example | Mutable |
|---|---|---|---|
| Integer | int | 42 | No |
| Float | float | 3.14 | No |
| String | str | hello | No |
| Boolean | bool | True | No |
| NoneType | None | None | No |
| List | list | [1,2,3] | Yes |
| Dictionary | dict | {key:val} | Yes |
| Tuple | tuple | (1,2,3) | No |
| Set | set | {1,2,3} | Yes |

Mutable = can be changed after creation.

## Type Conversion
- int("42") gives 42
- float(10) gives 10.0
- str(3.14) gives "3.14"
- bool(0) gives False
- bool("hello") gives True

Anything non-zero and non-empty is Truthy.

## Real-World Use Cases
- int: user age, item count, page number
- float: price, temperature, GPS coordinates
- str: names, emails, messages
- bool: login state, feature flags
- None: missing or uninitialized data

## Common Mistakes and Tips
| Mistake | Problem | Fix |
|---|---|---|
| "5" + 5 | Cannot add str and int | int("5") + 5 |
| 0.1 + 0.2 == 0.3 gives False | Float precision issue | Use round() |
| if x == None | Not Pythonic | Use if x is None |
| type(x) == int | Breaks with subclasses | Use isinstance(x, int) |

Tip: Use isinstance() over type() for type checking.
