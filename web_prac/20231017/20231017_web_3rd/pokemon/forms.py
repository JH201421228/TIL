from django import forms
from .models import Pokemon, Comment

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
       

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)