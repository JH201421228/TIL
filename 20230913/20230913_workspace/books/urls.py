from django.urls import path, include
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:author>', views.what_the, name='fxxk')
]
