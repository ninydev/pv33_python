import uuid

from django.db import models

# Create your models here.
class NewsSubscriber (models.Model):
    email = models.EmailField(unique=True)
    is_active=models.BooleanField(default=False)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)