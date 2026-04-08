# FastAPI Dependency Injection (DI)

FastAPI має вбудовану потужну систему впровадження залежностей (Dependency Injection). Вона базується на функції `Depends()` та анотаціях типів (type hints).

## Встановлення модулів

Для роботи цього прикладу необхідно встановити сам фреймворк FastAPI та сервер `uvicorn`:
```bash
pip install fastapi uvicorn
```

## Як це працює

1. Ми створюємо **функції-провайдери** (`get_storage`, `get_avatar_service`), які повертають екземпляри класів.
2. У параметрах маршруту (endpoint) або іншого провайдера ми використовуємо `Depends(функція_провайдер)`.
3. При виклику маршруту FastAPI автоматично будує граф залежностей:
   - Бачить, що для виконання `upload_avatar` потрібен `AvatarService` і викликає `get_avatar_service`.
   - Бачить, що `get_avatar_service` у своїх аргументах потребує `StorageInterface` через `Depends(get_storage)`, тому спочатку викликає `get_storage`.
   - Передає результат `get_storage` (об'єкт сховища) у `get_avatar_service`, а потім передає готовий `AvatarService` у наш маршрут.

## Запуск

Ви можете запустити скрипт безпосередньо:
```bash
python main.py
```
Або через uvicorn:
```bash
uvicorn main:app --reload
```
Після цього перейдіть до автоматично згенерованої документації за адресою `http://127.0.0.1:8000/docs` та спробуйте виконати POST-запит.
