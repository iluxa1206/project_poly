from django.db import models
from research_fields.models import ResearchField


class Tutor(models.Model):  # Ученые
    full_name = models.CharField(max_length=255)  # ФИО
    biography = models.TextField()  # Биография
    birth_date = models.DateField()  # Дата рождения
    research_field = models.ForeignKey(ResearchField, on_delete=models.CASCADE)  # Дисциплина / сфера изучения
    position = models.CharField(max_length=255)  # Должность
    academic_degree = models.CharField(max_length=255)  # Ученая степень
    photo = models.ImageField(upload_to='scientists/')  # фото

    def __str__(self):
        return self.full_name
