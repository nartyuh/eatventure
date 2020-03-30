from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Country(models.Model):
    country_name = models.CharField(primary_key=True, max_length=20)
    
    def __str__(self):
        return self.country_name


class Postcode(models.Model):
    postcode = models.CharField(primary_key=True ,max_length=10)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['city', 'state', 'country']

    def __str__(self):
        return self.city + ', ' + self.state + ', ' + self.country + ' ' + self.postcode


class Address(models.Model):
    address_id = models.CharField(primary_key=True, max_length=50)
    street_num = models.CharField(max_length=10)
    street_name = models.CharField(max_length=30)
    postcode = models.ForeignKey(Postcode, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['street_num', 'street_name', 'postcode']

    def __str__(self):
        return self.street_num + ' ' + self.street_name + ', ' + self.postcode
        