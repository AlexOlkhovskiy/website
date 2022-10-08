from django.urls import path
from . import views
from .views import show_category, shop_add_product

urlpatterns = [
    path('', views.shop, name = 'shop'),
    path('category/<slug:cat_slug>/', show_category, name = 'category'),
    path('category/<slug:cat_slug>/', show_category, name = 'category'),
    path('category/kosmetika/', show_category, name = 'category_main'),
    path('add_product', shop_add_product, name = 'add_product'),
]