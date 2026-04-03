from vehicle import Vehicle

class Bus(Vehicle):
    """Класс автобуса (наследник Vehicle)"""

    def __init__(self, make, model, engine, wheels, passenger_capacity):
        super().__init__(make, model, engine, wheels)
        self.passenger_capacity = passenger_capacity

    def display_info(self):
        super().display_info()
        print(f"Вместимость пассажиров: {self.passenger_capacity} чел.")
