from abc import ABC, abstractmethod

class Monitor(ABC):
    """
    Абстрактний базовий клас для всіх моніторів.
    Кожен монітор повинен мати спосіб приймати відеосигнал.
    """
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def receive_video_stream(self, data):
        """
        Метод для прийняття відеопотоку.
        У нащадках має бути реалізована логіка відображення.
        """
        pass

class Computer(ABC):
    """
    Абстрактний базовий клас для комп'ютерів та ноутбуків.
    Кожен комп'ютер повинен вміти передавати відеосигнал.
    """
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def send_video_stream(self):
        """
        Метод для передачі відеопотоку.
        У нащадках має бути реалізована логіка генерації сигналу.
        """
        pass
