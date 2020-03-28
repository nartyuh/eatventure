from django.contrib import admin
from .models import FoodCategory, EstablishmentType, Cuisine, RatingStats, BestSellingItem, Restaurant, Discount

# Register your models here.

admin.site.register(FoodCategory)
admin.site.register(EstablishmentType)
admin.site.register(Cuisine)
admin.site.register(RatingStats)
admin.site.register(BestSellingItem)
admin.site.register(Restaurant)
admin.site.register(Discount)