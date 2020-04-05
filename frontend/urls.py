from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.map),
    re_path(r'^search/(?P<restaurant_name>[^/]+)/(?P<street_name>[^/]+)/(?P<postcode>[^/]+)/$', views.search),
    path('mapstats/<slug:select>/', views.show_map_stats),
]