from django.urls import path
from . import views

# app_name은 써주는게 좋다.
app_name = 'pybo'
urlpatterns = [
    path('', views.index, name='index'),
    # html에서 {% url 'pybo:index' %} 가 name='index'로 연결, views의 index 함수로 넘어가고 rander로 해당 페이지로 이동
    path('add_todo/', views.add_todo, name='add_todo'),
    path('<int:todo_id>/edit_todo/', views.edit_todo, name='edit_todo'),
    path('save_news/', views.save_news, name='save_news'),
    path('calendar/',views.CalendarView.as_view(), name='calendar'),
    path('calendartest/',views.calendartest, name='calendartest'),
    # path(r'event/new/$', views.event, name='event_new'),
    path('event/new/', views.event, name='event_new'),
    # path(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    path('event/edit/<event_id>)/', views.event, name='event_edit'),
]
