from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

def home(request):
    records = Record.objects.all()



    """ Перевирка форми регистрациї """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Все вірно 'Раді Вас бачити на сайті'")
            return redirect('home')
        else:
            messages.success(request, "Невірний логин чи пароль, спробуй ще.")
            return redirect('home')
    else:        
        return render(request, 'bodi/home.html', {'records': records})

# def login_user(request):
#     pass    

def logout_user(request):
    logout(request)
    messages.success(request, "Ви успічно вийщли з облікового запису")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Пройдіть автентифікацію та увійдіть
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "'Ви успішно зареєстровані! Заходьте!'")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'bodi/register.html', {'form':form})

	return render(request, 'bodi/register.html', {'form':form})

def customer_record(reguest, pk):
    if reguest.user.is_authenticated:
        #Look up Records
        customer_record = Record.objects.get(id=pk)
        return render(reguest, 'bodi/record.html', {'customer_record': customer_record})
    else:
        messages.warning(reguest, "'Ви не авторизовані :( '")
        return redirect('home')    


def delit_record (reguest, pk):
    if reguest.user.is_authenticated:
        delit_it = Record.objects.get(id=pk)
        delit_it.delete()
        messages.success(reguest, "Обьєкт успішно видалено")
        return redirect('home')
    else:
        messages.warning(reguest, "Ви не авторизовані :( ")
        return redirect('home')

def add_record(reguest,):
    form = AddRecordForm(reguest.POST or None)
    if reguest.user.is_authenticated:
        if reguest.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(reguest, "Запис створено ,,,,")
                return redirect('home')

        return render(reguest, 'bodi/add.html', {'form': form})
    else:
        messages.warning(reguest, "Ви не авторизовані :( ")
        return redirect('home')

def update_record(reguest, pk):
    if reguest.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(reguest.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(reguest, "Запис змінено ,,,,")
            return redirect('home')
        return render(reguest, 'bodi/update_record.html', {'form': form})
    else:
        messages.warning(reguest, "Ви не авторизовані :( ")
        return redirect('home')