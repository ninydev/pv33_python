from vehicle import Vehicle

class Truck(Vehicle):
    """Класс грузового автомобиля (наследник Vehicle)"""

    def __init__(self, make, model, engine, wheels, load_capacity):
        super().__init__(make, model, engine, wheels)
        self.load_capacity = load_capacity

    def display_info(self):
        super().display_info()
        print(f"Грузоподъемность: {self.load_capacity} тонн")
