from django.urls import path

from . import views

urlpatterns = [
    path('', views.map),
    path('search/<slug:restaurant_name>/<slug:street_name>/<slug:postcode>/', views.search),
    path('mapstats/', views.show_map_stats),
]