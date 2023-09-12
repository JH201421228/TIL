from django.shortcuts import render

# Create your views here.
def babo(request):
    return render(request, 'index.html')