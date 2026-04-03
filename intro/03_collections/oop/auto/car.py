from vehicle import Vehicle

class Car(Vehicle):
    """Класс легкового автомобиля (наследник Vehicle)"""

    def __init__(self, make, model, engine, wheels, body_style):
        super().__init__(make, model, engine, wheels)
        self.body_style = body_style

    def display_info(self):
        super().display_info()
        print(f"Тип кузова: {self.body_style}")
