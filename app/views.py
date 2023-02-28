from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from loginsystem import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage


def dashboard(request):
    return render(request, 'authentication/index.html', {})


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['con_password']

        if User.objects.filter(username=username):
            messages.error(
                request, "Username already exist! Please try some other username.")
            return redirect('dashboard')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('dashboard')
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters.")

        if password != con_password:
            messages.error(request, "Passwords did not match")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('dashboard')

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()
        messages.success(
            request, "Your account has been successfully created. We have sent you a confirmation email, please confirm you email in order to activate your account  ")

        return redirect('signin')
    else:
        return render(request, 'authentication/signup.html', {})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'authentication/index.html', {'fname': fname})
        else:
            messages.error(request, '"Bad Credentials!')
            return redirect('signin')

    else:
        return render(request, 'authentication/signin.html', {})


def signout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('dashboard')
