from django.db import models


# Create your models here.
class Employees(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    employee_age = models.IntegerField()
    employee_salary = models.FloatField(max_length=10)

    def __str__(self):
        return self.first_name