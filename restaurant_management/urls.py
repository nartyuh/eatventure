from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.render_login),
    # path('<slug:username>/<slug:password>/', views.login),
    re_path(r'^(?P<username>[^/]+)/(?P<password>[^/]+)/$', views.login),
    # path('<slug:username>/<slug:password>/deleteaccount', views.delete_account),
    re_path(r'^(?P<username>[^/]+)/(?P<password>[^/]+)/deleteaccount/$', views.delete_account),
    re_path(r'^(?P<username>[^/]+)/(?P<password>[^/]+)/(?P<restaurant_id>[^/]+)/$', views.view_restaurant),
    re_path(r'^(?P<username>[^/]+)/(?P<password>[^/]+)/(?P<restaurant_id>[^/]+)/updaterestaurant/(?P<restaurant_name>[^/]+)/(?P<best_selling_item>[^/]+)/(?P<best_selling_item_dsc>[^/]+)/(?P<food_bank>[^/]+)/$', views.update_restaurant),
    re_path(r'^(?P<username>[^/]+)/(?P<password>[^/]+)/(?P<restaurant_id>[^/]+)/deleterestaurant/$', views.delete_restaurant),
    # path('<slug:username>/<slug:password>/<slug:restaurant_id>/deleterestaurant/', views.delete_restaurant),
]