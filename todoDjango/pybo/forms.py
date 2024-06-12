from django import forms
from pybo.models import Todo

class TodoForm(forms.ModelForm):
    class Meta :
        model = Todo
        fields = ['importance', 'text', 'timer']
