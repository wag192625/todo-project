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

class NewsSave(models.Model) :
    news_title = models.CharField(max_length=200, null= False)
    news_content = models.CharField(max_length=300, null= False)
    news_writing = models.CharField(max_length=20,null= True)
    news_image = models.URLField(max_length=200, null= True)
    news_link = models.URLField(max_length=200, null= False)

    def __str__(self):
        return self.news_title

# class weatherDB(models.Model):
#     timestamp = models.DateTimeField(auto_now=True, null=True, blank=True)
#     temp = models.IntegerField(blank=True, null=True)   # 온도
#     humidity = models.IntegerField(blank=True, null=True)   #습도
#     rainType = models.CharField(max_length=20, blank=True, null=True)   #한시간 동안 강수량
#     sky = models.IntegerField(blank=True, null=True)    # 하늘 상태
#     sky2 = models.IntegerField(blank=True, null=True)    # 하늘 상태

#     def __str__(self):
#         return str(self.timestamp)