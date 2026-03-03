# ============================================================
# TOPIC: while Loop in Python
# FILE:  while_loop.py
# ============================================================

# 1. BASIC while LOOP
count = 0              # initialize before the loop
while count < 5:       # check condition each iteration
    print(count)
    count += 1         # IMPORTANT: update or it runs forever
# Output: 0 1 2 3 4

# 2. ATTEMPT COUNTER example
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    print(f"Attempt {attempts + 1} of {max_attempts}")
    attempts += 1

# 3. INFINITE LOOP with break
number = 1
while True:            # runs forever until break
    print(number)
    number += 1
    if number > 5:
        break          # exit when done
# Output: 1 2 3 4 5

# 4. continue inside while
num = 0
while num < 6:
    num += 1
    if num == 3:
        continue       # skip 3
    print(num)
# Output: 1 2 4 5 6

# 5. else clause
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("Loop ended normally")

# 6. COUNTDOWN
countdown = 5
while countdown > 0:
    print(f"T-minus {countdown}...")
    countdown -= 1
print("Liftoff!")

# 7. NESTED while LOOPS
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
