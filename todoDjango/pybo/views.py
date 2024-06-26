from django.shortcuts import render ,get_object_or_404, redirect
from django.utils import timezone
from .models import Todo
from .forms import TodoForm
from .forms import NewsSave
from .weather import proc_weather
from .crawling import newslist
import json


def index(request):
    todo_list = Todo.objects.all()
    weather = proc_weather()
    newsList = newslist()
    context = {'todo_list': todo_list,
               'weather' : weather,
               'newsList': newsList}

    return render(request, 'pybo/todo_list.html', context)



# def add_todo(request):
#     form = TodoForm()
#     return render(request, 'pybo/todo_form.html', {'form':form})


def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid(): #유효성 검사
            todo = form.save(commit= False)
            todo.create_date = timezone.now()
            todo.save()
            return redirect('pybo:index')
    else:
        form = TodoForm()
    return render(request, 'pybo/todo_form.html', {'form': form})

def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('pybo:index')
    else:
        form = TodoForm(instance=todo)
    context= {'form':form}
    return render(request, 'pybo/todo_form.html', context)

def save_news(request):
    if request.method == 'POST' :
        form = NewsSave(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('pybo:index')
    else:
        form = NewsSave()
    return render(request, 'pybo/todo_list.html', {'form': form})

# # 챗지피티
# def save_news(request, title, content, writing, image, link):
#     news, created = NewsSave.objects.get_or_create(
#         news_title=title,
#         news_link=link,
#         news_content=content,
#         news_writing=writing,
#         news_image=image
#     )
#     if created:
#         news.save()
#     return redirect('pybo:index')