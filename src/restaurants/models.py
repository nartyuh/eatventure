from django.db import models
from locations.models import Address

# Create your models here.

class FoodCategory(models.Model):
    food_category_name = models.CharField(primary_key=True, max_length=20)
    disclaimer = models.CharField(max_length=200)

class EstablishmentType(models.Model):
    food_category_name = models.OneToOneField(FoodCategory, on_delete=models.CASCADE)
    atmosphere = models.CharField(max_length=20)

class Cuisine(models.Model):
    food_category_name = models.OneToOneField(FoodCategory, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=20)

class RecommendationBenchmark(models.Model):
    rating = models.IntegerField()
    num_of_reviews = models.IntegerField()
    recommended = models.CharField(max_length=3)

class BestSellerItem(models.Model):
    item_name = models.CharField(primary_key=True, max_length=50)
    item_type = models.CharField(max_length=20)

'''
class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=20)
    rating_stats = models.ForeignKey(RecommendationBenchmark, on_delete=models.DO_NOTHING)
    price_range = models.CharField(max_length=4)
    discount = models.ForeignKey(Discount, on_delete=models.DO_NOTHING)
    food_category_name = models.ForeignKey(FoodCategory, on_delete=models.DO_NOTHING)
    best_seller_item = models.ForeignKey(BestSellerItem, on_delete=models.DO_NOTHING)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)

class Discount(models.Model):
    discount_code = models.CharField(max_length=10)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
'''

