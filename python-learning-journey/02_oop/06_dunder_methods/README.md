# Dunder (Magic) Methods in Python

## What are Dunder Methods?
Dunder = Double Underscore. Special methods like __init__, __str__, __len__
that Python calls automatically in specific situations.
They let custom classes behave like built-in types.

## Common Dunder Methods
| Method | When Called | Use |
|---|---|---|
| __init__ | Object creation | Constructor |
| __str__ | print(obj) | Human-readable string |
| __repr__ | repr(obj) in REPL | Dev-friendly string |
| __len__ | len(obj) | Custom length |
| __add__ | obj1 + obj2 | Operator overloading |
| __eq__ | obj1 == obj2 | Equality comparison |
| __lt__ | obj1 < obj2 | Less-than comparison |
| __contains__ | x in obj | Membership test |
| __iter__ | for x in obj | Iteration support |
| __enter__ / __exit__ | with obj: | Context manager |

## Real-World Use Cases
- __str__ on User class for clean log output
- __eq__ on Product to compare by ID not memory address
- __len__ on Playlist to return song count
- __add__ on Money class for currency arithmetic
- __enter__/__exit__ for DB connection context managers

## Common Mistakes and Tips
| Mistake | Problem | Fix |
|---|---|---|
| Not implementing __repr__ | Hard to debug in REPL | Always implement both __str__ and __repr__ |
| Returning non-string from __str__ | TypeError | Always return a str |
| Defining __eq__ without __hash__ | Cannot use in sets or dicts | Define __hash__ alongside __eq__ |

Tip: A good __repr__ lets you copy-paste its output to recreate the object.
