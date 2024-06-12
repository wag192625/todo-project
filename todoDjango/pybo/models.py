from django.db import models

# Create your models here.
class Todo(models.Model) :
    importance = models.IntegerField(default= '1',     # 중요도
                                     choices=[
                                         (1,'1'),
                                         (2,'2'),
                                         (3,'3'),
                                     ])
    text = models.CharField(max_length=200)
    todo_check = models.BooleanField(default = False)
    timer = models.TimeField(null = True)
    create_date = models.DateField(auto_now_add = True) # 작성 날짜

    def __str__(self):
        return self.text

# class TodoDetail(models.Model):
#     todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
#     text = models.CharField(max_length=200)
#     todo_check = models.BooleanField(default = False)
#     create_date = models.DateTimeField()  # 필요한가?