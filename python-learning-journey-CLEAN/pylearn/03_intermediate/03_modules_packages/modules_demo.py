# ============================================================
# TOPIC: Modules and Packages in Python
# FILE:  modules_demo.py
# ============================================================

# 1. STANDARD LIBRARY - math
import math
print(math.sqrt(16))       # Output: 4.0
print(math.pi)             # Output: 3.141592653589793
print(math.ceil(4.2))      # Output: 5

# 2. FROM IMPORT - specific items only
from math import sqrt, factorial
print(sqrt(25))            # Output: 5.0
print(factorial(5))        # Output: 120

# 3. IMPORT WITH ALIAS
import datetime as dt
today = dt.date.today()
print(today)               # Output: current date e.g. 2025-01-15

# 4. os MODULE - operating system operations
import os
print(os.getcwd())         # current working directory
print(os.path.join("folder", "file.txt"))  # safe path building

# 5. random MODULE
import random
print(random.randint(1, 10))        # random int 1-10
print(random.random())              # random float 0-1
print(random.choice(["a","b","c"])) # random item from list

items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)               # shuffled list

# 6. json MODULE - work with JSON data
import json

user = {"name": "Alice", "age": 25, "active": True}
json_string = json.dumps(user, indent=2)   # dict -> JSON string
print(json_string)

parsed = json.loads(json_string)           # JSON string -> dict
print(parsed["name"])      # Output: Alice

# 7. collections - specialized containers
from collections import Counter, defaultdict

words = ["apple","banana","apple","cherry","banana","apple"]
counts = Counter(words)
print(counts)                    # Counter({'apple': 3, ...})
print(counts.most_common(2))     # top 2: [('apple',3),('banana',2)]

word_lengths = defaultdict(list)
for word in words:
    word_lengths[len(word)].append(word)  # group by length
print(dict(word_lengths))

# 8. __name__ == "__main__" pattern
def main():
    print("Running as a script directly")

if __name__ == "__main__":
    main()
# - Running: python modules_demo.py  -> main() runs
# - Importing: import modules_demo   -> main() does NOT run
