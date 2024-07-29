# myapp/models.py

from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name
    
    # class Meta:
    #     ordering = ['-value']