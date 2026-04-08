from storage_interface import StorageInterface

class AzureBlobStorage(StorageInterface):
    def save(self, avatar_name: str):
        print(f"Завантажено аватар {avatar_name} у сховище Azure Blob")
