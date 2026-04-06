from human import Human


a =  Human("Alice", 30)
b = Human("Bob", 25)

c: Human = Human.create_human("Charlie", 35)
d: Human = Human.create_human("David", 40)

try:
    e: Human = Human.create_human("Eva", -40)
except ValueError as e:
    print(f"Invalid age: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


print(Human.count)