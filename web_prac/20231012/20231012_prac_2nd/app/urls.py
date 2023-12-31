from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:pk>', views.detail, name='detail'),
    # path('new/', views.new, name='new'),
    path('create', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comment/', views.comments_create, name='comments_create'),
    path('<int:app_pk>/comment/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]
