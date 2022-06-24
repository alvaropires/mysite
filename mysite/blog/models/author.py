from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['first_name']


    def __str__(self):
        return self.last_name