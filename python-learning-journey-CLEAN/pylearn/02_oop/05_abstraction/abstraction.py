# ============================================================
# TOPIC: Abstraction in Python
# FILE:  abstraction.py
# ============================================================

from abc import ABC, abstractmethod

# 1. BASIC ABSTRACT CLASS
class Shape(ABC):               # ABC = cannot instantiate directly
    @abstractmethod
    def area(self):             # every subclass MUST implement this
        pass

    @abstractmethod
    def perimeter(self):        # every subclass MUST implement this
        pass

    def describe(self):         # concrete method - shared for all shapes
        return f"Area={self.area():.2f}, Perimeter={self.perimeter():.2f}"

# s = Shape()                   # TypeError if uncommented - cannot instantiate

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):             # MUST implement
        return 3.14159 * self.radius ** 2

    def perimeter(self):        # MUST implement
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

c = Circle(5)
r = Rectangle(4, 6)
print(c.describe())   # Output: Area=78.54, Perimeter=31.42
print(r.describe())   # Output: Area=24.00, Perimeter=20.00

# 2. REAL-WORLD - database connectors
class DatabaseConnector(ABC):
    @abstractmethod
    def connect(self): pass

    @abstractmethod
    def execute(self, query): pass

    @abstractmethod
    def close(self): pass

class MySQLConnector(DatabaseConnector):
    def connect(self):
        return "Connected to MySQL"

    def execute(self, query):
        return f"MySQL: {query}"

    def close(self):
        return "MySQL closed"

class SQLiteConnector(DatabaseConnector):
    def connect(self):
        return "Connected to SQLite"

    def execute(self, query):
        return f"SQLite: {query}"

    def close(self):
        return "SQLite closed"

def run_query(db, query):
    print(db.connect())
    print(db.execute(query))
    print(db.close())

run_query(MySQLConnector(), "SELECT * FROM users")
run_query(SQLiteConnector(), "SELECT * FROM products")

# 3. NOTIFICATIONS example
class Notification(ABC):
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    @abstractmethod
    def send(self): pass

    def log(self):              # shared concrete method
        print(f"[LOG] To {self.recipient}: {self.message}")

class EmailNotification(Notification):
    def send(self):
        self.log()
        return f"Email sent to {self.recipient}"

class SMSNotification(Notification):
    def send(self):
        self.log()
        return f"SMS sent to {self.recipient}"

for n in [EmailNotification("a@x.com", "Welcome!"), SMSNotification("+91-9999", "OTP: 1234")]:
    print(n.send())
