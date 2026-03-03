# ============================================================
# TOPIC: for Loop in Python
# FILE:  for_loop.py
# ============================================================

# 1. BASIC for LOOP - iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:   # fruit takes each value one by one
    print(fruit)
# Output: apple / banana / cherry

# 2. for WITH range()
for i in range(5):     # generates 0,1,2,3,4
    print(i)

for i in range(1, 6):  # start=1, stop=6 (exclusive) -> 1,2,3,4,5
    print(i)

for i in range(0, 10, 2):  # step of 2 -> 0,2,4,6,8
    print(i)

# 3. ITERATE OVER A STRING
for char in "Python":  # each character
    print(char)        # Output: P y t h o n

# 4. enumerate() - get index AND value
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"{index}: {color}")
# Output: 0: red / 1: green / 2: blue

for index, color in enumerate(colors, start=1):
    print(f"{index}: {color}")
# Output: 1: red / 2: green / 3: blue

# 5. NESTED for LOOPS
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")

# 6. break - exit early
for num in [1, 2, 3, 4, 5]:
    if num == 3:
        break          # stop at 3
    print(num)
# Output: 1 2

# 7. continue - skip one iteration
for num in range(1, 6):
    if num == 3:
        continue       # skip 3
    print(num)
# Output: 1 2 4 5

# 8. else clause - runs when no break occurred
for num in range(5):
    print(num)
else:
    print("Loop finished normally")

# 9. LIST COMPREHENSION - compact loop
squares = [x**2 for x in range(1, 6)]
print(squares)         # Output: [1, 4, 9, 16, 25]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)           # Output: [0, 2, 4, 6, 8]
