from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    """ Перевирка форми регистрациї """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Все відно 'Раді Вас бачити на сайті'")
            return redirect('home')
        else:
            messages.success(request, "Невірний логин чи пароль, спробуй ще.")
            return redirect('home')
    else:        
        return render(request, 'bodi/home.html', {})

# def login_user(request):
#     pass    

def logout_user(request):
    logout(request)
    messages.success(request, "Ви успічно вийщли з облікового запису")
    return redirect('home')