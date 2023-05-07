from django.shortcuts import render


def home(request):
    return render(request, 'bodi/home.html', {})
