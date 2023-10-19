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
    comments = pokemon.comment_set.all()
    context = {
        'pokemon':pokemon,
        'comment_form':comment_form,
        'comments':comments,
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

@login_required
def comment_create(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.pokemon = pokemon
        comment_form.save()
        return redirect('pokemon:detail', pokemon.pk)
    context = {
        'pokemon':pokemon,
        'comment_form':comment_form,
    }
    return render(request, 'pokemon/detail.html', context)


@login_required
def comments_delete(request, pokemon_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('pokemon:detail', pokemon_pk)


@login_required
def likes(request, pokemon_pk):
    pokemon = Pokemon.objects.get(pk=pokemon_pk)
    if request.user in pokemon.like_users.all():
        pokemon.like_users.remove(request.user)
    else:
        pokemon.like_users.add(request.user)
    return redirect('pokemon:index')