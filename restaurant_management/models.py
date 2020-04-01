from django.db import models
from restaurants.models import Restaurant

# Create your models here.

class ManagerAccount(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=100)

class MatchManagerToRestaurant(models.Model):
    restaurant = models.OneToOneField(Restaurant, primary_key=True ,on_delete=models.CASCADE)
    manager = models.ForeignKey(ManagerAccount, on_delete=models.CASCADE)