from django.db import models
from django.conf import settings

class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='books', null=True, blank=True)


    def __str__(self):
        return self.title
