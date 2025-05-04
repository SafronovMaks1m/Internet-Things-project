from django.db import models

class Sensors(models.Model):
    cpu = models.FloatField()
    mem = models.FloatField()
    disk = models.FloatField()

class Users(models.Model):
    name = models.CharField()

class DataUser(models.Model):
    upload = models.FloatField()
    download = models.FloatField()
    traffic = models.FloatField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
