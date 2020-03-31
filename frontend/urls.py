from django.urls import path

from . import views

urlpatterns = [
    path('', views.map, name='map'),
    path('search/<slug:restaurant_name>/<slug:street_name>/<slug:postcode>/', views.search, name='search')
]