from monitors import SamsungMonitor, OldDellMonitor
from computers import MacBook, OldPCLaptop
from adapter import VGAToHDMIAdapter

def main():
    print("--- 1. Пряме підключення через HDMI ---")
    mac = MacBook("MacBook Pro 16")
    samsung = SamsungMonitor("Samsung Odyssey")
    
    # Комп'ютер передає, монітор приймає
    signal = mac.send_video_stream()
    samsung.receive_video_stream(signal)
    
    print("\n--- 2. Пряме підключення через VGA ---")
    old_pc = OldPCLaptop("Pentium 4 Laptop")
    dell = OldDellMonitor("Dell UltraSharp Old")
    
    # Передача через VGA
    vga_signal = old_pc.send_video_stream()
    dell.receive_video_stream(vga_signal)
    
    print("\n--- 3. Використання адаптера (VGA в HDMI) ---")
    # У нас є старий комп'ютер (VGA) і новий монітор (HDMI)
    # Ми хочемо підключити old_pc до samsung
    
    adapter = VGAToHDMIAdapter(old_pc)
    
    # Тепер монітор Samsung може прийняти сигнал від адаптера, 
    # бо адаптер реалізує інтерфейс HDMI
    
    # Викликаємо конвертацію та передаємо в монітор
    print(f"Статус підключення: {adapter.hdmi_connection()}")
    adapted_signal = adapter.convert_signal()
    samsung.receive_video_stream(adapted_signal)

if __name__ == "__main__":
    main()
