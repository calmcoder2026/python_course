# ============================================================
# TOPIC: Encapsulation in Python
# FILE:  encapsulation.py
# ============================================================

# 1. PUBLIC, PROTECTED, PRIVATE conventions
class Employee:
    def __init__(self, name, salary, password):
        self.name = name            # public   - fine to access
        self._salary = salary       # protected - convention: internal use
        self.__password = password  # private  - name-mangled

emp = Employee("Alice", 70000, "secret")
print(emp.name)              # Output: Alice
print(emp._salary)           # Works but violates convention
# print(emp.__password)      # AttributeError!
print(emp._Employee__password)  # Can still reach it if you know the trick

# 2. GETTER AND SETTER METHODS
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private

    def get_balance(self):         # getter
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Amount must be positive")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        elif amount <= 0:
            print("Amount must be positive")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")

account = BankAccount("Alice", 1000)
print(account.get_balance())   # Output: 1000
account.deposit(500)
account.withdraw(2000)         # Output: Insufficient funds

# 3. @property - Pythonic getters and setters
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):              # getter - called like obj.name
        return self._name

    @name.setter
    def name(self, value):       # setter - called like obj.name = "Bob"
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value.strip()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0 or value > 150:
            raise ValueError("Age must be between 0 and 150")
        self._age = value

    @property
    def info(self):              # read-only property - no setter
        return f"{self._name}, age {self._age}"

p = Person("Alice", 25)
print(p.name)   # Output: Alice
p.name = "Bob"  # triggers setter
p.age = 30
print(p.info)   # Output: Bob, age 30

try:
    p.age = -5
except ValueError as e:
    print(e)    # Output: Age must be between 0 and 150
