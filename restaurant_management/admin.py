from django.contrib import admin
from .models import ManagerAccount, MatchManagerToRestaurant

# Register your models here.

admin.site.register(ManagerAccount)
admin.site.register(MatchManagerToRestaurant)
