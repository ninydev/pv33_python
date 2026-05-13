import json
import redis
from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from datetime import datetime

logger = get_task_logger(__name__)


@shared_task
def check_alerts():
    logger.info("I'm alive, I'm going to ask for information")
    
    # Подключаемся к Redis
    r = redis.Redis.from_url(settings.CELERY_BROKER_URL)
    
    # Формируем сообщение для отправки клиентам
    message = {
        'type': 'alert_update',
        'message': 'Я жива, я пошла спрашивать информацию (обновление)',
        'timestamp': datetime.now().strftime("%H:%M:%S")
    }
    
    # Публикуем сообщение в канал 'sse_messages'
    r.publish('sse_messages', json.dumps(message))
