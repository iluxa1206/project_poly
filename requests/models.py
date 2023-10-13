from django.db import models

# Create your models here.
# requests/models.py
from django.db import models


class Request(models.Model):
    fullname = models.CharField(max_length=255)
    birth_date = models.DateField()

    COURSE_CHOICES = (
        ('B', 'Бакалавриат'),
        ('S', 'Специалитет'),
        ('M', 'Магистратура'),
    )

    course = models.CharField(max_length=1, choices=COURSE_CHOICES)
    study_group = models.CharField(max_length=10)

    def __str__(self):
        return self.fullname
