# ============================================================
# TOPIC: Sets in Python
# FILE:  sets.py
# ============================================================

# 1. CREATING A SET
empty_set = set()            # empty set - NOT {} (that is a dict!)
numbers = {1, 2, 3, 4, 5}
with_dupes = {1, 2, 2, 3, 3}   # duplicates auto-removed
print(with_dupes)     # Output: {1, 2, 3}

# 2. FROM LIST - remove duplicates
emails = ["a@x.com", "b@x.com", "a@x.com"]
unique = set(emails)
print(unique)         # Output: {'a@x.com', 'b@x.com'}

# 3. ADD AND REMOVE
fruits = {"apple", "banana"}
fruits.add("cherry")         # add item
fruits.add("apple")          # no effect - already exists
fruits.remove("banana")      # remove - KeyError if absent
fruits.discard("mango")      # remove - NO error if absent
print(fruits)

# 4. MEMBERSHIP TEST - O(1) speed
valid_users = {"alice", "bob", "charlie"}
print("alice" in valid_users)   # Output: True
print("dave" in valid_users)    # Output: False

# 5. SET OPERATIONS
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a | b)   # UNION:            {1,2,3,4,5,6,7,8}
print(a & b)   # INTERSECTION:     {4, 5}
print(a - b)   # DIFFERENCE (a-b): {1, 2, 3}
print(b - a)   # DIFFERENCE (b-a): {6, 7, 8}
print(a ^ b)   # SYMMETRIC DIFF:   {1,2,3,6,7,8}

# 6. COMPARISON
x = {1, 2, 3}
y = {1, 2, 3, 4, 5}
print(x.issubset(y))         # Output: True
print(y.issuperset(x))       # Output: True

# 7. ITERATING
tags = {"python", "oop", "backend"}
for tag in sorted(tags):
    print(tag)
