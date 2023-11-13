from django.db import models

# Create your models here.
# requests/models.py
from django.db import models
from research_fields.models import ResearchField


class Request(models.Model):
    full_name = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    course = models.IntegerField()
    faculty = models.CharField(max_length=255)
    research_field = models.ForeignKey(ResearchField, on_delete=models.CASCADE)
    birth_date = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    def __str__(self):
        return self.fullname
