# Classes and Objects in Python

## What are Classes and Objects?
- A class is a blueprint defining structure and behavior
- An object is an instance created from that blueprint

    class Car:       # blueprint
        pass
    my_car = Car()   # object - an actual car

## Anatomy of a Class
    class Dog:
        species = "Canis familiaris"   # class attribute - shared by all

        def __init__(self, name, age): # constructor - runs at creation
            self.name = name           # instance attribute - unique per object
            self.age = age

        def bark(self):                # instance method - behavior
            return f"{self.name} says Woof!"

- __init__: constructor, runs automatically when object is created
- self: refers to the current object instance
- Class attributes: shared across all instances
- Instance attributes: unique to each object

## Real-World Use Cases
- User class to model users in a web app
- BankAccount class with balance and transactions
- Product class for an e-commerce catalog
- APIClient class to encapsulate connection logic

## Common Mistakes and Tips
| Mistake | Problem | Fix |
|---|---|---|
| Forgetting self in method | TypeError: takes 0 args | Always include self as first param |
| Confusing class vs instance attrs | Unintended shared state | Use self.attr for per-object data |

Tip: Think of a class as a cookie cutter and objects as the cookies.
