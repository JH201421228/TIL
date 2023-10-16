from django.shortcuts import render, redirect
from .models import Pokemons
from .forms import PokemonsForm

# Create your views here.
def index(request):
    pokemons = Pokemons.objects.all()
    context = {
        'pokemons':pokemons
    }
    return render(request, 'pokemons/index.html', context)

def detail(request, pk):
    pokemon = Pokemons.objects.get(pk=pk)
    context = {
        'pokemon':pokemon
    }
    return render(request, 'pokemons/detail.html', context)

# def new(request):
#     pokemon = PokemonsForm
#     context = {
#         'pokemon':pokemon,
#     }
#     return render(request, 'pokemons/new.html', context)

# def create(request):
#     name = request.POST.get('name')
#     describe = request.POST.get('describe')
#     pokemon = Pokemons(name=name, describe=describe)
#     pokemon.save()
#     return redirect('pokemons:detail', pokemon.pk)

# def create(request):
#     form = PokemonsForm(request.POST)
#     if form.is_valid():
#         pokemon = form.save()
#         return redirect('pokemons:detail', pokemon.pk)
#     context = {
#         'pokemon':form,
#     }
#     return render(request, 'pokemons/new.html', context)


def delete(request, pk):
    pokemon = Pokemons.objects.get(pk=pk)
    pokemon.delete()
    return redirect('pokemons:index')

# def edit(request, pk):
#     pokemon = Pokemons.objects.get(pk=pk)
#     context = {
#         'pokemon':pokemon
#     }
#     return render(request, 'pokemons/edit.html', context)

def edit(request, pk):
    pokemon = Pokemons.objects.get(pk=pk)
    form = PokemonsForm(instance=pokemon)
    context = {
        'pokemon':pokemon,
        'form':form
    }
    return render(request, 'pokemons/edit.html', context)

# def update(request, pk):
#     pokemon = Pokemons.objects.get(pk=pk)
#     pokemon.name = request.POST.get('name')
#     pokemon.describe = request.POST.get('describe')
#     pokemon.save()
#     return redirect('pokemons:detail', pk)

def update(request, pk):
    pokemon = Pokemons.objects.get(pk=pk)
    form = PokemonsForm(request.POST, instance=pokemon)
    if form.is_valid():
        form.save()
        return redirect('pokemons:detail', pokemon.pk)
    context = {
        'form':form,
    }
    return render(request, 'pokemons/edit.html', context)

def create(request):
    if request.method == 'POST':
        form = 