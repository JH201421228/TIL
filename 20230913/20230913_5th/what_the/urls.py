from django.urls import path, include
from . import views

app_name = 'what_the'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>', views.func, name='why_do_this')
]
