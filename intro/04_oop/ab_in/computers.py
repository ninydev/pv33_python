from base import Computer
from interfaces import HDMI, VGA

class MacBook(Computer, HDMI):
    """
    Сучасний ноутбук з підтримкою HDMI.
    """
    def hdmi_connection(self):
        return "HDMI сигнал готовий"

    def send_video_stream(self):
        signal = f"Відеопотік з {self.model} (4K)"
        print(f"{self.model}: {self.hdmi_connection()} -> Надсилаю: {signal}")
        return signal

class OldPCLaptop(Computer, VGA):
    """
    Старий ноутбук, який має тільки VGA вихід.
    """
    def vga_connection(self):
        return "VGA сигнал (аналоговий)"

    def send_video_stream(self):
        signal = f"Відеопотік з {self.model} (800x600)"
        print(f"{self.model}: {self.vga_connection()} -> Надсилаю: {signal}")
        return signal
