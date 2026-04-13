from tool_interface import ToolInterface

class Pitchfork(ToolInterface):
    """
    Реалізація інструмента: Вила.
    Використовується переважно для пухкого ґрунту або перекидання компосту.
    """
    def dig(self, area: str):
        print(f"Вила: Ефективно розпушуємо ґрунт на ділянці '{area}'.")
