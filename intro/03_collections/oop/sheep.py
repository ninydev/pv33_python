class Sheep:
    """Это класс - общая идея того, что такое барашек"""

    def __init__(self, name, weight):
        # Состояние объекта (его характеристики)
        self.name = name
        self.weight = weight

    def say_beee(self):
        # Поведение объекта
        print(f"{self.name} говорит: Бееее!")