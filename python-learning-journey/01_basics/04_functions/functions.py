# ============================================================
# TOPIC: Functions in Python
# FILE:  functions.py
# ============================================================

# 1. BASIC FUNCTION
def greet():
    print("Hello, World!")

greet()                # Output: Hello, World!

# 2. PARAMETERS
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")    # Output: Hello, Alice!
greet_user("Bob")      # Output: Hello, Bob!

# 3. RETURN VALUE
def add(a, b):
    return a + b       # returns result, does not print

result = add(3, 5)
print(result)          # Output: 8

# 4. DEFAULT PARAMETERS
def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}!")

greet_with_title("Smith")           # Output: Hello, Mr. Smith!
greet_with_title("Johnson", "Dr.")  # Output: Hello, Dr. Johnson!

# 5. KEYWORD ARGUMENTS
def describe_pet(name, animal):
    print(f"{name} is a {animal}")

describe_pet(animal="cat", name="Whiskers")  # order does not matter

# 6. *args - any number of positional arguments
def total(*numbers):   # packs all into a tuple
    return sum(numbers)

print(total(1, 2, 3))  # Output: 6
print(total(10, 20))   # Output: 30

# 7. **kwargs - any number of keyword arguments
def show_info(**details):  # packs into a dictionary
    for key, value in details.items():
        print(f"{key}: {value}")

show_info(name="Alice", age=25, city="Mumbai")

# 8. DOCSTRING
def calculate_area(length, width):
    """
    Calculate area of a rectangle.
    Args:
        length (float): The length.
        width (float): The width.
    Returns:
        float: The area.
    """
    return length * width

print(calculate_area(5, 3))  # Output: 15

# 9. LAMBDA - anonymous one-liner
square = lambda x: x ** 2
print(square(4))       # Output: 16

names = ["Charlie", "Alice", "Bob"]
names.sort(key=lambda n: len(n))
print(names)           # Output: ['Bob', 'Alice', 'Charlie']

# 10. RETURN MULTIPLE VALUES
def min_max(numbers):
    return min(numbers), max(numbers)  # returns a tuple

low, high = min_max([3, 1, 4, 1, 5, 9])
print(f"Min: {low}, Max: {high}")  # Output: Min: 1, Max: 9
