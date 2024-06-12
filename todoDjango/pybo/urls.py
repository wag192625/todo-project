from django.urls import path
from . import views

# app_name은 써주는게 좋다.
app_name = 'pybo'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add_todo' ),
    # path('',) # 세부사항

]