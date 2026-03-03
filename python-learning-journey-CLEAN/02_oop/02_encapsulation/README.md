# Encapsulation in Python

## What is Encapsulation?
Bundling data and methods together and restricting direct access to internal state.
Protects object data from unintended outside modification.

## Access Levels in Python
Python uses naming conventions (not hard access modifiers):

| Convention | Meaning | Example |
|---|---|---|
| name | Public - accessible anywhere | self.name |
| _name | Protected - internal use by convention | self._salary |
| __name | Private - name-mangled by Python | self.__password |

## The @property Way
Instead of get_x() and set_x() methods, Python uses @property:

    @property
    def name(self):       # getter
        return self._name

    @name.setter
    def name(self, value):  # setter with validation
        if value:
            self._name = value

## Real-World Use Cases
- Bank account: prevent balance going negative
- User profile: validate email format before storing
- Config: make settings read-only after init
- API client: hide auth tokens from direct access

## Common Mistakes and Tips
| Mistake | Problem | Fix |
|---|---|---|
| Accessing __attr directly | AttributeError | Use the public property |
| No validation in setters | Invalid data enters object | Always validate in setters |
| Making everything private | Overengineering | Only protect what truly needs it |

Tip: Python's philosophy is "we are all consenting adults." The _ prefix is a signal, not a lock.
