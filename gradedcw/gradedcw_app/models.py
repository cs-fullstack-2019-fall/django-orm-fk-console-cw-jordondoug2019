from datetime import date

from django.db import models

# Create your models here.
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.CharField(max_length=200)
    date_posted = models.DateField(default=date.today)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
