from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Пока ничего не добавляем, просто наследуем весь стандартный функционал
    pass