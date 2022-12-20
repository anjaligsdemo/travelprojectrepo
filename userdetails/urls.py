from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registration, name='home'),
    path('login/', views.login, name='input'),
    path('logout/', views.logout, name='input'),
]