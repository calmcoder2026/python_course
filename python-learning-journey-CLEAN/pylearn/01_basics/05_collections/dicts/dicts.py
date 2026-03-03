# ============================================================
# TOPIC: Dictionaries in Python
# FILE:  dicts.py
# ============================================================

# 1. CREATING A DICT
person = {"name": "Alice", "age": 25}
print(person)          # Output: {'name': 'Alice', 'age': 25}

# 2. ACCESSING VALUES
user = {"name": "Bob", "email": "bob@email.com"}
print(user["name"])              # Output: Bob
print(user.get("phone"))         # Output: None - no error
print(user.get("phone", "N/A"))  # Output: N/A - custom default

# 3. ADD AND UPDATE
profile = {"username": "alice99"}
profile["email"] = "alice@x.com"   # add new key
profile["username"] = "alice_2024" # update existing
print(profile)

# 4. REMOVING
data = {"a": 1, "b": 2, "c": 3}
del data["a"]           # delete by key
print(data)             # Output: {'b': 2, 'c': 3}
val = data.pop("b")     # remove and return
print(val)              # Output: 2
data.clear()            # remove everything
print(data)             # Output: {}

# 5. ITERATING
student = {"name": "Charlie", "grade": "A", "score": 95}

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():   # most common
    print(f"{key}: {value}")

# 6. CHECK KEY EXISTS
config = {"debug": True}
if "debug" in config:
    print("Debug:", config["debug"])

# 7. MERGE WITH update()
info = {"x": 1, "y": 2}
info.update({"z": 3, "x": 99})
print(info)   # Output: {'x': 99, 'y': 2, 'z': 3}

# 8. NESTED DICT
company = {"name": "TechCorp", "ceo": {"name": "Diana"}}
print(company["ceo"]["name"])   # Output: Diana

# 9. DICT COMPREHENSION
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1:1, 2:4, 3:9, 4:16, 5:25}
