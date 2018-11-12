from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def sportEquip(request):
    return render(request, 'myapp/sportequip.html')

def properties(request):
    return render(request, 'myapp/properties.html')
def login(request):
    return render(request, 'myapp/login.html')
def reset(request):
    return render(request, 'myapp/reset.html')
