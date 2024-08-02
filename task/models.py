from django.db import models
from category.models import TaskCategory

# Create your models here.

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=150)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField()
    task_cat = models.ManyToManyField(TaskCategory, related_name='cat_of_task')

    def __str__(self):
        return self.taskTitle
    