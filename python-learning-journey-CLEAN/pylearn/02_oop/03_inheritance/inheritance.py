# ============================================================
# TOPIC: Inheritance in Python
# FILE:  inheritance.py
# ============================================================

# 1. BASIC SINGLE INHERITANCE
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

    def eat(self):
        return f"{self.name} is eating"

class Dog(Animal):           # Dog inherits from Animal
    def fetch(self):         # new method only in Dog
        return f"{self.name} fetches the ball!"

class Cat(Animal):           # Cat also inherits from Animal
    def purr(self):
        return f"{self.name} purrs..."

dog = Dog("Buddy", "Woof")
cat = Cat("Whiskers", "Meow")

print(dog.speak())    # Output: Buddy says Woof  (inherited)
print(dog.eat())      # Output: Buddy is eating  (inherited)
print(dog.fetch())    # Output: Buddy fetches... (own method)
print(cat.speak())    # Output: Whiskers says Meow

# 2. super() - call parent from child
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        return f"{self.brand} - max speed: {self.speed} km/h"

class ElectricCar(Vehicle):
    def __init__(self, brand, speed, battery_range):
        super().__init__(brand, speed)      # call parent first
        self.battery_range = battery_range  # add own attribute

    def describe(self):
        base = super().describe()           # get parent output
        return f"{base} | Range: {self.battery_range} km (Electric)"

car = ElectricCar("Tesla", 250, 500)
print(car.describe())
# Output: Tesla - max speed: 250 km/h | Range: 500 km (Electric)

# 3. METHOD OVERRIDING
class Shape:
    def area(self):
        return 0

    def describe(self):
        return f"Area = {self.area()}"   # uses whichever area() is active

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):          # override parent area()
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):          # override parent area()
        return round(3.14159 * self.r ** 2, 2)

r = Rectangle(4, 5)
c = Circle(7)
print(r.describe())   # Output: Area = 20
print(c.describe())   # Output: Area = 153.94

# 4. MULTI-LEVEL INHERITANCE
class LivingThing:
    def breathe(self):
        return "breathing"

class Animal2(LivingThing):
    def move(self):
        return "moving"

class Bird(Animal2):
    def fly(self):
        return "flying"

eagle = Bird()
print(eagle.breathe())  # from LivingThing (2 levels up)
print(eagle.move())     # from Animal2
print(eagle.fly())      # from Bird

# 5. isinstance and issubclass
print(isinstance(dog, Dog))     # Output: True
print(isinstance(dog, Animal))  # Output: True - Dog is-a Animal
print(issubclass(Dog, Animal))  # Output: True
