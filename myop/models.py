from django.db import models
from django.urls import reverse
# Create your models here.
class User(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=250)
    Login = models.CharField(max_length=250)
    Password = models.CharField(max_length=250)
    ID_Roles = models.IntegerField()

    def __str__(self):
        return self.Name
class Film(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name_Film = models.CharField(max_length=250)
    Name_Film_Eng = models.CharField(max_length=250)
    Duration_of_the_film = models.CharField(max_length=250)
    Description = models.CharField(max_length=500)
    year_production = models.CharField(max_length=250)
    Country = models.CharField(max_length=250)
    Genre = models.CharField(max_length=250)
    Director = models.CharField(max_length=250)
    Budget = models.CharField(max_length=250)
    Fees_in_the_world = models.CharField(max_length=250)
    Age_restrictions = models.CharField(max_length=250)
    World_premiere = models.DateField()
    Photo = models.ImageField(upload_to='static/Image/')

    def __str__(self):
        return self.Name_Film



class Role(models.Model):
    ID = models.IntegerField(primary_key=True)
    Role = models.CharField(max_length=250)

    def __str__(self):
        return self.Role

class Review(models.Model):
    ID = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=1000)
    Rate = models.IntegerField()
    ID_User = models.IntegerField()
    ID_Films = models.IntegerField()

    def __str__(self):
        return self.ID_User


