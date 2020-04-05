from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.render_login, name='login'),
    path('<slug:username>/<slug:password>/', views.login),
    path('<slug:username>/<slug:password>/<slug:restaurant_id>/', views.view_restaurant),
    re_path(r'^(?P<username>[\w|\W]+)/(?P<password>[\w|\W]+)/(?P<restaurant_id>[\w|\W]+)/update/(?P<restaurant_name>[\w|\W]+)/(?P<best_selling_item>[\w|\W]+)/(?P<best_selling_item_dsc>[\w|\W]+)/(?P<food_bank>[\w|\W]+)/$', views.update),
    path('<slug:username>/<slug:password>/<slug:restaurant_id>/delete/', views.delete),
]