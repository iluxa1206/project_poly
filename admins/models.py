# Create your models here.
# admins/models.py
from django.db import models
from django.contrib.auth.models import User


class Admin(models.Model):  # Админы
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Имя пользователя
    is_major = models.BooleanField(default=False)  # Главный да/нет

    def __str__(self):
        return self.user.username
