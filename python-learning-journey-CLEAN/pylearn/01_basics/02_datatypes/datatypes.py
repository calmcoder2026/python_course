# ============================================================
# TOPIC: Data Types in Python
# FILE:  datatypes.py
# ============================================================

# 1. INTEGER
age = 25
temperature = -10
big = 1_000_000        # underscores improve readability

print(type(age))       # Output: <class 'int'>
print(big)             # Output: 1000000

# 2. FLOAT
price = 9.99
print(type(price))     # Output: <class 'float'>

# Float precision - important to know!
print(0.1 + 0.2)       # Output: 0.30000000000000004
print(round(0.1 + 0.2, 2))  # Output: 0.3

# 3. STRING
name = "Alice"
print(len(name))       # Output: 5
print(name.upper())    # Output: ALICE
print(name[0])         # Output: A

# 4. BOOLEAN
is_active = True
print(type(is_active)) # Output: <class 'bool'>
print(int(True))       # Output: 1
print(int(False))      # Output: 0

# 5. NONE
result = None
print(result)          # Output: None
print(result is None)  # Output: True (correct way to check)

# 6. TYPE CONVERSION
num_str = "42"
num_int = int(num_str)
print(num_int + 8)     # Output: 50

x = float(10)
print(x)               # Output: 10.0

age_str = str(25)
print("Age: " + age_str)  # Output: Age: 25

# 7. TRUTHY AND FALSY
print(bool(0))         # Output: False
print(bool(""))        # Output: False
print(bool([]))        # Output: False
print(bool(42))        # Output: True
print(bool("hi"))      # Output: True

# 8. TYPE CHECKING
value = 3.14
print(isinstance(value, float))         # Output: True
print(isinstance(value, (int, float)))  # Output: True
