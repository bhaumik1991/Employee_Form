from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10,)
    salary = models.IntegerField()
    occupation = models.CharField(max_length=250)

    def __str__(self):
        return self.full_name


