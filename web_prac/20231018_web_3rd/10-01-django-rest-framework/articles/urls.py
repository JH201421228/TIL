from django.urls import path
from articles import views


urlpatterns = [
    path('articles/', views.article_index),
    path('articles/<int:article_pk>/', views.article_detail),
]
