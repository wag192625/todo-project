from django.shortcuts import render ,get_object_or_404, redirect
from django.utils import timezone

from datetime import datetime, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from django.urls import reverse

from .models import *
from .forms import  *
from .weather import proc_weather
from .crawling import newslist
from .calender import Calendar

import json
import calendar

def index(request):
    todo_list = Todo.objects.all()
    weather = proc_weather()
    newsList = newslist()
    context = {'todo_list': todo_list,
               'weather' : weather,
               'newsList': newsList}

    return render(request, 'pybo/todo_list.html', context)

def calendartest(request):
    return render(request, 'pybo/calendertest.html')


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





class CalendarView(generic.ListView):
    model = Event
    template_name = 'pybo/calender.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        
        # d = get_date(self.request.GET.get('month', None)) #적용 안됨
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

# def get_date(req_day):
#     if req_day:
#         year, month = (int(x) for x in req_day.split('-'))
#         return datetime(year, month, day=1)
#     return datetime.today()

# def prev_month(d):
#     first = d.replace(day=1)
#     prev_month = first - timedelta(days=1)
#     month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
#     return month

# def next_month(d):
#     days_in_month = calendar.monthrange(d.year, d.month)[1]
#     last = d.replace(day=days_in_month)
#     next_month = last + timedelta(days=1)
#     month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
#     return month

# ----- 날짜 변경 -----
def get_date(req_day):
    try:
        if req_day: 
            year, month, day = (int(x) for x in req_day.split('-'))
            return datetime(year, month, day=1)
    except (ValueError, TypeError):
        pass
    return datetime.today().date()
def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    a = 'day=' + str(prev_month.year) + '-' + str(prev_month.month) + '-' + str(prev_month.day)
    return a
def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    a = 'day=' + str(next_month.year) + '-' + str(next_month.month) + '-' + str(next_month.day)
    return a
# ----- 날짜 변경 -----

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('pybo:calendar'))
    return render(request, 'pybo/event.html', {'form': form})

def eventDelete(request,event_id):
    event = get_object_or_404(Event, event_id)
    event.delete()
    return redirect('pybo:calendar')