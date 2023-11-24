from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_detail, name='cart-detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart-add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart-remove'),
    path('wishlist/', views.wishlist_detail, name='wishlist-detail'),
    path('wishlist/add/<int:product_id>/', views.cart_add, name='wishlist-add'),
    path('wishlist/remove/<int:product_id>/', views.wishlist_remove, name='wishlist-remove'),
]
