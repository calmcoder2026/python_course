# ============================================================
# TOPIC: Lists in Python
# FILE:  lists.py
# ============================================================

# 1. CREATING A LIST
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
print(numbers)         # Output: [1, 2, 3, 4, 5]

# 2. ACCESSING - zero-based index
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])       # Output: apple   (first)
print(fruits[-1])      # Output: date    (last)
print(fruits[1:3])     # Output: ['banana', 'cherry']

# 3. SLICING
nums = [0,1,2,3,4,5,6,7,8,9]
print(nums[2:5])       # Output: [2, 3, 4]
print(nums[:4])        # Output: [0, 1, 2, 3]
print(nums[6:])        # Output: [6, 7, 8, 9]
print(nums[::2])       # Output: [0, 2, 4, 6, 8] every 2nd
print(nums[::-1])      # Output: [9,8,...,0] reversed

# 4. MODIFYING
colors = ["red", "green", "blue"]
colors[1] = "yellow"      # change item
colors.append("purple")   # add to end
colors.insert(0, "orange")# insert at position 0
colors.extend(["pink"])    # add multiple items
print(colors)

# 5. REMOVING
items = ["a", "b", "c", "d"]
items.remove("c")      # remove by value
print(items)           # Output: ['a', 'b', 'd']
popped = items.pop()   # remove and return last
print(popped)          # Output: d
del items[0]           # delete by index
items.clear()          # remove everything
print(items)           # Output: []

# 6. USEFUL METHODS
n = [3, 1, 4, 1, 5, 9]
print(len(n))          # Output: 6
print(n.count(1))      # Output: 2
print(sum(n))          # Output: 23
print(min(n))          # Output: 1
print(max(n))          # Output: 9
n.sort()
print(n)               # Output: [1, 1, 3, 4, 5, 9]

# 7. COPY - avoid reference bugs
original = [1, 2, 3]
wrong = original           # NOT a copy - same object!
right = original.copy()    # independent copy

wrong.append(99)
print(original)        # Output: [1, 2, 3, 99] - changed!
right.append(100)
print(original)        # Output: [1, 2, 3, 99] - unchanged

# 8. LIST COMPREHENSION
squares = [x**2 for x in range(1, 6)]
print(squares)         # Output: [1, 4, 9, 16, 25]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)           # Output: [0, 2, 4, 6, 8]
