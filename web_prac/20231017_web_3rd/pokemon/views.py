from django.shortcuts import render, redirect
from .models import Pokemon, Comment
from .forms import PokemonForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    pokemons = Pokemon.objects.all()
    context = {
        'pokemons':pokemons
    }
    return render(request, 'pokemon/index.html', context)

def detail(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'pokemon':pokemon,
        'comment_form':comment_form,
    }
    return render(request, 'pokemon/detail.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            pokemon = form.save()
            return redirect('pokemon:detail', pokemon.pk)
    else:
        form = PokemonForm()
    context = {
        'form':form
    }
    return render(request, 'pokemon/create.html', context)

@login_required
def update(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    if request.method == 'POST':
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokemon:detail', pokemon.pk)
    else:
        form = PokemonForm(instance=pokemon)
    context = {
        'pokemon':pokemon,
        'form':form,
    }
    return render(request, 'pokemon/update.html', context)

@login_required
def delete(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    pokemon.delete()
    return redirect('pokemon:index')