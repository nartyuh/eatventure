from django.contrib import admin
from .models import Country, Postcode, Address

# Register your models here.

admin.site.register(Country)
admin.site.register(Postcode)
admin.site.register(Address)