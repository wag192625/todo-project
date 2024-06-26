from django import forms
from pybo.models import Todo
from pybo.models import NewsSave

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


#  importance = models.IntegerField(default= '1',     # 중요도
#                                      choices=[
#                                          (1,'1'),
#                                          (2,'2'),
#                                          (3,'3'),
#                                      ])
#     timer = models.TimeField(null = True)