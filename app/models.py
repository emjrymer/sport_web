from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=30)
    att = models.IntegerField()
    yds = models.IntegerField()
    avg = models.FloatField()
    long = models.IntegerField()
    td = models.IntegerField()

    def __str__(self):
        return self.name