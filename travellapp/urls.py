from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('input/', views.input_page, name='input'),
]