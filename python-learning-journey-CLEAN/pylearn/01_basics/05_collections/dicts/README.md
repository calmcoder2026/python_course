# Dictionaries in Python

## What is a Dictionary?
Stores data as key-value pairs.
Like a real dictionary: look up a key to find its value.

    person = {"name": "Alice", "age": 25}

## Key Properties
- Keys must be unique and immutable (str, int, tuple)
- Values can be anything
- Mutable: add, update, delete freely
- Ordered by insertion order (Python 3.7+)

## Key Operations
| Operation | Syntax | Note |
|---|---|---|
| Access | d["key"] | KeyError if missing |
| Safe access | d.get("key") | Returns None if missing |
| Add/Update | d["key"] = val | Creates or updates |
| Delete | del d["key"] | Removes entry |
| All keys | d.keys() | View object |
| All values | d.values() | View object |
| All pairs | d.items() | (key, value) tuples |

## Real-World Use Cases
- User profile: name, email, preferences
- JSON API response data
- Word frequency counter
- Product catalog: ID to product details

## Common Mistakes and Tips
| Mistake | Problem | Fix |
|---|---|---|
| d["missing"] | KeyError | Use d.get("key", default) |
| List as a key | TypeError - unhashable | Use a tuple instead |
| Iterating while modifying | RuntimeError | Use list(d.keys()) first |

Tip: Always use d.get(key, default) when the key might not exist.
