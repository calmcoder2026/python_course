# ============================================================
# TOPIC: Polymorphism in Python
# FILE:  polymorphism.py
# ============================================================

# 1. METHOD OVERRIDING - same method, different behavior
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):      # override - Dog-specific
        return "Woof!"

class Cat(Animal):
    def speak(self):      # override - Cat-specific
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

# Same interface (speak) - different output for each type
animals = [Dog(), Cat(), Duck(), Animal()]
for animal in animals:
    print(animal.speak())
# Output: Woof! / Meow! / Quack! / Some generic sound

# 2. POLYMORPHIC FUNCTION - works with any object that has speak()
def make_it_speak(creature):
    print(creature.speak())   # no type checking needed

make_it_speak(Dog())          # Output: Woof!
make_it_speak(Cat())          # Output: Meow!

# 3. DUCK TYPING - no inheritance required
class Robot:
    def speak(self):           # NOT related to Animal
        return "Beep boop"

class Parrot:
    def speak(self):
        return "Polly wants a cracker"

for entity in [Dog(), Robot(), Parrot()]:
    make_it_speak(entity)     # all work because they have speak()

# 4. OPERATOR OVERLOADING - operators behave differently per type
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # defines + behavior
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2               # calls __add__
print(v3)                  # Output: Vector(4, 6)

# Python's + is already polymorphic:
print(1 + 2)               # int addition
print("hello" + " world")  # string concatenation
print([1,2] + [3,4])       # list join

# 5. REAL-WORLD - payment processors
class StripePayment:
    def process(self, amount):
        return f"Stripe: charged ${amount}"

class PayPalPayment:
    def process(self, amount):
        return f"PayPal: sent ${amount}"

def checkout(method, amount):
    print(method.process(amount))  # works with any processor

checkout(StripePayment(), 99.99)
checkout(PayPalPayment(), 49.00)
