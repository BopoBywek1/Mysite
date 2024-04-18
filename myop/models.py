from django.db import models

# Create your models here.
class Users(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=250)
    Login = models.CharField(max_length=250)
    Password = models.CharField(max_length=250)
    ID_Roles = models.IntegerField()

    def __str__(self):
        return self.Name
class Films(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name_Film = models.CharField(max_length=250)
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

    def __str__(self):
        return self.Name_Film



