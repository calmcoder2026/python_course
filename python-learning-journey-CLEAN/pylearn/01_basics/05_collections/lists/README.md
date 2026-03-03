# Lists in Python

## What is a List?
An ordered, mutable collection that holds any type of item including duplicates.

    my_list = [1, "hello", 3.14, True]

## Key Properties
- Ordered: items keep their insertion position
- Mutable: add, remove, and change items freely
- Indexed: access by position starting at 0
- Allows duplicates

## Key Operations
| Operation | Syntax | Result |
|---|---|---|
| Access | lst[0] | First item |
| Slice | lst[1:3] | Items at index 1 and 2 |
| Append | lst.append(x) | Add to end |
| Insert | lst.insert(i, x) | Add at index i |
| Remove | lst.remove(x) | Remove first x |
| Pop | lst.pop() | Remove and return last |
| Length | len(lst) | Number of items |
| Sort | lst.sort() | Sort in place |

## Real-World Use Cases
- Items in a shopping cart
- Queue of background tasks
- User responses from a form
- Rows of data read from a CSV file

## Common Mistakes and Tips
| Mistake | Problem | Fix |
|---|---|---|
| lst2 = lst1 | Same object, not a copy | lst2 = lst1.copy() |
| remove(x) when x absent | ValueError | Check: if x in lst first |
| append([1,2]) | Adds nested list | Use extend([1,2]) to add individually |

Tip: List comprehensions are the Pythonic way to build and filter lists.
