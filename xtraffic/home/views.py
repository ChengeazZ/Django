from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')

def page1(request):
    return render(request, 'drugs.html')

def page2(request):
    return render(request, 'slaves.html')

def page3(request):
    return render(request, 'guns.html')

def page4(request):
    return render(request, 'prostitutes.html')