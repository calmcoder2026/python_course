# ============================================================
# TOPIC: Dunder (Magic) Methods in Python
# FILE:  dunder_methods.py
# ============================================================

# 1. __init__ - constructor
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book = Book("Python Crash Course", "Eric Matthes", 544)

# 2. __str__ and __repr__
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):        # called by print() - for users
        return f"{self.name} - ${self.price:.2f}"

    def __repr__(self):       # called in REPL - for developers
        return f"Product(name='{self.name}', price={self.price})"

p = Product("Laptop", 999.99)
print(p)          # Output: Laptop - $999.99
print(repr(p))    # Output: Product(name='Laptop', price=999.99)

# 3. __len__
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __len__(self):        # enables len(playlist)
        return len(self.songs)

pl = Playlist("Favorites")
pl.add_song("Song A")
pl.add_song("Song B")
pl.add_song("Song C")
print(len(pl))    # Output: 3

# 4. __add__
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):     # enables money1 + money2
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __str__(self):
        return f"{self.currency} {self.amount:.2f}"

m1 = Money(10.50)
m2 = Money(5.75)
print(m1 + m2)    # Output: USD 16.25

# 5. __eq__ and __lt__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):      # enables ==
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):      # enables <
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(1, 1)
print(p1 == p2)   # Output: True
print(p3 < p1)    # Output: True (p3 closer to origin)

# 6. __contains__
class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __contains__(self, item):  # enables "item in inventory"
        return item in self.items

inv = Inventory()
inv.add("sword")
inv.add("shield")
print("sword" in inv)   # Output: True
print("potion" in inv)  # Output: False

# 7. __enter__ and __exit__ - context manager
class DBConnection:
    def __init__(self, name):
        self.name = name

    def __enter__(self):      # runs at start of with block
        print(f"Connected to {self.name}")
        return self

    def __exit__(self, *args):  # runs at end of with block
        print(f"Disconnected from {self.name}")
        return False

with DBConnection("users_db") as db:
    print(f"Running query on {db.name}")
# Output: Connected / Running query / Disconnected
