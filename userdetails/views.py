from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages,auth

# Create your views here.


def registration(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email_id']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken")
            return redirect('/user/register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email already exist")
            return redirect('/user/register')
        elif password != confirm_password:
            messages.info(request, "Password not matching")
            return redirect('/user/register')
        else:
            create_user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            create_user.save()
            return redirect('/user/login')
    else:
        return render(request, 'registration.html')
    return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('/user/login')


    return render(request, 'login.html')


def logout(request):
    auth.logout(request)

    return redirect('/')