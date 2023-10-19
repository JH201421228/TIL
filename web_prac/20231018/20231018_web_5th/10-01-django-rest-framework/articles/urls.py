from django.urls import path
from articles import views


urlpatterns = [
    path('articles/', views.index),
    path('articles/<int:article_pk>/', views.detail),
]
