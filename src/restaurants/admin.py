from django.contrib import admin
from .models import FoodCategory, EstablishmentType, Cuisine, RecommendationBenchmark, BestSellerItem

# Register your models here.

admin.site.register(FoodCategory)
admin.site.register(EstablishmentType)
admin.site.register(Cuisine)
admin.site.register(RecommendationBenchmark)
admin.site.register(BestSellerItem)