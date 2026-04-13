from tool_interface import ToolInterface

class GardenService:
    """
    Сервіс для догляду за садом.
    Цей клас демонструє впровадження залежностей (Dependency Injection).
    Він не знає, яким саме інструментом він копає, він знає лише про інтерфейс.
    """
    def __init__(self, tool: ToolInterface):
        """
        Впровадження залежності через конструктор.
        
        :param tool: Об'єкт, що реалізує ToolInterface.
        """
        self.tool = tool

    def prepare_garden(self, garden_name: str):
        """
        Завдання (Job) - підготувати город.
        Виконується за допомогою впровадженого інструмента.
        """
        print(f"--- Процес підготовки городу: {garden_name} ---")
        self.tool.dig(garden_name)
        print("Статус: Город готовий до посадки!\n")
