from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main-page'),
    path('contacts/', views.contacts, name='contacts'),
    path('news/', views.news, name='news'),
    path('shop', views.shop, name='shop-all'),
    path('shop/bicycles', views.shop_bicycles, name='shop-bicycles'),
    path('shop/accessories', views.shop_accessories, name='shop-accessories'),
    path('shop/spare-parts', views.shop_spare_parts, name='shop-spare-parts'),
    path('shop/clothes', views.shop_clothes, name='shop-clothes')
]
