from firstapp.models import article,User,push,party
from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
import pyprind
import os
import random
from bs4 import BeautifulSoup
# Create your views here.
def home(request):
    #article.objects.all().delete()
    #User.objects.all().delete()
    #push.objects.all().delete()
    #party.objects.all().delete()
    return render(request, 'home.html', locals())
def test(request):
    pushes = push.objects.all()
    pushes=pushes[110000:]
    x=len(pushes)
    for i in pushes:
        try:
            tmp=article.objects.filter(title=i.title_value,author=i.author)
            i.title=tmp[0]
            i.save()
            print(x)
            x-=1
        except:
            print(i)
            x-=1
    return render(request, 'home.html', locals())
def idlist(request):
    flag=0
    try:
        keyword = request.GET['keyword']        #取得關鍵字
        gender = request.GET['gender']          #取得性別
        flag=1
    except:
        print("No get input")
    allResult_p=[]
    allResult_n=[]
    alluser_p=[]
    alluser_n=[]
    if flag==1:
        articles = article.objects.filter(title__contains=keyword) #依照關鍵字向資料庫拉資料
        p_user=[]
        n_user=[]
        for i in articles:                                         #分開正負面推文者
            for j in i.push_set.all() :
                if j.mood==1:
                    if j.pusher not in p_user:
                        p_user.append(j.pusher)
                elif j.mood==0:
                    if j.pusher not in n_user:
                        n_user.append(j.pusher)
        p_user=p_user[:300]
        n_user=n_user[:300]
        b_user_p=[]
        g_user_p=[]
        b_user_n=[]
        g_user_n=[]
        for i in p_user:                                            #分開不同政黨正面推文者
            tmp=User.objects.get(acount=i)
            if tmp.gender==0:
                b_user_p.append(i)
            else:
                g_user_p.append(i)
        for i in n_user:                                            #分開不同政黨負面推文者
            tmp=User.objects.get(acount=i)
            if tmp.gender==0:
                b_user_n.append(i)
            else:
                g_user_n.append(i)
        b_user_p=b_user_p[:100]
        g_user_p=g_user_p[:100]
        b_user_n=b_user_n[:100]
        g_user_n=g_user_n[:100]
        for i in b_user_p if gender=='0' else g_user_p:
            acount=User.objects.get(acount=i).party_set.all()
            tmp={}
            tmp["acount"]=i
            tmp["tendency"]={}
            for j in acount:
                tmp["tendency"][j.year]=j.tendency
            alluser_p.append(tmp)
        for i in b_user_n if gender=='0' else g_user_n:
            acount=User.objects.get(acount=i).party_set.all()
            tmp={}
            tmp["acount"]=i
            tmp["tendency"]={}
            for j in acount:
                tmp["tendency"][j.year]=j.tendency
            alluser_n.append(tmp)
        allResult_p=json.dumps(alluser_p,ensure_ascii=False)
        allResult_n=json.dumps(alluser_n,ensure_ascii=False)
    return render(request, 'idlist.html', locals())
def get_art(request):  #回傳文章統計json
    flag=0
    try:
        keyword = request.GET['keyword']
        flag=1
    except:
        print("No get input")
    allResult=[]
    if flag==1:
        print(keyword)
        articles = article.objects.filter(title__contains=keyword)
        allResult=[]
        tmp={}
        tmp['blue_p']=0
        tmp['blue_n']=0
        tmp['green_p']=0
        tmp['green_n']=0
        tmp['male_p']=0
        tmp['male_n']=0
        tmp['female_p']=0
        tmp['female_n']=0
        for i in articles:
            tmp['blue_p']+=i.blue_p
            tmp['blue_n']+=i.blue_n
            tmp['green_p']+=i.green_p
            tmp['green_n']+=i.green_n
            tmp['male_p']+=i.male_p
            tmp['male_n']+=i.male_n
            tmp['female_p']+=i.female_p
            tmp['female_n']+=i.female_n
        allResult.append(tmp)
        allResult=json.dumps(allResult,ensure_ascii=False)
    return JsonResponse(allResult, safe=False)
def update_user(request):       #更新資料庫
    allResult=[]
    tmp=[]
    acount_input_data=[]
    article_input_data=[]
    push_input_data=[]
    for i in os.walk(".\idDictpoli"):
        tmp.append(i)
    for i in tmp[0][2]:
        acount_input_data.append(User(acount=i))
        with open('.\idDictpoli\\'+ i, encoding='utf8') as f:
            print(i)
            data=json.load(f)
            for j in data['articles']:
                article_input_data.append(article(author=i,title=j['title'],
                    context=j['context'],time=j['time']))
            for j in data['pushes']:
                if j['tag']==2:
                    x=0
                elif j['tag']==0:
                    x=-1
                else:
                    x=1
                push_input_data.append(push(pusher=i,content=j['content'],time=j['idt'],mood=x,tag=j['tag']
                    ,author=j['reply_article']['author'],title_value=j['reply_article']['title']))

    User.objects.bulk_create(acount_input_data)
    article.objects.bulk_create(article_input_data)
    push.objects.bulk_create(push_input_data)

    users= User.objects.all()
    party_input_data=[]
    for i in users:
        for j in range(2013,2018):
            party_input_data.append(party(acount=i,year=j,tendency=random.randint(0,2)))
    party.objects.bulk_create(party_input_data)
    return render(request, 'home.html', locals())
