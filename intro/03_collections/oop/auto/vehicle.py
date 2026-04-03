class Vehicle:
    """Базовый класс транспортного средства"""

    def __init__(self, make, model, engine, wheels):
        self.make = make
        self.model = model
        self.engine = engine  # Ожидается объект класса Engine
        self.wheels = wheels  # Ожидается список объектов класса Wheel

    def display_info(self):
        """Метод для вывода общей информации о ТС"""
        print(f"--- {self.__class__.__name__}: {self.make} {self.model} ---")
        print(f"Двигатель: {self.engine}")
        print(f"Колес: {len(self.wheels)}")
        if self.wheels:
            print(f"Тип колес: {self.wheels[0]}")

    def move(self):
        print(f"{self.make} {self.model} начинает движение.")
