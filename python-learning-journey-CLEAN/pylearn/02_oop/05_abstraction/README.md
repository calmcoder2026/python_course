# Abstraction in Python

## What is Abstraction?
Hiding implementation details and exposing only what is necessary.
Defines a contract - what a class MUST do, without specifying HOW.

    from abc import ABC, abstractmethod

    class Shape(ABC):
        @abstractmethod
        def area(self):    # every Shape MUST implement area()
            pass

## Theory
- Import ABC and abstractmethod from the abc module
- A class with @abstractmethod cannot be instantiated directly
- Any subclass MUST implement all abstract methods
- Enforces a consistent interface across all subclasses

## Abstract vs Concrete
| Type | Description |
|---|---|
| Abstract class | Blueprint - cannot instantiate directly |
| Concrete class | Implements all abstract methods - can instantiate |
| Abstract method | Must be overridden in every subclass |

## Real-World Use Cases
- DatabaseConnector: MySQL, PostgreSQL, SQLite must all implement connect(), query(), close()
- Notification: Email, SMS, Push must all implement send()
- Plugin system: enforce what every plugin must provide
- Django View, Model base classes

## Common Mistakes and Tips
| Mistake | Problem | Fix |
|---|---|---|
| Instantiating abstract class | TypeError | Only instantiate concrete subclasses |
| Not implementing all abstract methods | TypeError on create | Implement every @abstractmethod |

Tip: Abstraction answers: "What must every X be able to do?" without caring how.
