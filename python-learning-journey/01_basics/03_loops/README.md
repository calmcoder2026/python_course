# Loops in Python

## What are Loops?
Loops let you repeat a block of code multiple times without writing it manually.

## for Loop
Used when iterating over a sequence or repeating a fixed number of times.

    for item in sequence:
        do something

## while Loop
Used when repeating as long as a condition is True.

    while condition:
        do something
        update the condition

## Loop Control Statements
| Statement | Purpose |
|---|---|
| break | Exit the loop immediately |
| continue | Skip current iteration |
| else | Runs after normal loop completion |
| pass | Placeholder, does nothing |

## Real-World Use Cases
- for: process every cart item, read file lines
- while: keep prompting until valid input given
- break: stop searching once match found
- continue: skip invalid records in data

## Common Mistakes and Tips
| Mistake | Problem | Fix |
|---|---|---|
| while True with no break | Infinite loop | Always add a break condition |
| Modify list while looping | Skips items | Loop over a copy: list[:] |
| range(5) expecting 1-5 | Gives 0-4 not 1-5 | Use range(1, 6) |
| Forgetting to increment in while | Infinite loop | Always update the variable |

Tip: Prefer for loops when possible - safer and more Pythonic.
