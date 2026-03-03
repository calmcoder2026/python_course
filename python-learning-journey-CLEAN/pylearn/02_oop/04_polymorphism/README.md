# Polymorphism in Python

## What is Polymorphism?
"Many forms" - the same method name works differently depending on the object calling it.

    for shape in [Circle(), Rectangle(), Triangle()]:
        print(shape.area())   # same call, different results

## Two Key Forms

1. Method Overriding (Runtime Polymorphism)
   Child class redefines a method from the parent.

2. Duck Typing
   Python does not care about the type - only whether the object has the method.
   "If it walks like a duck and quacks like a duck, it is a duck."

    def make_sound(animal):    # works with ANY object that has speak()
        print(animal.speak())

## Real-World Use Cases
- render() on Button, Modal, Table - all different implementations
- save() for PDF, CSV, JSON files
- process_payment() for Stripe, PayPal, Crypto
- draw() across shapes in a graphics editor

## Common Mistakes and Tips
| Mistake | Problem | Fix |
|---|---|---|
| Checking type before calling | Breaks duck typing | Trust the interface, not the type |
| Not overriding required methods | Base behavior used by mistake | Use ABC to enforce overriding |

Tip: Polymorphism lets you write code that works with objects you have not even created yet.
