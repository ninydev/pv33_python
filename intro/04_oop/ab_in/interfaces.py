from abc import ABC, abstractmethod

class HDMI(ABC):
    """
    Інтерфейс HDMI.
    Забезпечує передачу цифрового відеосигналу високої роздільної здатності.
    """
    @abstractmethod
    def hdmi_connection(self):
        """
        Метод для встановлення з'єднання через HDMI.
        """
        pass

class VGA(ABC):
    """
    Інтерфейс VGA.
    Старий аналоговий інтерфейс для передачі відео.
    """
    @abstractmethod
    def vga_connection(self):
        """
        Метод для встановлення з'єднання через VGA.
        """
        pass
