class Engine:
    """Класс, описывающий двигатель"""

    def __init__(self, power, engine_type):
        self.power = power
        self.engine_type = engine_type

    def __str__(self):
        return f"Двигатель {self.engine_type} (мощность: {self.power} л.с.)"
