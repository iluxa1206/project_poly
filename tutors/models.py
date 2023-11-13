from django.db import models
from research_fields.models import ResearchField

class Tutor(models.Model):
    full_name = models.CharField(max_length=255)
    biography = models.TextField()
    birth_date = models.DateField()
    research_field = models.ForeignKey(ResearchField, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    academic_degree = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='scientists/')

    def __str__(self):
        return self.full_name
