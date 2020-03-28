from django.db import models
from locations.models import Address

# Create your models here.

class FoodCategory(models.Model):
    food_category_name = models.CharField(primary_key=True, max_length=20)
    disclaimer = models.CharField(max_length=200)

    def __str__(self):
        return self.food_category_name + ': ' + self.disclaimer


class EstablishmentType(models.Model):
    establishment_type_id = models.AutoField(auto_created=True, primary_key=True)
    food_category_name = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    atmosphere = models.CharField(max_length=20)

    class Meta:
        unique_together = ['food_category_name', 'atmosphere']

    def __str__(self):
        return self.atmosphere + ' ' + self.food_category_name


class Cuisine(models.Model):
    cuisine_id = models.AutoField(auto_created=True, primary_key=True)
    food_category_name = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=20)

    class Meta: 
        unique_together = ['food_category_name', 'nationality']

    def __str__(self):
        return self.nationality + ' ' + self.food_category_name


class RatingStats(models.Model):
    rating_stats_id = models.AutoField(auto_created=True, primary_key=True)
    rating = models.IntegerField(default=0)
    num_of_reviews = models.IntegerField(default=0)
    recommended = models.BooleanField()

    def __str__(self):
        return self.rating + ' stars, ' + self.num_of_reviews + ' reviews'

class BestSellingItem(models.Model):
    item_id = models.AutoField(auto_created=True, primary_key=True)
    item_name = models.CharField(max_length=50)
    item_description = models.CharField(max_length=200)

    def __str__(self):
        return self.item_name + ': ' + self.item_description


class Restaurant(models.Model):
    restaurant_id = models.AutoField(auto_created=True, primary_key=True)
    restaurant_name = models.CharField(max_length=20)
    rating_stats_id = models.OneToOneField(RatingStats, null=True, on_delete=models.SET_NULL)
    price_range = models.CharField(max_length=4)
    food_category = models.ForeignKey(FoodCategory, null=True, on_delete=models.SET_NULL)
    establishment_type = models.ForeignKey(EstablishmentType, null=True, on_delete=models.SET_NULL)
    cuisine = models.ForeignKey(Cuisine, null=True, on_delete=models.SET_NULL)
    '''
        we make Restaurant and BestSellingItem one-to-one relationship cuz each restaurant is 
        going to have different description for their best selling item
    '''
    best_selling_item = models.OneToOneField(BestSellingItem, null=True, on_delete=models.SET_NULL)
    '''
        one address can have many restaurants (food court, mall, etc.)
    '''
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['restaurant_name', 'address_id']

    def __str__(self):
        return self.restaurant_name + ', ' + self.address_id + ', ratings: ' + self.rating_stats_id


class Discount(models.Model):
    discount_code = models.CharField(max_length=10)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    expiry_date = models.DateTimeField(editable=True)
    details = models.CharField(max_length=200)

    class Meta:
        unique_together = ['discount_code', 'restaurant_id']

    def __str__(self):
        return self.restaurant_id + ', ' + self.discount_code + ' expires on ' + self.expiry_date 