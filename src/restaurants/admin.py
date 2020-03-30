from django.contrib import admin
from .models import RatingStats, BestSellingItem, Restaurant, Coordinates

# Register your models here.

admin.site.register(RatingStats)
admin.site.register(BestSellingItem)
admin.site.register(Restaurant)
admin.site.register(Coordinates)