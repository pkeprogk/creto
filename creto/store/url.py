from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main-page'),
    path('contacts/', views.contacts, name='contacts'),
    path('news/', views.news, name='news'),
    path('shop/', views.shop, name='shop'),
]
