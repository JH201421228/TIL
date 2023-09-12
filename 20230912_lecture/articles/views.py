from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
def this(request):
    return render(request, 'this.html')

def my_page(request):
    return render(request, 'index2.html')
