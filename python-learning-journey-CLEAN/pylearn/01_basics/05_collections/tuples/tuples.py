# ============================================================
# TOPIC: Tuples in Python
# FILE:  tuples.py
# ============================================================

# 1. CREATING A TUPLE
empty = ()
single = (42,)         # trailing comma REQUIRED for single item
not_a_tuple = (42)     # this is just the integer 42!

print(type(single))    # Output: <class 'tuple'>
print(type(not_a_tuple))  # Output: <class 'int'>

# 2. ACCESSING
colors = ("red", "green", "blue", "yellow")
print(colors[0])       # Output: red (first)
print(colors[-1])      # Output: yellow (last)
print(colors[1:3])     # Output: ('green', 'blue')

# 3. IMMUTABILITY
point = (10, 20)
# point[0] = 99        # TypeError! Cannot modify
print(point)           # Output: (10, 20)

point = (99, 20)       # reassigning the variable is OK
print(point)

# 4. UNPACKING
lat, lng = (40.7128, -74.0060)
print(f"Lat: {lat}, Lng: {lng}")

first, *rest = (1, 2, 3, 4, 5)
print(first)           # Output: 1
print(rest)            # Output: [2, 3, 4, 5]

a, b = 10, 20
a, b = b, a            # Pythonic swap
print(a, b)            # Output: 20 10

# 5. METHODS (only two because immutable)
nums = (1, 2, 3, 2, 4, 2)
print(nums.count(2))   # Output: 3
print(nums.index(3))   # Output: 2
print(len(nums))       # Output: 6

# 6. AS DICT KEY (lists cannot do this)
locations = {}
locations[(40.7, -74.0)] = "New York"
print(locations[(40.7, -74.0)])   # Output: New York

# 7. CONVERT BETWEEN TUPLE AND LIST
my_tuple = (1, 2, 3)
as_list = list(my_tuple)
as_list.append(4)
back = tuple(as_list)
print(back)            # Output: (1, 2, 3, 4)
