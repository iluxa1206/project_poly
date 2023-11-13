from django.db import models

# Create your models here.
# articles/models.py
from django.db import models
from tutors.models import Tutor
from research_fields.models import ResearchField


class Article(models.Model):  # Статья
    title = models.CharField(max_length=255)  # Название
    text = models.TextField()  # Текст
    scientist_tag = models.ForeignKey(Tutor, on_delete=models.CASCADE)  # тэг с отметкой ученого
    research_field_tag = models.ForeignKey(ResearchField, on_delete=models.CASCADE)  # Тэг с отметкой сферы изучения
    photo = models.ImageField(upload_to='articles/')  # Фото

    def __str__(self):
        return self.title
