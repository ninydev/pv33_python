# Django Project

Этот проект использует Celery для выполнения фоновых задач (например, получение данных каждые 20 секунд) и Redis в качестве брокера сообщений.

## Требования

* Python 3.10+
* Docker и Docker Compose

## Установка и запуск

1.  **Склонируйте репозиторий и перейдите в папку проекта:**

    ```bash
    # git clone <your_repo_url>
    cd intro/django1
    ```

2.  **Создайте и активируйте виртуальное окружение:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Linux/macOS
    # venv\Scripts\activate   # Для Windows
    ```

3.  **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```
    *(Убедитесь, что у вас есть `celery`, `redis` и `django-celery-beat` в `requirements.txt`)*

4.  **Запустите Redis через Docker Compose:**

    Для работы Celery необходим брокер сообщений. В нашем случае это Redis.

    ```bash
    docker-compose up -d redis
    ```

5.  **Примените миграции:**

    ```bash
    python manage.py migrate
    ```

6.  **Запустите Django сервер:**

    Откройте новый терминал (с активированным виртуальным окружением) и выполните:

    ```bash
    python manage.py runserver
    ```

7.  **Запустите Celery Worker:**

    Откройте еще один терминал (с активированным виртуальным окружением) и выполните:

    ```bash
    celery -A core worker -l info
    ```

8.  **Запустите Celery Beat:**

    Откройте еще один (четвертый) терминал (с активированным виртуальным окружением) и выполните:

    ```bash
    celery -A core beat -l info
    ```
    *Celery Beat будет отправлять задачу `check_alerts` каждые 20 секунд, а Worker будет её выполнять и писать сообщение в лог.*
