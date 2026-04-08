from storage_interface import StorageInterface

class MinioStorage(StorageInterface):
    def save(self, avatar_name: str):
        print(f"Завантажено аватар {avatar_name} у сховище MinIO")
