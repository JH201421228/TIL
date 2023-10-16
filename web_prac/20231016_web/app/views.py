from django.shortcuts import render, redirect
from .models import App

# Create your views here.
def index(request):
    app = App.objects.all()
    context = {
        'pokemons':app
    }
    return render(request, 'app/index.html', context)


def detail(request, pk):
    app = App.objects.get(pk=pk)
    context = {
        'pokemon':app
    }
    return render(request, 'app/detail.html', context)

def new(request):
    return render(request, 'app/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    app = App(title=title, content=content)
    app.save()
    # return render(request, 'app/create.html')
    return redirect('app:detail', app.pk)

def delete(request, pk):
    app = App.objects.get(pk=pk)
    app.delete()
    return redirect('app:index')

def edit(request, pk):
    app = App.objects.get(pk=pk)
    context = {
        'pokemon':app
    }
    return render(request, 'app/edit.html', context)

def update(request, pk):
    title = request.POST.get('title')
    content = request.POST.get('content')
    app = App(title=title, content=content)
    app.save()
    return redirect('app:detail', app.pk)