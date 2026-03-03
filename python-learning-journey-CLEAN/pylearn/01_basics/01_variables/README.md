# Variables in Python

## What is a Variable?
A named container that stores a value in memory. Python determines type automatically (dynamic typing).

## Theory
- Created the moment you assign a value
- Case-sensitive: name and Name are different
- Can be reassigned to a different type at any time

## Naming Rules
| Rule | Good | Bad |
|---|---|---|
| Start with letter or _ | name, _count | 1name |
| No spaces | first_name | first name |
| No special chars | total_price | total@price |
| Not a keyword | user_input | if = 5 |

Convention: use snake_case (PEP 8)

## Real-World Use Cases
- Storing user name, age, email from a form
- Tracking a score in a game loop
- Holding a config value like a file path
- Saving a calculation result to reuse it

## Common Mistakes and Tips
| Mistake | Problem | Fix |
|---|---|---|
| 1name = Ali | Cannot start with number | name1 = Ali |
| Vague names x, y | Unreadable code | Use user_age, item_price |
| list = [1,2,3] | Shadows built-in list() | Avoid built-in names |

Tip: A good variable name makes code self-documenting.
