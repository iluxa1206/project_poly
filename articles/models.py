from django.db import models

# Create your models here.
# articles/models.py
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='articles/')
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.title
