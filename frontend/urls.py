from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.map),
    re_path(r'^search/(?P<restaurant_name>[\w|\W]+)/(?P<street_name>[\w|\W]+)/(?P<postcode>[\w|\W]+)/$', views.search),
    path('mapstats/', views.show_map_stats),
]