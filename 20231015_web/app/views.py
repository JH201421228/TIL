from django.shortcuts import render, redirect
from .forms import AppForm

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def new(request):
    form = AppForm()
    context = {
        'form':form
    }
    return render(request, 'app/new.html', context)

def create(request):
    