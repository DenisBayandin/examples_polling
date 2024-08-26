from django.db import models


class Book(models.Model):
    title = models.CharField(blank=False, null=False, max_length=255)
    description = models.TextField(blank=True, null=True, max_length=8000)

    def __str__(self):
        return self.title
