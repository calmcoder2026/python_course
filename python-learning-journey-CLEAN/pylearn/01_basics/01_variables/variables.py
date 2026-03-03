# ============================================================
# TOPIC: Variables in Python
# FILE:  variables.py
# ============================================================

# 1. BASIC ASSIGNMENT
name = "Alice"       # str  - stores text
age = 25              # int  - whole number
height = 5.6          # float - decimal number
is_student = True     # bool - True or False

print(name)           # Output: Alice
print(age)            # Output: 25
print(height)         # Output: 5.6
print(is_student)     # Output: True

# 2. CHECKING TYPE
print(type(name))     # Output: <class str>
print(type(age))      # Output: <class int>

# 3. DYNAMIC TYPING - reassign to a different type
x = 10                # x is integer
x = "hello"          # x is now string - allowed in Python
print(type(x))        # Output: <class str>

# 4. MULTIPLE ASSIGNMENT
a, b, c = 1, 2, 3    # assign three at once
print(a, b, c)        # Output: 1 2 3

p = q = r = 0         # same value to multiple variables
print(p, q, r)        # Output: 0 0 0

# 5. CONSTANTS - ALL_CAPS is convention, not enforced
MAX_RETRIES = 3
PI = 3.14159

# 6. SWAP VARIABLES - Pythonic one-liner
first = "apple"
second = "banana"
first, second = second, first
print(first)          # Output: banana
print(second)         # Output: apple

# 7. DELETE A VARIABLE
temp = "temporary"
del temp              # removes from memory
# print(temp)         # NameError if uncommented
