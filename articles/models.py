from django.db import models

# Create your models here.
# articles/models.py
from django.db import models
from tutors.models import Tutor
from research_fields.models import ResearchField

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    scientist_tag = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    research_field_tag = models.ForeignKey(ResearchField, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='articles/')


    def __str__(self):
        return self.title
