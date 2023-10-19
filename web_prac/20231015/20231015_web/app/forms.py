from django import forms

class AppForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField()