from django.db import models
from category.models import Category

# Create your models here.
class Task (models.Model):
    taskTitle = models.CharField(max_length = 200)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_date = models.DateField()
    task_category = models.ManyToManyField(Category)