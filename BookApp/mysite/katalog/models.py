from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=40)
    category = models.CharField(max_length=30)
    description = models.TextField(max_length=1000, default="Book's description")

    def __str__(self):
        return self.title
