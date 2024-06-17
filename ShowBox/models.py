from django.db import models


class ShowBox(models.Model):
    theater_name = models.CharField(max_length=20)
    show_name = models.CharField(max_length=50)
    show_time = models.DateTimeField()
    total_seats = models.IntegerField()
    reserved_seats = models.IntegerField()
    amount = models.IntegerField()
