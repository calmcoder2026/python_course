# Exception Handling in Python

## What is Exception Handling?
Exceptions are runtime errors that interrupt normal program flow.
Exception handling lets you anticipate and respond to errors gracefully.

## Structure
    try:
        # code that might raise an exception
    except SomeException as e:
        # handle that specific exception
    except AnotherException:
        # handle another type
    else:
        # runs ONLY if no exception occurred
    finally:
        # ALWAYS runs - for cleanup code

## Common Built-in Exceptions
| Exception | Cause |
|---|---|
| ValueError | Wrong value/format: int("abc") |
| TypeError | Wrong type: "a" + 1 |
| KeyError | Dict key not found |
| IndexError | List index out of range |
| FileNotFoundError | File does not exist |
| ZeroDivisionError | Division by zero |
| AttributeError | Object has no such attribute |

## Real-World Use Cases
- Catch FileNotFoundError when a config file is missing
- Handle ValueError when parsing form input
- Retry on ConnectionError for network requests
- Roll back a DB transaction in finally block

## Common Mistakes and Tips
| Mistake | Problem | Fix |
|---|---|---|
| except Exception too broadly | Hides bugs | Catch specific exceptions |
| Bare except: | Catches even SystemExit | Always specify exception type |
| Silencing with pass | Error disappears silently | At minimum, log the error |
| Not using finally | Resources left open | Use finally or context managers |

Tip: Catch exceptions where you can actually do something about them.
