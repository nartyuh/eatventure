from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Country(models.Model):
    country_name = models.CharField(primary_key=True, max_length=20)


class Postcode(models.Model):
    postcode = models.CharField(primary_key=True ,max_length=10)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Address(models.Model):
    address_id = models.AutoField(auto_created=True, primary_key=True)
    unit_num = models.CharField(max_length=10, null=True)
    street_num = models.CharField(max_length=10)
    street_name = models.CharField(max_length=30)
    postcode = models.ForeignKey(Postcode, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['unit_num','street_num', 'street_name', 'postcode']