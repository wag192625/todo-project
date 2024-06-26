from django.urls import path
from . import views

# app_name은 써주는게 좋다.
app_name = 'pybo'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('<int:todo_id>/edit_todo/', views.edit_todo, name='edit_todo'),
    path('save_news/', views.save_news, name='save_news'),

    # 챗지피티
    # path('save_news/<str:title>/<str:content>/<str:writing>/<str:image>/<str:link>/', views.save_news, name='save_news'),
]