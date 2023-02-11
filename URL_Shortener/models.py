from django.db import models

# Create your models here.

class ShortenedURL(models.Model):

    originalURL = models.URLField(max_length = 1000)
    shortenedURL = models.CharField(max_length = 100)
    shortened = models.URLField(max_length = 100)
    dateOfCreation = models.DateTimeField()

    def __str__(self):
        return self.originalURL