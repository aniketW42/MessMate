from django.shortcuts import redirect, render
from .models import MessmateUser 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/explore')
        else:
            messages.error(request, 'Invalid credentials')
    
    return render(request, 'SignIn/login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if MessmateUser.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
            else:
                user = MessmateUser.objects.create_user(email=email, username=name)
                user.set_password(password1)
                user.save()
                messages.success(request, 'User created')
        else:
            messages.info(request, 'Passwords do not match')

    return render(request, 'SignUp/register.html')

def logout_page(request):
    logout(request)
    return redirect('/accounts/login')