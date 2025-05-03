from django.db import models

class Sensors(models.Model):
    cpu = models.FloatField()
    mem = models.FloatField()
    disk = models.FloatField()
