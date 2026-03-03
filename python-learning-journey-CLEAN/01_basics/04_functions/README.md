# Functions in Python

## What is a Function?
A named, reusable block of code that performs a specific task.
Define once, call as many times as needed.

## Syntax
    def function_name(parameters):
        # code body
        return value

- def: keyword that starts the definition
- parameters: inputs the function accepts
- return: output the function gives back (None if omitted)
- docstring: optional description - always include it

## Types of Arguments
| Type | Example | Description |
|---|---|---|
| Positional | greet("Alice") | Matched by position |
| Keyword | greet(name="Alice") | Matched by name |
| Default | def greet(name="User") | Used if not provided |
| *args | def total(*nums) | Any number of positional |
| **kwargs | def info(**data) | Any number of keyword |

## Real-World Use Cases
- Validate user input before saving to database
- Calculate shipping cost by weight and distance
- Format data before showing in UI
- Wrap API call logic for reuse

## Common Mistakes and Tips
| Mistake | Problem | Fix |
|---|---|---|
| def f(lst=[]) mutable default | Shared across calls | def f(lst=None) then lst = lst or [] |
| Not returning a value | Returns None silently | Explicitly return what you need |
| Function does too much | Hard to test | One function = one clear task |

Tip: If you need the word "and" to describe what a function does, split it into two.
