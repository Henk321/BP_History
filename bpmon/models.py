from django.db import models
from django.utils import timezone


class Pressure(models.Model):
    'blood pressure (systolic and diastolic) and heart rate readings (bpm)'
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    rate = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)


class Weight(models.Model):
    'weight (in pounds for now)'
    wght = models.DecimalField(max_digits=4, decimal_places=1)
    date = models.DateTimeField(default=timezone.now)
