# File Handling in Python

## What is File Handling?
Reading from and writing to files on disk.
Essential for persisting data between program runs.

## File Modes
| Mode | Description |
|---|---|
| r | Read (default) - file must exist |
| w | Write - creates or overwrites |
| a | Append - adds to end of file |
| x | Create - fails if file exists |
| rb / wb | Binary read/write |

## The with Statement
    with open("file.txt", "r") as f:
        content = f.read()
    # file closes automatically - even if an error occurs

Always use with - it guarantees the file is closed properly.

## Real-World Use Cases
- Reading config from a .txt or .json file
- Logging events to a log file
- Writing output data to a CSV for reporting
- Processing large files line-by-line

## Common Mistakes and Tips
| Mistake | Problem | Fix |
|---|---|---|
| Not using with | File may stay open (memory leak) | Always use with open() |
| open("f", "w") on existing file | Overwrites silently | Use "a" or check first |
| read() on huge file | Loads all into RAM | Read line by line instead |
| Hardcoded paths | Breaks on other machines | Use os.path or pathlib |

Tip: Use pathlib.Path for paths - cleaner and works on all OS.
