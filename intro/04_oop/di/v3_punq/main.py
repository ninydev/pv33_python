import sys
from pathlib import Path
import punq

# # Додаємо шлях до v1, щоб використовувати існуючі класи
# sys.path.append(str(Path(__file__).parent.parent / "v1"))

from storage_interface import StorageInterface
from local_storage import LocalStorage
from minio_storage import MinioStorage
from avatar_service import AvatarService

def main():
    container = punq.Container()
    
    # Реєструємо реалізацію для інтерфейсу
    container.register(StorageInterface, LocalStorage)
    
    # Реєструємо сервіс.
    # punq автоматично проаналізує метод __init__ класу AvatarService
    # та підставить StorageInterface під час створення об'єкта.
    container.register(AvatarService)
    
    # Отримуємо (resolve) готовий сервіс
    avatar_service = container.resolve(AvatarService)
    
    print("--- Punq DI Example ---")
    avatar_service.upload_avatar("punq_photo.jpg")
    
    # Щоб змінити сховище, достатньо зареєструвати нову реалізацію
    print("\n--- Changing implementation to MinioStorage ---")
    container.register(StorageInterface, MinioStorage)
    minio_service = container.resolve(AvatarService)
    minio_service.upload_avatar("punq_photo.jpg")

if __name__ == "__main__":
    main()
