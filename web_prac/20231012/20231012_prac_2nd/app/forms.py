from django import forms
from .models import App, Comment

# class AppForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     content = forms.CharField(widget=forms.Textarea)
#     # content = forms.TextInput()

class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ('title', 'content',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)