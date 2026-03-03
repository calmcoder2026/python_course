# Tuples in Python

## What is a Tuple?
An ordered, immutable collection. Once created it cannot be changed.
Use when data should never be modified.

    coordinates = (40.7128, -74.0060)

## Key Properties
- Ordered: items keep their position
- Immutable: no add, remove, or change after creation
- Allows duplicates
- Faster than lists (Python optimizes immutable objects)
- Can be used as dictionary keys

## Tuple vs List
| Use Case | Tuple | List |
|---|---|---|
| Fixed data | Yes | No |
| Return multiple values | Yes | |
| Dict keys | Yes | No |
| Changing data | No | Yes |

## Real-World Use Cases
- GPS coordinates (lat, lng)
- RGB color values (255, 128, 0)
- Database rows from a query
- Returning multiple values from a function

## Common Mistakes and Tips
| Mistake | Problem | Fix |
|---|---|---|
| t = (1) is not a tuple | (1) is just integer 1 | Use (1,) with trailing comma |
| Modifying a tuple | TypeError | Use a list if you need to modify |

Tip: Tuples signal intent - this data is fixed and should not change.
