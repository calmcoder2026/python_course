# ============================================================
# TOPIC: Exception Handling in Python
# FILE:  exception_handling.py
# ============================================================

# 1. BASIC try / except
try:
    result = 10 / 0            # ZeroDivisionError!
except ZeroDivisionError:
    print("Cannot divide by zero")

# 2. CATCHING THE EXCEPTION OBJECT
try:
    number = int("abc")        # ValueError
except ValueError as e:
    print(f"ValueError: {e}")
# Output: ValueError: invalid literal for int()...

# 3. MULTIPLE except BLOCKS
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: division by zero"
    except TypeError:
        return "Error: invalid types"

print(safe_divide(10, 2))      # Output: 5.0
print(safe_divide(10, 0))      # Output: Error: division by zero
print(safe_divide("10", 2))    # Output: Error: invalid types

# 4. else - runs only if NO exception occurred
try:
    x = int("42")
except ValueError:
    print("Conversion failed")
else:
    print(f"Conversion succeeded: {x}")  # runs because no exception

# 5. finally - ALWAYS runs
def read_file(path):
    f = None
    try:
        f = open(path, "r")
        return f.read()
    except FileNotFoundError:
        return f"Not found: {path}"
    finally:
        if f:
            f.close()          # always close the file
        print("Finally ran")   # always prints

print(read_file("doesnotexist.txt"))

# 6. RAISING EXCEPTIONS
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 150:
        raise ValueError(f"Age {age} is out of range")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)

try:
    set_age("twenty")
except TypeError as e:
    print(e)

# 7. CUSTOM EXCEPTION CLASS
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}. Balance is {balance}.")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount

account = BankAccount(500)
try:
    account.withdraw(1000)
except InsufficientFundsError as e:
    print(e)   # Output: Cannot withdraw 1000. Balance is 500.

# 8. EXCEPTION CHAINING
def load_config(filename):
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError as e:
        raise RuntimeError(f"Config load failed: {filename}") from e

try:
    load_config("config.json")
except RuntimeError as e:
    print(e)
