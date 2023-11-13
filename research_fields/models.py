from django.db import models

# Create your models here.
class ResearchField(models.Model):  # Дисциплина / предмет изучения
    name = models.CharField(max_length=255)  # Название
    description = models.TextField()  # Описание