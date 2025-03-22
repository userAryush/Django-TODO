from django.db import models

# Create your models here.

class Todo(models.Model):
    
    name = models.CharField(max_length=200)
    task = models.TextField()
    status = models.CharField(max_length=100)
    deadline_day = models.IntegerField(null=True, blank =True)
    
        