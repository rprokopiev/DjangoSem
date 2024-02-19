from django.db import models


class HeadsTailsResult(models.Model):
    result = models.CharField(max_length=5)
    time = models.DateTimeField()


class Dice(models.Model):
    result = models.CharField(max_length=5)
    time = models.DateTimeField()


class RandomInt(models.Model):
    result = models.CharField(max_length=5)
    time = models.DateTimeField()