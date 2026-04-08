from storage_interface import StorageInterface

class AvatarService:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def upload_avatar(self, avatar_name: str):
        self.storage.save(avatar_name)
