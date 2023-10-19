from django.urls import path
from . import views

urlpatterns = [
    path('account/register/', views.register_user, name='register'),
    path('account/login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('account/', views.user_account, name='account'),
]
