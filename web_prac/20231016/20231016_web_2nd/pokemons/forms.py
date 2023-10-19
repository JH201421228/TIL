from django import forms
from .models import Pokemons

# class PokemonsForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     describe = forms.CharField()
#     catch_date = forms.DateTimeield()

class PokemonsForm(forms.ModelForm):
    class Meta:
        model = Pokemons
        fields = '__all__'