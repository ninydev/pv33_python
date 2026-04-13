from tool_interface import ToolInterface

class Shovel(ToolInterface):
    """
    Реалізація інструмента: Лопата.
    Класичний інструмент для глибокого перекопування.
    """
    def dig(self, area: str):
        print(f"Лопата: Перекопуємо ділянку '{area}', перевертаючи великі пласти землі.")
