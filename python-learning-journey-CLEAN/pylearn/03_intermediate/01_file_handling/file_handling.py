# ============================================================
# TOPIC: File Handling in Python
# FILE:  file_handling.py
# ============================================================

import os

# 1. WRITING A FILE - "w" creates or overwrites
with open("demo.txt", "w") as f:   # "with" ensures file closes after block
    f.write("Hello, World!\n")     # write first line
    f.write("Python file handling\n")
    f.write("Line three\n")
print("File written")

# 2. READING ENTIRE FILE
with open("demo.txt", "r") as f:
    content = f.read()             # reads entire file as one string
print("Full content:")
print(content)

# 3. READ LINE BY LINE - memory efficient
with open("demo.txt", "r") as f:
    for line in f:                 # iterate line by line
        print(line.strip())        # strip() removes trailing newline

# 4. READ ALL LINES INTO A LIST
with open("demo.txt", "r") as f:
    lines = f.readlines()          # list of all lines with newlines
print(f"Total lines: {len(lines)}")

# 5. APPENDING - "a" adds to end, does NOT overwrite
with open("demo.txt", "a") as f:
    f.write("This was appended\n")

# 6. CHECK IF FILE EXISTS before operating
if os.path.exists("demo.txt"):
    print(f"File exists, size: {os.path.getsize('demo.txt')} bytes")
else:
    print("File not found")

# 7. WRITE MULTIPLE LINES AT ONCE
data = ["Alice,25,Engineer\n", "Bob,30,Designer\n"]
with open("users.txt", "w") as f:
    f.writelines(data)             # writes all strings in the list

# 8. SEEK - move cursor to specific position
with open("demo.txt", "r") as f:
    print(f.tell())                # Output: 0 (start)
    f.read(5)                      # read 5 chars
    print(f.tell())                # Output: 5 (moved)
    f.seek(0)                      # go back to start
    first = f.readline().strip()
    print(first)

# 9. WRITE AND READ CSV manually
with open("scores.csv", "w") as f:
    f.write("name,score,grade\n")
    f.write("Alice,92,A\n")
    f.write("Bob,78,B\n")

with open("scores.csv", "r") as f:
    header = f.readline().strip()
    print("Header:", header)
    for line in f:
        name, score, grade = line.strip().split(",")
        print(f"{name}: {score} ({grade})")

# 10. CLEANUP demo files
for fname in ["demo.txt", "users.txt", "scores.csv"]:
    if os.path.exists(fname):
        os.remove(fname)
print("Demo files cleaned up")
