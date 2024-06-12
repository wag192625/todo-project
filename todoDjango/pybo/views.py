from django.shortcuts import render ,get_object_or_404, redirect
from django.utils import timezone
from .models import Todo
from .forms import TodoForm

def index(request):
    todo_list = Todo.objects.all()
    context = {'todo_list': todo_list}
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