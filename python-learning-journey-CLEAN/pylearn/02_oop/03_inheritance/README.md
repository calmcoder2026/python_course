# Inheritance in Python

## What is Inheritance?
A class (child) acquires attributes and methods from another class (parent).
Promotes code reuse and establishes a logical hierarchy.

    class Animal:             # Parent
        def breathe(self):
            return "breathing"

    class Dog(Animal):        # Child inherits from Animal
        def bark(self):
            return "Woof!"

    d = Dog()
    d.breathe()   # inherited from Animal
    d.bark()      # defined in Dog

## Key Terms
| Term | Description |
|---|---|
| Parent / Base class | The class being inherited from |
| Child / Derived class | The class that inherits |
| super() | Access the parent from child |
| Method overriding | Child redefines a parent method |

## Types of Inheritance
- Single: one parent, one child
- Multi-level: A -> B -> C chain
- Multiple: child inherits from multiple parents

## Real-World Use Cases
- Vehicle -> Car, Truck, Motorcycle
- User -> AdminUser, GuestUser
- Shape -> Circle, Rectangle, Triangle

## Common Mistakes and Tips
| Mistake | Problem | Fix |
|---|---|---|
| Not calling super().__init__() | Parent attributes not set | Always call super().__init__() first |
| Too deep inheritance chains | Hard to trace | Prefer composition for "has-a" |

Tip: Use inheritance for "is-a" relationships. A Car IS-A Vehicle.
Use composition for "has-a". A Car HAS-A Engine.
