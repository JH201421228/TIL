from django.shortcuts import render, redirect
from .models import App, Comment
from .forms import AppForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    apps = App.objects.all()
    context = {
        'apps':apps,
    }
    return render(request, 'app/index.html', context)

def detail(request, pk):
    app = App.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = app.comment_set.all()
    context = {
        'app':app,
        'commnet_form':comment_form,
        'comments':comments,

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

@login_required
def create(request):
    if request.method == 'POST':
        form = AppForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.user = request.user
            app.save()
            return redirect('app:detail', app.pk)
    else:
        form = AppForm()
    context = {
        'form':form
    }
    return render(request, 'app/create.html', context)

@login_required
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

@login_required
def update(request, pk):
    app = App.objects.get(pk=pk)
    if request.user == app.user:
        if request.method == 'POST':
            form = AppForm(request.POST, instance=app)
            if form.is_valid():
                form.save()
                return redirect('app:detail', app.pk)
        else:
            form = AppForm(instance=app)
    else:
        return redirect('app:index')
    context = {
        'app':app,
        'form':form,
    }
    return render(request, 'app/update.html')

def comments_create(request, pk):
    app = App.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.app = app
        comment_form.save()
        return redirect('app:detail', app.pk)
    context = {
        'app':app,
        'commnet_form':comment_form,
    }
    return render(request, 'app/detail.html', context)

def comments_delete(request, app_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('app:detail', app_pk)