from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, "Username already exists!")
            elif User.objects.filter(email = email).exists():
                messages.error(request, "Email already exists!")
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1
                )
                user.save()
                messages.success(request, "Account Created Successfully!")
                return redirect("/accounts/login/")
        else:
            messages.error(request, "Passowrd did not match!")
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username = username , password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Sucessfull!")
            return redirect("/news/all_news/")
        else:
            messages.error(request, "Invalid Email or password!")

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out Successfull!")
    return redirect("/accounts/login/")
