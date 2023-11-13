from django.db import models

# Create your models here.
# requests/models.py
from django.db import models
from research_fields.models import ResearchField


class Request(models.Model):  # Данные для формы, которая заполняется студентом
    full_name = models.CharField(max_length=255)  # ФИО Студента
    group = models.CharField(max_length=255)  # Номер группы
    course = models.IntegerField()  # курс
    faculty = models.CharField(max_length=255)  # Факультет
    research_field = models.ForeignKey(ResearchField, on_delete=models.CASCADE)  # Предмет изучения
    birth_date = models.DateField()  # дата рождения
    phone = models.CharField(max_length=15)  # телефон
    email = models.EmailField()  # email

    def __str__(self):
        return self.fullname
