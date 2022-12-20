from django.http import HttpResponse
from django.shortcuts import render
from .models import Features

# Create your views here.


def home(request):

    features = Features.objects.all()

    return render(request, 'index.html', {'features': features})


def input_page(request):
    return render(request, 'registration.html')




