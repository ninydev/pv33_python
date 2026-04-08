from storage_interface import StorageInterface
from avatar_service import AvatarService

class DIContainer:
    def __init__(self):
        self._services = {}

    def register(self, interface: type, implementation: object):
        self._services[interface] = implementation

    def resolve(self, interface: type):
        return self._services.get(interface)

    def get_avatar_service(self) -> AvatarService:
        storage = self.resolve(StorageInterface)
        if not storage:
            raise Exception("Storage implementation not registered")
        return AvatarService(storage)
