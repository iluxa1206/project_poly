from django.db import models


class Tutor(models.Model):
    full_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=100)
    about = models.TextField()
    science_degree = models.CharField(max_length=100)
    books = models.TextField(null=True, blank=True)
    works = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.full_name
