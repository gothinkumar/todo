from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=60)
    number = models.IntegerField()
    date = models.DateField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.task