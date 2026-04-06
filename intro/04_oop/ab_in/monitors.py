from .base import Monitor
from .interfaces import HDMI, VGA

class SamsungMonitor(Monitor, HDMI):
    """
    Сучасний монітор Samsung з HDMI інтерфейсом.
    """
    def hdmi_connection(self):
        return "Підключено через HDMI"

    def receive_video_stream(self, data):
        print(f"Монітор {self.model} ({self.hdmi_connection()}) відображає: {data}")

class OldDellMonitor(Monitor, VGA):
    """
    Старий монітор Dell, який має тільки VGA порт.
    """
    def vga_connection(self):
        return "Підключено через VGA"

    def receive_video_stream(self, data):
        print(f"Монітор {self.model} ({self.vga_connection()}) відображає: {data} (аналоговий сигнал)")
