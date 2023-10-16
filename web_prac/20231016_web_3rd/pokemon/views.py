from django.shortcuts import render, redirect
from .models import Pokemon
from .forms import PokemonForm

# Create your views here.
def index(request):
    pokemons = Pokemon.objects.all()
    context = {
        'pokemons':pokemons
    }
    return render(request, 'pokemon/index.html', context)

def detail(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    context = {
        'pokemon':pokemon
    }
    return render(request, 'pokemon/detail.html', context)

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
        'form':form
    }
    return render(request, 'pokemon/update.html', context)

def delete(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    pokemon.delete()
    return redirect('pokemon:index')
