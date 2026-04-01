from itertools import zip_longest

ids = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie", "Dave"]
addresses = ["123 Main St", "456 Elm St", "789 Oak St"]

print("Using zip:")
for user_id, name, apt in zip(ids, names, addresses):
    print(f"ID: {user_id}, Name: {name}, Address: {apt}")

print("\nUsing zip_longest with fillvalue:")
for user_id, name, apt in zip_longest(ids, names, addresses, fillvalue="No Address"):
    print(f"ID: {user_id}, Name: {name}, Address: {apt}")