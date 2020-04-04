from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.render_login, name='login'),
    path('<slug:username>/<slug:password>/', views.login),
    path('<slug:username>/<slug:password>/<slug:restaurant_id>/', views.view_restaurant),
    path('<slug:username>/<slug:password>/<slug:restaurant_id>/update/<slug:restaurant_name>/<slug:best_selling_item>/<slug:best_selling_item_dsc>/<slug:food_bank>/', views.update),
    path('<slug:username>/<slug:password>/<slug:restaurant_id>/delete/', views.delete),
]