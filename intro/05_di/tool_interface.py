from abc import ABC, abstractmethod

class ToolInterface(ABC):
    """
    Інтерфейс для інструментів копання.
    Цей клас визначає 'контракт', якому повинні слідувати всі інструменти.
    """
    @abstractmethod
    def dig(self, area: str):
        """
        Метод для копання певної ділянки.
        
        :param area: Назва ділянки, яку треба перекопати.
        """
        pass
