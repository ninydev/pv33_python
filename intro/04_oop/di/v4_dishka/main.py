import sys
from pathlib import Path
from dishka import Provider, Scope, make_container, provide

# Додаємо шлях до v1, щоб використовувати існуючі класи
sys.path.append(str(Path(__file__).parent.parent / "v1"))

from storage_interface import StorageInterface
from local_storage import LocalStorage
from avatar_service import AvatarService

class AppProvider(Provider):
    # Вказуємо Scope.APP, щоб створювався один екземпляр на весь життєвий цикл додатку
    @provide(scope=Scope.APP)
    def get_storage(self) -> StorageInterface:
        return LocalStorage()
        
    @provide(scope=Scope.APP)
    def get_avatar_service(self, storage: StorageInterface) -> AvatarService:
        return AvatarService(storage)

def main():
    # Створюємо провайдер та ініціалізуємо DI контейнер
    provider = AppProvider()
    container = make_container(provider)
    
    print("--- Dishka DI Example ---")
    
    # Отримуємо готовий сервіс з контейнера
    avatar_service = container.get(AvatarService)
    avatar_service.upload_avatar("dishka_photo.jpg")
    
    # Важливо закривати контейнер для вивільнення ресурсів
    container.close()

if __name__ == "__main__":
    main()
