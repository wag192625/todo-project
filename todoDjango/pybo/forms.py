from django import forms
from pybo.models import *
from django.forms import ModelForm, DateInput

class TodoForm(forms.ModelForm):
    class Meta :
        model = Todo
        fields = ['importance', 'text']
        # fields = ['importance', 'text', 'timer']
        # # 연동된 html에서 값을 입력받을 때
        # 모델의 필드 중 null=False 또는 blank=False로 설정된 필드가 폼에 포함되어 있어야 db에 저장 가능.
        # 폼에서 모든 '필수' 필드에 값을 입력해야 함. 

class NewsForm(forms.ModelForm):
    class Meta :
        model = NewsSave
        fields = ['news_title','news_content','news_writing','news_image','news_link']


class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)






    
#  importance = models.IntegerField(default= '1',     # 중요도
#                                      choices=[
#                                          (1,'1'),
#                                          (2,'2'),
#                                          (3,'3'),
#                                      ])
#     timer = models.TimeField(null = True)