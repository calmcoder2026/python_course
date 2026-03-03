# ============================================================
# TOPIC: Classes and Objects in Python
# FILE:  classes_objects.py
# ============================================================

# 1. DEFINING A CLASS
class Dog:
    species = "Canis familiaris"  # class attribute - shared by ALL dogs

    def __init__(self, name, age):
        # instance attributes - unique to each Dog object
        self.name = name
        self.age = age

    def bark(self):               # instance method
        return f"{self.name} says: Woof!"

    def describe(self):
        return f"{self.name} is {self.age} year(s) old"

# 2. CREATING OBJECTS
dog1 = Dog("Buddy", 3)           # create first Dog
dog2 = Dog("Max", 5)             # create second - independent

print(dog1.name)      # Output: Buddy
print(dog2.name)      # Output: Max
print(dog1.bark())    # Output: Buddy says: Woof!
print(dog1.species)   # Output: Canis familiaris (class attr)
print(dog2.species)   # Output: Canis familiaris (same!)

# 3. CLASS vs INSTANCE ATTRIBUTES
class Counter:
    count = 0            # class attribute - shared

    def __init__(self, name):
        self.name = name             # instance - unique
        Counter.count += 1          # increment the shared counter

c1 = Counter("First")
c2 = Counter("Second")
print(Counter.count)  # Output: 2 - shared across all
print(c1.name)        # Output: First - unique to c1

# 4. CLASS METHOD and STATIC METHOD
class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):                      # instance method
        return Circle.pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):    # class method - alternate constructor
        return cls(diameter / 2)

    @staticmethod
    def is_valid(radius):                # static method - no self or cls
        return radius > 0

c = Circle(5)
print(c.area())                          # Output: 78.53975
c2 = Circle.from_diameter(10)
print(c2.radius)                         # Output: 5.0
print(Circle.is_valid(-3))              # Output: False

# 5. __str__ and __repr__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):           # called by print() - human-friendly
        return f"Point({self.x}, {self.y})"

    def __repr__(self):          # called in REPL - developer-friendly
        return f"Point(x={self.x}, y={self.y})"

p = Point(3, 4)
print(p)          # Output: Point(3, 4)
print(repr(p))    # Output: Point(x=3, y=4)
