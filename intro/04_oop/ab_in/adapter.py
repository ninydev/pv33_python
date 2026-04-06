from .interfaces import HDMI, VGA

class VGAToHDMIAdapter(HDMI):
    """
    Адаптер, який приймає VGA сигнал та перетворює його на HDMI.
    Він реалізує інтерфейс HDMI, але в середині тримає посилання на VGA джерело.
    Це приклад патерна Adapter.
    """
    def __init__(self, vga_source):
        """
        :param vga_source: Об'єкт, що має VGA вихід.
        """
        self.vga_source = vga_source

    def hdmi_connection(self):
        """
        Реалізація методу інтерфейсу HDMI через перетворення.
        """
        return f"Адаптований сигнал ({self.vga_source.vga_connection()}) -> перетворено на HDMI"

    def convert_signal(self):
        """
        Метод для отримання перетвореного сигналу.
        """
        original_signal = self.vga_source.send_video_stream()
        converted_signal = f"[КОНВЕРТОВАНО] {original_signal}"
        return converted_signal
