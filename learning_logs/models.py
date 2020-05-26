from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    course_name=models.CharField(max_length=100)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.course_name

class Entry(models.Model):
    course_name=models.ForeignKey(Course, on_delete=models.CASCADE)
    course_id=models.CharField(max_length=10)
    Date=models.DateField()
    Hours_spent=models.IntegerField()
    statuses=[
        ('In Progress','In Progress'),
        ('Completed','Completed'),
        ]
    status=models.CharField(max_length=15, choices=statuses)

    class Meta:
        verbose_name_plural='entries'