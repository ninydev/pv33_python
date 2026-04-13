from tool_interface import ToolInterface

class Cultivator(ToolInterface):
    """
    Реалізація інструмента: Культиватор.
    Механізований інструмент для швидкої підготовки великих площ.
    """
    def dig(self, area: str):
        print(f"Культиватор: Швидко розпушуємо ділянку '{area}' за допомогою фрез.")
