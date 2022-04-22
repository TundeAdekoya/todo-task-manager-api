
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TASK_CHOICES = (
    ('ongoing', 'Ongoing'),
    ('completed', 'Completed'),
)


class Todo(models.Model):
    title = models.CharField(max_length=200)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    task = models.CharField(max_length=20, choices=TASK_CHOICES, default='ongoing' )
    created_on = models.DateTimeField(editable=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
