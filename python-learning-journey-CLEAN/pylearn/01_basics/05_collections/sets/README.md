# Sets in Python

## What is a Set?
An unordered collection of unique items. Automatically removes duplicates.

    my_set = {1, 2, 2, 3}  # becomes {1, 2, 3}

## Key Properties
- Unordered: no index, no guaranteed order
- Mutable: add and remove items
- No duplicates: enforced automatically
- Items must be hashable (no lists or dicts inside)

## Set Math Operations
| Operation | Syntax | Description |
|---|---|---|
| Union | a or b | All items from both |
| Intersection | a and b | Only in both |
| Difference | a - b | In a but not b |
| Symmetric diff | a ^ b | In either but not both |

## Real-World Use Cases
- Remove duplicates from a list of emails
- Find common users across two platforms
- Fast membership check: is this username taken?
- Unique tags across all blog articles

## Common Mistakes and Tips
| Mistake | Problem | Fix |
|---|---|---|
| {} creates a dict not set | type({}) is dict | Use set() for empty set |
| Accessing by index s[0] | Sets have no index | Convert to list first |
| Assuming order | Set order is arbitrary | Use sorted(my_set) if needed |

Tip: Sets are dramatically faster than lists for membership checks.
