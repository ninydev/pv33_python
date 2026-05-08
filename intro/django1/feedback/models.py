from django.db import models
from django.conf import settings  # Правильный способ сослаться на кастомного юзера

# Create your models here.
class Feedback(models.Model):
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Feedback from {self.firstName} ({self.email}) at {self.created_at}"