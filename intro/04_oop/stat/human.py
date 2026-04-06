class Human:

    count = 0

    @staticmethod
    def create_human(name, age):
        if age < 0:
            raise ValueError("Age must be positive")
        return Human(name, age)

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Human.count_people()

    @staticmethod
    def count_people():
        Human.count += 1

