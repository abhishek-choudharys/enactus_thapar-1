from django.db import models

class Events(models.Model):
    name = models.CharField(max_length=200)
    branch=models.CharField(max_length=200)
    event=models.CharField(max_length=200)
    email=models.EmailField()
    number=models.IntegerField()
    Year=models.IntegerField()
    Rollno=models.IntegerField()

    def __str__(self):

        return self.title
