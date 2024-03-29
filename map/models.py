from django.db import models

# Create your models here.

class Cctv(models.Model):
    class Meta:
        db_table = 'cctv'
    cctvId =  models.AutoField(primary_key=True, db_column='cctvId')
    latitude = models.FloatField(db_column='latitude')
    longtitude = models.FloatField(db_column='longtitude')
    address = models.TextField(db_column='address')
    detect = models.IntegerField(default=0, db_column='detect')

class Violent(models.Model):
    class Meta:
        db_table = 'violent'
    
    #외래키
    cctvId=models.ForeignKey(Cctv, null=True, on_delete=models.SET_NULL, db_column='cctvId')
    violentTime=models.DateTimeField(auto_now_add=True, db_column='violentTime')
    violentRate=models.IntegerField(default=0, db_column='violentRate')

class User(models.Model):
    class meta:
        db_table = 'user'

    id = models.CharField(max_length=255, unique=True, primary_key=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    tel = models.CharField(max_length=255, unique=True)
    agency = models.CharField(max_length=255)


