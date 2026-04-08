import sys
from pathlib import Path
from fastapi import FastAPI, Depends
import uvicorn

# Додаємо шлях до v1, щоб використовувати існуючі класи
sys.path.append(str(Path(__file__).parent.parent / "v1"))

from storage_interface import StorageInterface
from local_storage import LocalStorage
from avatar_service import AvatarService

app = FastAPI(title="FastAPI DI Example")

# Функція-провайдер для Storage
def get_storage() -> StorageInterface:
    # Тут ми можемо змінити LocalStorage на будь-яке інше сховище в одному місці
    return LocalStorage()

# Функція-провайдер для AvatarService, яка залежить від StorageInterface
def get_avatar_service(storage: StorageInterface = Depends(get_storage)) -> AvatarService:
    return AvatarService(storage)

@app.post("/avatar/")
def upload_avatar(avatar_name: str, service: AvatarService = Depends(get_avatar_service)):
    service.upload_avatar(avatar_name)
    return {"message": f"Avatar {avatar_name} successfully uploaded"}

if __name__ == "__main__":
    print("Run this app with: uvicorn main:app --reload")
    uvicorn.run(app, host="127.0.0.1", port=8000)
