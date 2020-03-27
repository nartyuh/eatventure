from django.db import models

# Create your models here.

class Country(models.Model):
    country_name = models.CharField(primary_key=True, max_length=20)


class Postcode(models.Model):
    postcode = models.CharField(primary_key=True ,max_length=10)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Address(models.Model):
    street_num = models.CharField(max_length=10)
    street_name = models.CharField(max_length=30)
    postcode = models.ForeignKey(Postcode, on_delete=models.CASCADE, default='should not be null')