
# Create your models here.
# admins/models.py
from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_major = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
