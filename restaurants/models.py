from django.db import models
from locations.models import Address

# Create your models here.

class Restaurant(models.Model):
    restaurant_id = models.CharField(primary_key=True, max_length=50)
    restaurant_name = models.CharField(max_length=100)
    price_range = models.CharField(max_length=10)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['restaurant_name', 'address_id']

class RatingStats(models.Model):
    rating_stats_id = models.OneToOneField(Restaurant, primary_key=True, on_delete=models.CASCADE)
    aggregate_rating = models.FloatField(default=0)
    review_count = models.IntegerField(default=0)
    recommended = models.BooleanField(default=False)

class BestSellingItem(models.Model):
    best_selling_item_id = models.OneToOneField(Restaurant, primary_key=True, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=200)

class Coordinates(models.Model):
    coordinates_id  =models.OneToOneField(Restaurant, primary_key=True, on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=16, decimal_places=12)
    latitude = models.DecimalField(max_digits=16, decimal_places=12)