from di_container import DIContainer
from storage_interface import StorageInterface
from azure_blob_storage import AzureBlobStorage
from minio_storage import MinioStorage
from local_storage import LocalStorage

def run_example(storage_impl):
    container = DIContainer()
    
    # Реєструємо обрану реалізацію
    container.register(StorageInterface, storage_impl)
    
    # Отримуємо сервіс через контейнер
    avatar_service = container.get_avatar_service()
    
    # Використовуємо сервіс
    avatar_service.upload_avatar("my_photo.jpg")

if __name__ == "__main__":
    print("--- Використання Azure Blob Storage ---")
    run_example(AzureBlobStorage())

    print("\n--- Використання MinIO Storage ---")
    run_example(MinioStorage())

    print("\n--- Використання Local Storage ---")
    run_example(LocalStorage())
