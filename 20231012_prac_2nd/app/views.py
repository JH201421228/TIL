from django.shortcuts import render, redirect
from .models import App
from .forms import AppForm

# Create your views here.
def index(request):
    apps = App.objects.all()
    context = {
        'apps':apps,
    }
    return render(request, 'app/index.html', context)

def detail(request, pk):
    app = App.objects.get(pk=pk)
    context = {
        'app':app
    }
    return render(request, 'app/detail.html', context)

# def new(request):
#     return render(request, 'app/new.html')
# def new(request):
#     form = AppForm()
#     context = {
#         'form':form
#     }
#     return render(request, 'app/new.html', context)

# def create(request):
#     title = request.POST.get('title')
#     content = request.POST.get('content')

#     app = App(title=title, content=content)
#     app.save()

#     return redirect('app:detail', app.pk)


# def create(request):
#     form = AppForm(request.POST)
#     if form.is_valid():
#         app = form.save()
#         return redirect('app:detail', app.pk)
#     context = {
#         'form':form
#     }
#     return render(request, 'app/new.html', context)

def create(request):
    if request.method == 'POST':
        form = AppForm(request.POST)
        if form.is_valid():
            app = form.save()
            return redirect('app:detail', app.pk)
    else:
        form = AppForm()
    context = {
        'form':form
    }
    return render(request, 'app/new.html', context)

def delete(request, pk):
    app = App.objects.get(pk=pk)
    app.delete()
    return redirect('app:index')

# def edit(request, pk):
#     app = App.objects.get(pk=pk)
#     context = {
#         'app':app
#     }
#     return render(request, 'app/edit.html', context)

# def edit(request, pk):
#     app = App.objects.get(pk=pk)
#     form = AppForm(instance=app)
#     context = {
#         'app':app,
#         'form':form
#     }
#     return render(request, 'app/edit.html', context)

# def update(request, pk):
#     app = App.objects.get(pk=pk)
#     app.title = request.POST.get('title')
#     app.content = request.POST.get('content')
#     app.save()
#     return redirect('app:detail', app.pk)

# def update(request, pk):
#     app = App.objects.get(pk=pk)
#     form = AppForm(request.POST, instance=app)
#     if form.is_valid():
#         form.save()
#         return redirect('app:detail', app.pk)
#     context = {
#         'form':form
#     }
#     return render(request, 'app/edit.html', context)

def update(request, pk):
    app = App.objects.get(pk=pk)
    if request.method == 'POST':
        form = AppForm(request.POST, instance=app)
        if form.is_valid():
            form.save()
            return redirect('app:detail', app.pk)
    else:
        form = AppForm(instance=app)
    context = {
        'app':app,
        'form':form,
    }
    return render(request, 'app/update.html')