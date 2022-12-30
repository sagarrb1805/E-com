from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def user_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        address = request.POST.get('address')
        
        if User.objects.filter(email=email):
            messages.error(request, "An account with this email exits try login")
            redirect('accounts:user_login')

        if password != confirm_password:
            messages.error(request, "password doesn't match")
            return reverse('accounts:user_register')
        myuser = User.objects.create_user(username=email, email=email, password=password)
        myuser.full_name = name
        myuser.phone_number = phone_number
        myuser.address = address

        myuser.save()
        messages.success(request, 'Your account has been successfuly created')
        return redirect('accounts:user_login')


    return render(request, 'accounts/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('products:home_view')
        else:
            messages.error(request, 'Bad credentials')
            return redirect('accounts:user_login')

    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'logged out')
    return redirect('products:home_view')

