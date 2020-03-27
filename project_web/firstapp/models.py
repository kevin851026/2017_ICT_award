from django.db import models

class User(models.Model):
    acount = models.CharField(max_length=50)              #帳號
    area  = models.CharField(max_length=30,default="")    #地區
    gender  = models.IntegerField(default=-1)             #性別
    def __str__(self):
        return self.acount
class party(models.Model):
    acount = models.ForeignKey(User)                      #帳號
    year = models.CharField(max_length=30,default="")   #年份
    tendency = models.IntegerField(default=-1)            #傾向
    def __str__(self):
        return str(self.acount)
class article(models.Model):
    author = models.CharField(max_length=30,default="") #作者
    title = models.CharField(max_length=50,default="")  #文章標題
    context = models.TextField(default="")              #文章內容
    time   =models.CharField(max_length=50,default="")  #建立時間
    pusher = models.TextField(default="")                 #推文者
    blue_p = models.PositiveIntegerField(default=0)       #藍黨正面
    blue_n = models.PositiveIntegerField(default=0)       #藍黨負面
    green_p = models.PositiveIntegerField(default=0)      #藍黨負面
    green_n = models.PositiveIntegerField(default=0)      #藍黨負面
    male_p = models.PositiveIntegerField(default=0)       #藍黨負面
    male_n = models.PositiveIntegerField(default=0)       #藍黨負面
    female_p = models.PositiveIntegerField(default=0)     #藍黨負面
    female_n = models.PositiveIntegerField(default=0)     #藍黨負面
    def __str__(self):
        return self.title
class push(models.Model):
    pusher = models.CharField(max_length=30,default="")  #推文者
    content = models.TextField(default="")               #推文內容
    time = models.CharField(max_length=50,default="")    #推文時間
    tag = models.SmallIntegerField(default="")           #標籤
    author = models.CharField(max_length=30,default="")  #文章作者
    title = models.ForeignKey(article,null=True)         #外鍵
    mood = models.IntegerField(default=0)                #正負面
    title_value = models.CharField(max_length=50,default="")  #文章標題
    def __str__(self):
        return self.pusher
