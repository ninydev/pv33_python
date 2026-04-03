class Wheel:
    """Класс, описывающий колесо"""

    def __init__(self, brand, diameter):
        self.brand = brand
        self.diameter = diameter

    def __str__(self):
        return f"Колесо {self.brand} (диаметр: {self.diameter}\")"
